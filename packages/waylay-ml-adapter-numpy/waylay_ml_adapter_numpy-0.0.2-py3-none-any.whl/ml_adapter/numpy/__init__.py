"""ML Adapter for numpy."""

from .adapter import V1NumpyModelAdapter
from .marshall import V1NumpyMarshaller

__all__ = ["V1NumpyMarshaller", "V1NumpyModelAdapter"]
