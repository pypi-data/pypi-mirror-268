from __future__ import annotations

import os
import re
from typing import TYPE_CHECKING

import requests
from bs4 import BeautifulSoup
from mkdocs.plugins import get_plugin_logger
from mkdocs.structure.files import (
    File as MkDocsFile,
)
from mkdocs.structure.files import (
    Files as MkDocsFiles,
)

from inline_svg.__version__ import __version__

if TYPE_CHECKING:
    from inline_svg.config import InlineSvgConfig


log = get_plugin_logger(__name__)

tag_blocklist = "script"
user_agent_string = f"{__package__}/{__version__}"
REQUESTS_TIMEOUT = 10


def _sanitize_svg(svg_soup):
    for tag in svg_soup.findAll():
        if tag.name.lower() in tag_blocklist:
            tag.extract()
            continue

        for attr in tag.attrs:
            if attr.lower().startswith("on"):
                tag.attrs.remove(attr)


# TODO: make it configurable
color_mappings = {
    "white": "var(--md-default-bg-color)",
    "#ffffff": "var(--md-default-bg-color)",
    "black": "var(--md-default-fg-color)",
    "#000000": "var(--md-default-fg-color)",
    "#000": "var(--md-default-fg-color)",
    "#ffffa0": "var(--bytefield-yellow)",
    "#ffb0a0": "var(--bytefield-red)",
    "#e4b5f7": "var(--bytefield-purple)",
    "#a0ffa0": "var(--bytefield-green)",
    "#a0fafa": "var(--bytefield-blue)",
    "#F1F1F1": "var(--plantuml-grey)",
    "#181818": "var(--plantuml-black)",
    "#ddd": "var(--vegalite-stroke)",
    "#888": "var(--vegalite-stroke2)",
    "#c30d24": "var(--vegalite-red)",
    "#f3a583": "var(--vegalite-orange)",
    "#cccccc": "var(--vegalite-grey)",
    "#94c6da": "var(--vegalite-light-blue)",
    "#1770ab": "var(--vegalite-blue)",
    "#33322E": "var(--nomnoml-stroke)",
    "#eee8d5": "var(--nomnoml-yellow)",
    "#fdf6e3": "var(--nomnoml-yellow2)",
}


def _patch_style(svg_soup):
    for element in svg_soup.findAll(["polygon", "ellipse", "rect", "line", "path", "text", "g"]):
        if "fill" in element.attrs:
            element.attrs["fill"] = color_mappings.get(element.attrs["fill"]) or element.attrs["fill"]
        if "stroke" in element.attrs:
            element.attrs["stroke"] = color_mappings.get(element.attrs["stroke"]) or element.attrs["stroke"]

        if "style" in element.attrs:
            for color, replacement in color_mappings.items():
                element.attrs["style"] = element.attrs["style"].replace(color, replacement)

        if element.name == "text" and "fill" not in element.attrs:
            element.attrs["fill"] = "var(--md-default-fg-color)"


def _get_local_file_from_url(url: str, files: MkDocsFiles, config: InlineSvgConfig) -> MkDocsFile | None:
    return files.get_file_from_path(url.removeprefix(config.site_url))


def get_svg_data(url: str, files: MkDocsFiles, config: InlineSvgConfig) -> str | None:
    static_file = _get_local_file_from_url(url, files, config)
    log.debug("_get_local_file_from_url(url, files, config): %s", static_file)
    if static_file:
        with open(static_file.abs_src_path) as file:
            svg_data = file.read()
        files.remove(static_file)
        return svg_data

    response = requests.get(url, headers={"User-Agent": user_agent_string}, timeout=REQUESTS_TIMEOUT)
    if not response.ok:
        log.error("Could not download [%s: %s %s]", url, response.status_code, response.reason)
        return None

    return response.text


def include_assets(svg_soup, files: MkDocsFiles, config: InlineSvgConfig):
    url_regex = r'url\(["\']([^"\']+)["\']\)'

    def _css_url(url: str) -> str:
        return f'url("{url}")'

    def _download_asset(match: re.Match) -> str:
        url = match.groups("url")[0]
        if _get_local_file_from_url(url, files, config):
            log.debug("asset not remote: %s, leaving as it is", url)
            return _css_url(url)

        file_name = url.split("/")[-1]
        file_src = os.path.join(config.temp_dir.name, file_name)
        file_path = os.path.join(config.site_url, config.asset_dir, file_name)
        if os.path.exists(file_src):
            log.debug("asset already present: %s -> using present %s", url, file_path)
            return _css_url(file_path)

        response = requests.get(url, headers={"User-Agent": user_agent_string}, timeout=REQUESTS_TIMEOUT)
        if not response.ok:
            log.error("Could not download [%s]: %s %s], skipping", url, response.status_code, response.reason)
            return _css_url(url)

        asset_data = response.content
        with open(file_src, "xb") as file:
            file.write(asset_data)

        files.append(
            MkDocsFile(
                path=file_name,
                src_dir=config.temp_dir.name,
                dest_dir=os.path.join(config.site_dir, config.asset_dir),
                use_directory_urls=False,
            )
        )
        log.debug("include asset: %s -> %s", url, file_path)
        return _css_url(file_path)

    for tag in svg_soup.find_all("style"):
        tag.string = re.sub(url_regex, _download_asset, tag.string)

    return svg_soup


def get_svg_tag(svg_data, config: InlineSvgConfig):
    svg_soup = BeautifulSoup(svg_data, "html.parser")

    # suppress upscaling of smaller images
    if "width" in svg_soup.svg.attrs:
        max_width = svg_soup.svg.attrs["width"]
        svg_soup.svg.attrs["style"] = f"max-width: {max_width}"

    # set the viewbox if not present
    if "viewbox" not in svg_soup.svg.attrs:
        if ("height" in svg_soup.svg.attrs) and ("width" in svg_soup.svg.attrs):
            height = "".join(filter(str.isdigit, svg_soup.svg.attrs["height"]))
            width = "".join(filter(str.isdigit, svg_soup.svg.attrs["width"]))
            svg_soup.svg.attrs["viewbox"] = f"0 0 {width} {height}"
        else:
            log.error("SVG does not contain viewbox or height and width.")

    # remove unnecessary attrs
    svg_soup.svg.attrs = {
        k: v for k, v in svg_soup.svg.attrs.items() if k in ["version", "viewbox", "style", "width", "height"]
    }

    svg_soup.svg.attrs["id"] = __package__
    _sanitize_svg(svg_soup)

    if config.patch_style:
        _patch_style(svg_soup)

    return svg_soup.svg
