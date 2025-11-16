# Protocol CodeGen

**Generic bidirectional protocol code generator** - Generate type-safe protocol code (C++, Java, and more) from simple Python message definitions.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

---

## 🎯 What is Protocol CodeGen?

Protocol CodeGen is a **standalone code generation tool** for creating type-safe, bidirectional communication protocols. Define your messages once in Python, and generate complete encoder/decoder implementations for multiple languages.

**Perfect for:**
- 🎛️ Hardware ↔ Software communication (embedded devices, audio controllers, etc.)
- 🎮 Game engine plugins ↔ External tools
- 📱 IoT devices ↔ Mobile/Desktop apps
- 🎵 Audio plugins ↔ DAWs (Digital Audio Workstations)
- 🤖 Robotics control systems
- 🔌 Any project requiring structured bidirectional communication

---

## ✨ Features

### Protocol Methods
- ✅ **SysEx (MIDI System Exclusive)** - Binary protocol for MIDI devices
- 🔮 **OSC (Open Sound Control)** *(planned)*
- 🔮 **Custom Binary Protocols** *(planned)*
- 🔮 **JSON-RPC** *(planned)*

### Code Generators
- ✅ **C++** - For embedded systems, audio plugins, native applications
- ✅ **Java** - For desktop applications, Android, host extensions
- 🔮 **Rust** *(planned)*
- 🔮 **Python** *(planned)*
- 🔮 **TypeScript/JavaScript** *(planned)*

### Why Use Protocol CodeGen?
- ✅ **Type-safe** - Catch errors at compile time, not runtime
- ✅ **DRY** - Define messages once, generate code for all languages
- ✅ **Validated** - Strict validation prevents invalid protocols
- ✅ **Auto ID allocation** - Message IDs assigned automatically by direction
- ✅ **Zero boilerplate** - Focus on messages, not serialization code
- ✅ **Extensible** - Easy to add new protocol methods and generators

---

## 🚀 Quick Start

### Installation

```bash
# Using pip
pip install protocol-codegen

# Using uv (recommended)
uv add protocol-codegen
```

### Define Your Messages

Create a `messages.py` file with your protocol definition:

```python
from protocol_codegen.core import Message, Field, Flow, Type

# Define messages
SENSOR_READING = Message(
    name="SENSOR_READING",
    flow=Flow.DEVICE_TO_HOST,
    description="Temperature sensor reading",
    fields=[
        Field('sensor_id', Type.UINT8),
        Field('temperature', Type.INT16),  # Celsius * 100
        Field('timestamp', Type.UINT32),
    ]
)

SET_LED_COLOR = Message(
    name="SET_LED_COLOR",
    flow=Flow.HOST_TO_DEVICE,
    description="Set RGB LED color",
    fields=[
        Field('led_id', Type.UINT8),
        Field('red', Type.UINT8),
        Field('green', Type.UINT8),
        Field('blue', Type.UINT8),
    ]
)

ALL_MESSAGES = [
    SENSOR_READING,
    SET_LED_COLOR,
]
```

### Generate Code

```bash
protocol-codegen generate \
  --method sysex \
  --messages ./messages.py \
  --output-cpp ./src/protocol \
  --output-java ./src/main/java/protocol
```

### Use Generated Code

**C++ (Embedded side):**
```cpp
#include "protocol/Encoder.hpp"
#include "protocol/struct/SensorReadingMessage.hpp"

// Send sensor reading
SensorReadingMessage msg;
msg.sensor_id = 1;
msg.temperature = 2350;  // 23.50°C
msg.timestamp = millis();

uint8_t buffer[64];
size_t length = Protocol::Encoder::encode(msg, buffer);
Serial.write(buffer, length);
```

**Java (Host side):**
```java
import protocol.Decoder;
import protocol.struct.SensorReadingMessage;

// Receive sensor reading
byte[] data = midiInput.readSysEx();
SensorReadingMessage msg = Decoder.decodeSensorReading(data);

System.out.println("Sensor " + msg.sensorId +
                   ": " + (msg.temperature / 100.0) + "°C");
```

---

## 📚 Documentation

### Core Concepts

#### Message Definition
A message has:
- **name**: Unique identifier (SCREAMING_SNAKE_CASE)
- **flow**: Direction (DEVICE_TO_HOST, HOST_TO_DEVICE, BIDIRECTIONAL)
- **description**: Human-readable description
- **fields**: List of typed fields

#### Field Types
Built-in types:
- `UINT8`, `UINT16`, `UINT32` - Unsigned integers
- `INT8`, `INT16`, `INT32` - Signed integers
- `BOOL` - Boolean
- `FLOAT` - 32-bit float
- `STRING` - Variable-length string

Arrays:
```python
Field('values', Type.UINT16, array=8)  # Fixed-size array
```

#### Message Flow
- `DEVICE_TO_HOST` - Device sends to host (IDs: 0x00-0x3F)
- `HOST_TO_DEVICE` - Host sends to device (IDs: 0x40-0xBF)
- `BIDIRECTIONAL` - Both directions (IDs: 0xC0-0xFF)

### CLI Reference

```bash
# Generate code
protocol-codegen generate \
  --method sysex \
  --messages ./messages.py \
  --config ./protocol_config.py \
  --output-cpp ./cpp \
  --output-java ./java

# Validate messages
protocol-codegen validate \
  --method sysex \
  --messages ./messages.py

# List available methods and generators
protocol-codegen list-methods
protocol-codegen list-generators

# Show version
protocol-codegen --version
```

---

## 🎓 Examples

See the `examples/` directory for complete projects:

- **`sysex-arduino-python/`** - Arduino ↔ Python via SysEx
- **`sysex-teensy-java/`** - Teensy 4.1 ↔ Java (audio plugin use case)
- **`custom-protocol/`** - Custom binary protocol example

---

## 🔧 Development

### Setup Development Environment

```bash
git clone https://github.com/petitechose-audio/protocol-codegen.git
cd protocol-codegen

# Install with dev dependencies
uv sync --dev
# or
pip install -e ".[dev]"
```

### Run Tests

```bash
pytest
```

### Code Quality

```bash
# Format
black src/ tests/

# Lint
ruff check src/ tests/

# Type check
mypy src/
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Add new protocol methods** (OSC, custom protocols)
2. **Add new code generators** (Rust, Python, C#, TypeScript)
3. **Improve existing generators** (optimizations, features)
4. **Write documentation and examples**
5. **Report bugs and suggest features**

See `CONTRIBUTING.md` for guidelines.

---

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### Why MIT?

Protocol CodeGen is a **development tool** designed to be used by the widest possible audience. The MIT license allows:
- ✅ Commercial use
- ✅ Modification
- ✅ Distribution
- ✅ Private use

Projects using Protocol CodeGen (like MIDI Studio) can use any license they choose.

---

## 🌟 Projects Using Protocol CodeGen

- **[MIDI Studio](https://github.com/petitechose-midi-studio)** - MIDI controller with bidirectional SysEx protocol (Teensy 4.1 ↔ Bitwig Studio)
- *Your project here!* - Open an issue to be listed

---

## 🙏 Acknowledgments

- Inspired by Protocol Buffers, Cap'n Proto, and FlatBuffers
- Built for the embedded audio and MIDI community
- Special thanks to the MIDI Studio beta testers

---

## 📬 Contact

- **Author**: petitechose.audio
- **GitHub**: [@petitechose-audio](https://github.com/petitechose-audio)
- **Issues**: [GitHub Issues](https://github.com/petitechose-audio/protocol-codegen/issues)

---

**Made with ❤️ for embedded developers, audio engineers, and hardware hackers**
