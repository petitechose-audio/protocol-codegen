# Protocol CodeGen - Repository Structure

## Overview

This is a standalone Python package for generating type-safe bidirectional protocol code.

```
protocol-codegen/
├── src/protocol_codegen/          # Main package
│   ├── __init__.py                # Package initialization
│   ├── __main__.py                # CLI entry point (python -m protocol_codegen)
│   ├── cli.py                     # Click-based CLI
│   │
│   ├── core/                      # Core type system & validation
│   │   ├── __init__.py
│   │   ├── types.py               # Builtin type definitions (uint8, bool, etc.)
│   │   ├── field.py               # Field system & Flow enum
│   │   ├── message.py             # Message class
│   │   ├── loader.py              # TypeRegistry for loading types
│   │   ├── importer.py            # Dynamic message importer
│   │   ├── allocator.py           # MessageID allocation
│   │   ├── validator.py           # Protocol validation
│   │   └── stub_generator.py      # Type stub generator for IDE support
│   │
│   ├── methods/                   # Protocol method implementations
│   │   ├── __init__.py
│   │   └── sysex/                 # SysEx (MIDI System Exclusive)
│   │       ├── __init__.py
│   │       ├── config.py          # SysEx configuration
│   │       └── builtin_config.py  # Default SysEx config
│   │
│   ├── generators/                # Code generators
│   │   ├── __init__.py
│   │   ├── cpp/                   # C++ code generator
│   │   │   ├── __init__.py
│   │   │   ├── encoder_generator.py
│   │   │   ├── decoder_generator.py
│   │   │   ├── messageid_generator.py
│   │   │   ├── struct_generator.py
│   │   │   ├── constants_generator.py
│   │   │   ├── logger_generator.py
│   │   │   ├── callbacks_generator.py
│   │   │   ├── decoder_registry_generator.py
│   │   │   └── message_structure_generator.py
│   │   │
│   │   └── java/                  # Java code generator
│   │       ├── __init__.py
│   │       ├── encoder_generator.py
│   │       ├── decoder_generator.py
│   │       ├── messageid_generator.py
│   │       ├── struct_generator.py
│   │       ├── constants_generator.py
│   │       ├── logger_generator.py
│   │       ├── callbacks_generator.py
│   │       ├── decoder_registry_generator.py
│   │       └── message_structure_generator.py
│   │
│   └── templates/                 # Jinja2 templates (future)
│       ├── cpp/
│       └── java/
│
├── tests/                         # Unit tests
│   ├── test_core.py
│   ├── test_generators.py
│   └── fixtures/
│
├── examples/                      # Example projects
│   ├── sysex-arduino-python/
│   ├── sysex-teensy-java/
│   └── custom-protocol/
│
├── docs/                          # Documentation
│   ├── getting-started.md
│   ├── message-definition.md
│   ├── type-system.md
│   └── extending.md
│
├── pyproject.toml                 # Python package configuration
├── README.md                      # Main documentation
├── LICENSE                        # MIT License
├── .gitignore                     # Git ignore rules
└── STRUCTURE.md                   # This file
```

## Key Files

### Package Configuration
- `pyproject.toml` - Modern Python packaging with dependencies
- `src/protocol_codegen/__init__.py` - Public API exports
- `src/protocol_codegen/__main__.py` - CLI entry point

### Core System
- `core/types.py` - Builtin primitive types (uint8, bool, float, etc.)
- `core/field.py` - Field composition system & message flow
- `core/message.py` - Message definition class
- `core/validator.py` - Strict validation (types, circular deps, etc.)

### Code Generators
- `generators/cpp/` - C++ code generation (Teensy, Arduino, native apps)
- `generators/java/` - Java code generation (desktop, Android, extensions)
- Future: `generators/rust/`, `generators/python/`, etc.

### Protocol Methods
- `methods/sysex/` - MIDI System Exclusive implementation
- Future: `methods/osc/`, `methods/custom/`, etc.

## Installation

```bash
# From source (development)
cd protocol-codegen
uv sync --dev

# From PyPI (when published)
pip install protocol-codegen
```

## Usage

```bash
# CLI
protocol-codegen generate --method sysex --messages ./messages.py --output-cpp ./cpp

# Python API
from protocol_codegen.core import Message, Field, Flow, Type
```

## Development Workflow

1. Make changes to code
2. Run tests: `pytest`
3. Format code: `black src/ tests/`
4. Lint: `ruff check src/ tests/`
5. Type check: `mypy src/`
6. Commit changes

## Migration from MIDI Studio

This package was extracted from the MIDI Studio project to be a standalone tool.

Original location in MIDI Studio:
- `resource/code/py/protocol/` → `src/protocol_codegen/core/`
- `resource/code/py/protocol/sysex/` → `src/protocol_codegen/methods/sysex/`
- `resource/code/py/protocol/generators/` → `src/protocol_codegen/generators/`

The code has been refactored to be generic and reusable by any project.
