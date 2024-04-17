# type: ignore[attr-defined]
"""PyCXpress is a high-performance hybrid framework that seamlessly integrates Python and C++ to harness the flexibility of Python and the speed of C++ for efficient and expressive computation, particularly in the realm of deep learning and numerical computing."""

__all__ = [
    "TensorMeta",
    "ModelAnnotationCreator",
    "ModelAnnotationType",
    "ModelRuntimeType",
    "convert_to_spec_tuple",
    "get_include",
    "version",
]

import sys
from pathlib import Path

if sys.version_info >= (3, 8):
    from importlib import metadata as importlib_metadata
else:
    import importlib_metadata


def get_version() -> str:
    try:
        return importlib_metadata.version(__name__)
    except importlib_metadata.PackageNotFoundError:  # pragma: no cover
        return "unknown"


version: str = get_version()


from .core import TensorMeta, ModelAnnotationCreator, ModelAnnotationType, ModelRuntimeType
from .core import convert_to_spec_tuple


def get_include() -> str:
    return str(Path(__file__).parent.absolute()/"include")