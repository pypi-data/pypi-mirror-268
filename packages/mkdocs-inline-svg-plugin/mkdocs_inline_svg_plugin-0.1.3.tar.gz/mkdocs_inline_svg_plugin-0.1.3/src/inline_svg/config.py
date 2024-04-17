from tempfile import TemporaryDirectory

from mkdocs.config.base import Config as MkDocsBaseConfig
from mkdocs.config.config_options import (
    Deprecated as MkDocsConfigDeprecated,
)
from mkdocs.config.config_options import (
    Type as MkDocsConfigType,
)

WILDCARD = "*"


class InlineSvgConfig(MkDocsBaseConfig):
    alt_name = MkDocsConfigType(str, default=WILDCARD)
    include_assets = MkDocsConfigType(bool, default=False)
    asset_dir = MkDocsConfigType(str, default="assets/")
    patch_style = MkDocsConfigType(bool, default=False)
    site_url: str
    site_dir: str
    temp_dir = TemporaryDirectory()

    AltName = MkDocsConfigDeprecated(moved_to="alt_name")
    IncludeAssets = MkDocsConfigDeprecated(moved_to="include_assets")
    AssetDir = MkDocsConfigDeprecated(moved_to="asset_dir")
    PatchStyle = MkDocsConfigDeprecated(moved_to="patch_style")

    def __repr__(self):
        repr_dict = self.data.copy()
        # Add non-user-dict entries to repr
        repr_dict.update({"site_url": self.site_url, "site_dir": self.site_dir, "temp_dir": self.temp_dir})
        return repr(repr_dict)

    def image_should_be_ignored(self, img_alt_name) -> bool:
        return self.alt_name not in {WILDCARD, img_alt_name}
