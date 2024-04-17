"""Model asset holder."""

from typing import Generic, Optional

import ml_adapter.api.types as T

from ..assets import WithAssets
from .base import ModelAsset
from .dill import DillModelAsset
from .joblib import JoblibModelAsset
from .serialize import SelfSerializingModelAsset

ModelAssetTypeList = list[type[ModelAsset]]


class WithModel(WithAssets, Generic[T.MI]):
    """Holder of model assets."""

    MODEL_ASSET_CLASSES = [DillModelAsset, JoblibModelAsset, SelfSerializingModelAsset]
    DEFAULT_MODEL_PATH: Optional[str] = "model.dill"
    MODEL_CLASS: Optional[type[T.MI]] = None

    _model_path: Optional[str] = None

    def __init__(
        self,
        model: Optional[T.MI] = None,
        model_path: Optional[str] = None,
        model_class: Optional[type[T.MI]] = None,
        is_dir: bool = False,
        **kwargs,
    ):
        """Register the manifest asset classes."""
        super().__init__(**kwargs)
        self.assets.asset_classes.extend(self.MODEL_ASSET_CLASSES)
        self._model_path = model_path
        self._model_class = model_class
        self._model_is_dir = is_dir
        if model:
            self.model = model
        self._init_model_asset()

    @property
    def model_class(self) -> type[T.MI]:
        """Return the current or supported model class."""
        if self.model:
            return self.model.__class__
        if self._model_class:
            return self._model_class
        if self.MODEL_CLASS:
            return self.MODEL_CLASS
        raise AttributeError("No model_class provided. ")

    @property
    def model_path(self) -> str:
        """Model path."""
        if self._model_path:
            return self._model_path
        if self.DEFAULT_MODEL_PATH:
            return self.DEFAULT_MODEL_PATH
        patterns = ",".join(
            set(f"'{p}'" for ac in self.MODEL_ASSET_CLASSES for p in ac.PATH_PATTERNS)
        )
        raise AttributeError(
            "No default model_path provided. "
            f"Please provide a path that matches any of {patterns}"
        )

    def _init_model_asset(self):
        model_asset_class = self.assets.asset_class_for(
            self.model_path, is_dir=self._model_is_dir
        )
        self.assets.add(
            model_asset_class,
            self.model_path,
            model_class=self._model_class or self.MODEL_CLASS,
        )

    @property
    def model_asset(self) -> ModelAsset:
        """The asset holding the model instance."""
        model_asset = self.assets.get(asset_type=ModelAsset)
        if model_asset is not None:
            return model_asset

        # lazy init
        self._init_model_asset()
        return self.assets.get_or_fail(asset_type=ModelAsset)

    @property
    def model(self) -> T.MI:
        """Get the model instance."""
        return self.model_asset.model

    @model.setter
    def model(self, model: T.MI):
        """Set the model instance."""
        if model is not None:
            self._model_class = model.__class__
        self.model_asset.model = model
