"""ML Adapter mixing providing access to assets."""

from typing import Optional, Self

from ml_adapter.api.types import AssetLocation, as_location

from .base import Asset
from .root import AssetsRoot


class WithAssets:
    """Mixin for a configuration backed by assets."""

    assets: AssetsRoot

    def __init__(self, location: Optional[AssetLocation | str] = None, **kwargs):
        """Create assets support."""
        self.assets = AssetsRoot(location=as_location(location), **kwargs)

    async def save(self, **kwargs) -> Self:
        """Save the current assets when accessed."""
        await self.assets.save(**kwargs)
        return self

    async def load(self, *asset_classes: type["Asset"], **kwargs) -> Self:
        """Load all assets."""
        await self.assets.load(*asset_classes, **kwargs)
        return self

    async def save_archive(
        self, target: Optional[AssetLocation | str] = None, **kwargs
    ) -> AssetLocation:
        """Save the archive."""
        return await self.assets.save_archive(target, **kwargs)

    @property
    def location(self) -> AssetLocation:
        """Return the location of the stored assets."""
        return self.assets.location
