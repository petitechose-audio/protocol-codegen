"""
Protocol CodeGen - Generic bidirectional protocol code generator

Generate type-safe protocol code (C++, Java, Rust, etc.) from Python message definitions.

Examples:
    >>> from protocol_codegen.core import Message, Field, Flow, Type
    >>> msg = Message(
    ...     name="SENSOR_READING",
    ...     flow=Flow.DEVICE_TO_HOST,
    ...     description="Temperature sensor reading",
    ...     fields=[
    ...         Field('sensor_id', Type.UINT8),
    ...         Field('temperature', Type.INT16),
    ...     ]
    ... )
"""

__version__ = "1.0.0"
__author__ = "petitechose.audio"
__license__ = "MIT"

# Re-export main API
from protocol_codegen.core.field import PrimitiveField, CompositeField, Type
from protocol_codegen.core.message import Message

# Type will be populated dynamically when types are loaded
# from protocol_codegen.core.types import Type

__all__ = [
    "Message",
    "PrimitiveField",
    "CompositeField",
    "Type",
    # "Type",  # Will be available after types are loaded
    "__version__",
]
