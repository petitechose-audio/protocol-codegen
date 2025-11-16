#!/usr/bin/env python3
import sys
from pathlib import Path

# Add to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

print("Quick generation test - checking if imports work")
print("="*70)

# Import core
from protocol_codegen.core.types import BUILTIN_TYPES
from protocol_codegen.core.loader import TypeRegistry

# Create registry
registry = TypeRegistry()
registry.load_builtins()

print(f"TypeRegistry loaded: {len(registry.types)} types")
for name in list(registry.types.keys())[:5]:
    print(f"  - {name}")

print("\nSUCCESS - Core imports working!")
print("Next step: adapt generator to work with example")
