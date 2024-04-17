import re

from bs4 import BeautifulSoup
from mkdocs.plugins import BasePlugin as MkDocsBasePlugin

from inline_svg.config import InlineSvgConfig
from inline_svg.util import (
    get_svg_data,
    get_svg_tag,
    include_assets,
    log,
)


class InlineSvgPlugin(MkDocsBasePlugin[InlineSvgConfig]):
    def on_config(self, config, **_kwargs):
        self.config.site_url = config.get("site_url", "/")
        self.config.site_dir = config["site_dir"]
        log.debug(f"Config: {self.config}")

        return config

    def on_page_content(self, html: str, *, files, **_kwargs):
        log.debug("on_page_content")
        soup = BeautifulSoup(html, "html.parser")

        for img_tag in soup.find_all("img", {"src": re.compile(r"(/svg/)|(\.svg$)")}):
            if self.config.image_should_be_ignored(img_tag["alt"]):
                continue

            log.debug(f'inlining {img_tag} -> {img_tag["src"]}')
            svg_data = get_svg_data(img_tag["src"], files, self.config)
            if svg_data:
                svg_tag = get_svg_tag(svg_data, self.config)
                if self.config.include_assets:
                    svg_tag = include_assets(svg_tag, files, self.config)
                img_tag.replace_with(svg_tag)

        return str(soup)
