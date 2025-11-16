#!/usr/bin/env python3
"""
Quick test script for simple-sensor-network example
"""
import sys
from pathlib import Path

# Add protocol-codegen to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))
sys.path.insert(0, str(Path(__file__).parent / 'examples' / 'simple-sensor-network'))

print("="*70)
print("Testing simple-sensor-network example")
print("="*70)
print()

# Test 1: Import protocol_codegen
print("[1/5] Testing protocol_codegen imports...")
try:
    from protocol_codegen.core import BUILTIN_TYPES, PrimitiveField, Type, Message
    print(f"  OK: Loaded {len(BUILTIN_TYPES)} builtin types")
except Exception as e:
    print(f"  FAILED: {e}")
    sys.exit(1)

# Test 2: Load example fields
print("[2/5] Loading example fields...")
try:
    from field.sensor import sensor_id, sensor_value, sensor_info_array
    from field.color import color_rgb
    print(f"  OK: Loaded sensor fields")
except Exception as e:
    print(f"  FAILED: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Test 3: Load example messages
print("[3/5] Loading example messages...")
try:
    from message import ALL_MESSAGES
    print(f"  OK: Loaded {len(ALL_MESSAGES)} messages")
    for msg in ALL_MESSAGES:
        print(f"    - {msg.name}: {len(msg.fields)} fields")
except Exception as e:
    print(f"  FAILED: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Test 4: Load TypeRegistry
print("[4/5] Loading TypeRegistry...")
try:
    from protocol_codegen.core.loader import TypeRegistry
    registry = TypeRegistry()
    registry.load_builtins()
    print(f"  OK: TypeRegistry has {len(registry.types)} types")
except Exception as e:
    print(f"  FAILED: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Test 5: Validate messages
print("[5/5] Validating messages...")
try:
    from protocol_codegen.core.validator import ProtocolValidator
    validator = ProtocolValidator(registry)
    errors = validator.validate_messages(ALL_MESSAGES)
    if errors:
        print(f"  FAILED: {len(errors)} validation errors:")
        for error in errors:
            print(f"    - {error}")
        sys.exit(1)
    else:
        print(f"  OK: All {len(ALL_MESSAGES)} messages validated successfully")
except Exception as e:
    print(f"  FAILED: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print()
print("="*70)
print("SUCCESS: All tests passed!")
print("="*70)
