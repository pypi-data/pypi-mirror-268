"""Mapping and validation of remote data to and from model inference."""

import abc
from abc import ABC
from typing import Any, Generic, Optional

import ml_adapter.api.types as T


class RequestMarshaller(Generic[T.MREQ, T.RREQ], ABC):
    """Base class to marshall inference requests."""

    @abc.abstractmethod
    def map_request(self, request: T.RREQ, /, **kwargs) -> T.MREQ:
        """Convert a remote request to an model inference request."""

    @abc.abstractmethod
    def encode_request(
        self, request: T.MREQ, parameters: Optional[T.Parameters] = None, **kwargs
    ) -> T.RREQ:
        """Convert a model inference request to the remote protocol."""


class ResponseMarshaller(Generic[T.MRES, T.RREQ, T.RRES], ABC):
    """Base class to marshall inference responses."""

    @abc.abstractmethod
    def map_response(
        self,
        request: T.RREQ,
        response: T.MRES,
        output_params: Optional[dict[str, Any]] = None,
        /,
        **kwargs,
    ) -> T.RRES:
        """Convert a model inference response to the remote protocol."""

    @abc.abstractmethod
    def decode_response(
        self, response: T.RRES, /, **kwargs
    ) -> (T.MRES, Optional[T.Parameters]):
        """Decode a remote model inference response."""


class Marshaller(
    RequestMarshaller[T.MREQ, T.RREQ],
    ResponseMarshaller[T.MRES, T.RREQ, T.RRES],
    Generic[T.MREQ, T.MRES, T.RREQ, T.RRES],
    ABC,
):
    """Base class to marshall inference requests and responses."""


class NoMarshaller(
    RequestMarshaller[T.MREQ, T.MREQ],
    ResponseMarshaller[T.MRES, T.MREQ, T.MREQ],
    Generic[T.MREQ, T.MRES],
):
    """Identity marshaller."""

    def map_request(self, request: T.MREQ, /, **kwargs) -> T.MREQ:
        """Convert a remote request to an model inference request."""
        return request

    def encode_request(
        self, request: T.MREQ, parameters: T.Parameters | None = None, **kwargs
    ) -> T.MREQ:
        """Encode a tensor request with default input name."""
        return request

    def decode_response(
        self, response: T.MRES, /, **kwargs
    ) -> (T.MRES, Optional[T.Parameters]):
        """Decode the default tensor from a V1 response."""
        return response, {}

    def map_response(
        self,
        request: T.MREQ,
        response: T.MRES,
        output_params: Optional[dict[str, Any]] = None,
        /,
        **kwargs,
    ) -> T.MRES:
        """Convert a model inference response to the remote protocol."""
        return response
