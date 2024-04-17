"""ML Adapter base infrastructure."""

from .adapter import ModelAdapter, TensorModelAdapter
from .assets import WithAssets, WithManifest, WithOpenapi, WithPython
from .marshall import Marshaller
from .model import (
    DillModelAsset,
    JoblibModelAsset,
    SelfSerializingModelAsset,
    WithModel,
)

__all__ = [
    "ModelAdapter",
    "TensorModelAdapter",
    "WithAssets",
    "WithManifest",
    "WithOpenapi",
    "WithPython",
    "WithModel",
    "SelfSerializingModelAsset",
    "DillModelAsset",
    "JoblibModelAsset",
    "Marshaller",
]
