"""Serialization of models with pickling libraries (dill, joblib)."""

import inspect
from typing import Generic, Optional, TypeVar

import ml_adapter.api.types as T

from ..assets import AssetsFolder
from .base import ModelAsset

SMI = TypeVar("SMI", bound=T.SerializableModel)


class SelfSerializingModelAsset(ModelAsset[SMI], Generic[SMI]):
    """Model asset with own serialization methods."""

    PATH_PATTERNS = ["model.sav"]
    DEFAULT_PATH = "model.sav"
    MODEL_CLASS: Optional[type[SMI]] = None

    model_class: type[SMI]

    def __init__(
        self, parent: AssetsFolder, model_class: Optional[type[SMI]] = None, **kwargs
    ):
        """Create a self-serializing model asset."""
        super().__init__(parent, **kwargs)
        model_class = model_class or self.MODEL_CLASS
        if not model_class:
            raise TypeError(
                f'Loading a self-serializing model using "{self.__class__.__name__}"'
                ' requires a "model_class" argument.'
            )
        self.model_class = model_class

    async def load_content(self, **kwargs):
        """Load a model with its 'load' method."""
        model = self.model_class.load(self.location, **kwargs)
        if inspect.isawaitable(model):
            model = await model
        self.content = model

    async def save_content(self, **kwargs):
        """Save a model with its 'save' method."""
        res = self.content.save(self.location, **kwargs)
        if inspect.isawaitable(res):
            res = await res
