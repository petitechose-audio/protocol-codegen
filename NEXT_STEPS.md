# Protocol CodeGen - Next Steps

## ✅ Phase 1 Complete!

**Repository:** `E:\projets\dev\petitechose-audio\protocol-codegen`  
**Commit:** `411f4e0` - Initial extraction from midi-studio  
**Status:** Files extracted, structure created, ready for refactoring

---

## 🎯 Immediate Next Steps (Phase 2)

### Step 1: Fix All Import Paths (CRITICAL)

All files currently have broken imports. Need to update:

```bash
# Find all files with old imports
cd "E:\projets\dev\petitechose-audio\protocol-codegen"
grep -r "from protocol\." src/ | wc -l
# Expected: Many files

# Replace pattern:
# OLD: from protocol.core import ...
# NEW: from protocol_codegen.core import ...
# OLD: from protocol.sysex import ...
# NEW: from protocol_codegen.methods.sysex import ...
# OLD: from protocol.generators.cpp import ...
# NEW: from protocol_codegen.generators.cpp import ...
```

**Files to update:** All 37 Python files

### Step 2: Create SysEx Generator Orchestrator

Create: `src/protocol_codegen/methods/sysex/generator.py`

This file should:
```python
def generate_sysex_protocol(messages_path, config_path, output_cpp, output_java, verbose):
    """Main orchestrator called by CLI"""
    # Load messages
    # Load config
    # Generate C++ code (if output_cpp specified)
    # Generate Java code (if output_java specified)
    # Print summary
```

### Step 3: Test Basic Functionality

```bash
# Install package in dev mode
cd "E:\projets\dev\petitechose-audio\protocol-codegen"
uv sync --dev

# Test CLI works
protocol-codegen --help
protocol-codegen list-methods
protocol-codegen list-generators

# Create test messages file
# Try to generate code
protocol-codegen generate --method sysex --messages ./test_messages.py --output-cpp ./test_out
```

### Step 4: Fix Runtime Errors

Debug any errors that occur:
- Import errors → fix paths
- Missing files → create them
- Logic errors → adapt from original code

---

## 📋 Detailed Refactoring Checklist

### Core Module (`src/protocol_codegen/core/`)
- [ ] `types.py` - Update imports
- [ ] `field.py` - Update imports
- [ ] `message.py` - Update imports
- [ ] `loader.py` - Update imports, make paths generic
- [ ] `importer.py` - Update imports, make paths generic
- [ ] `allocator.py` - Update imports
- [ ] `validator.py` - Update imports
- [ ] `stub_generator.py` - Update imports, fix output paths

### SysEx Method (`src/protocol_codegen/methods/sysex/`)
- [ ] `config.py` - Update imports
- [ ] `builtin_config.py` - Update imports
- [ ] `generator.py` - **CREATE THIS FILE** (orchestrator)

### C++ Generators (`src/protocol_codegen/generators/cpp/`)
- [ ] `encoder_generator.py` - Update imports
- [ ] `decoder_generator.py` - Update imports
- [ ] `messageid_generator.py` - Update imports
- [ ] `struct_generator.py` - Update imports
- [ ] `constants_generator.py` - Update imports
- [ ] `logger_generator.py` - Update imports
- [ ] `callbacks_generator.py` - Update imports
- [ ] `decoder_registry_generator.py` - Update imports
- [ ] `message_structure_generator.py` - Update imports

### Java Generators (`src/protocol_codegen/generators/java/`)
- [ ] Same 9 files as C++ (update imports)

### CLI & Package
- [ ] `cli.py` - Already correct (uses protocol_codegen.*)
- [ ] `__init__.py` - Already correct
- [ ] `__main__.py` - Already correct

---

## 🔧 Recommended Workflow

### Option A: Manual Refactoring
1. Open each file
2. Find/Replace old imports
3. Test incrementally

### Option B: Automated Refactoring (FASTER)
```bash
cd "E:\projets\dev\petitechose-audio\protocol-codegen"

# Replace all imports automatically
find src/ -name "*.py" -type f -exec sed -i 's/from protocol\./from protocol_codegen./g' {} +
find src/ -name "*.py" -type f -exec sed -i 's/from protocol import/from protocol_codegen import/g' {} +

# Verify changes
git diff src/
```

---

## 🧪 Testing Strategy

### 1. Create Simple Test Protocol
```python
# test_messages.py
from protocol_codegen.core import Message, Field, Flow, Type

LED_ON = Message(
    name="LED_ON",
    flow=Flow.HOST_TO_DEVICE,
    description="Turn LED on",
    fields=[Field('led_id', Type.UINT8)]
)

ALL_MESSAGES = [LED_ON]
```

### 2. Generate Code
```bash
protocol-codegen generate \
  --method sysex \
  --messages ./test_messages.py \
  --output-cpp ./test_cpp \
  --output-java ./test_java
```

### 3. Verify Output
- Check `test_cpp/` has Encoder.hpp, Decoder.hpp, etc.
- Check `test_java/` has Encoder.java, Decoder.java, etc.
- Verify C++ syntax (can it compile?)
- Verify Java syntax (can it compile?)

---

## 📊 Success Criteria

Before pushing to GitHub:
- [ ] All imports work (no ModuleNotFoundError)
- [ ] CLI responds to `--help`
- [ ] Can generate code for test protocol
- [ ] Generated C++ compiles with g++
- [ ] Generated Java compiles with javac
- [ ] No MIDI Studio hardcoded paths remain

---

## 🚀 After Phase 2

### Phase 3: Testing & Examples
- Write unit tests (pytest)
- Create example projects
- Test on Arduino, Teensy, Java

### Phase 4: Documentation
- Write tutorials
- Add API reference
- Create video demo

### Phase 5: Publication
- Publish to PyPI
- Announce on GitHub
- Share with community

---

## 💡 Tips

1. **Work incrementally** - Fix one module at a time
2. **Test often** - Run CLI after each change
3. **Commit frequently** - Small commits are easier to debug
4. **Ask for help** - Claude can help fix specific import errors
5. **Document issues** - Note any design decisions or breaking changes

---

## 📞 Support

Need help?
- Check `MIGRATION_STATUS.md` for current progress
- Check `STRUCTURE.md` for repository layout
- Ask Claude to fix specific import errors
- Create GitHub issues for bugs

---

**You've got this! Phase 1 (20%) complete, Phase 2 starting now! 🚀**
