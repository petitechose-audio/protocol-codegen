"""
Protocol CodeGen - Core module

Provides the core type system, message definitions, and validation.
"""

from protocol_codegen.core.field import PrimitiveField, CompositeField, Type, populate_type_names
from protocol_codegen.core.message import Message
from protocol_codegen.core.types import BUILTIN_TYPES, BuiltinTypeDef
from protocol_codegen.core.loader import TypeRegistry
from protocol_codegen.core.validator import ProtocolValidator
from protocol_codegen.core.allocator import allocate_message_ids

__all__ = [
    "PrimitiveField",
    "CompositeField",
    "Type",
    "populate_type_names",
    "Message",
    "BUILTIN_TYPES",
    "BuiltinTypeDef",
    "TypeRegistry",
    "ProtocolValidator",
    "allocate_message_ids",
]
