"""
Protocol CodeGen - Type-safe protocol code generator

Generate type-safe protocol code (C++ and Java) from Python message definitions.

Examples:
    >>> from protocol_codegen.core.message import Message
    >>> from protocol_codegen.core.field import PrimitiveField
    >>> msg = Message(
    ...     description="Temperature sensor reading",
    ...     fields=[
    ...         PrimitiveField('sensor_id', type_name='uint8'),
    ...         PrimitiveField('temperature', type_name='int16'),
    ...     ]
    ... )
    >>> msg.name = 'SENSOR_READING'
"""

__version__ = "1.0.0"
__author__ = "petitechose.audio"
__license__ = "MIT"

# Re-export main API
from protocol_codegen.core.field import CompositeField, PrimitiveField, Type
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
