# Simple Sensor Network - Protocol CodeGen Example

This example demonstrates how to define a complete protocol with **nested/composite types** for a sensor network application.

## 📁 Structure

```
simple-sensor-network/
├── field/                      # Field definitions (types)
│   ├── color.py               # Simple: RGB color field
│   ├── sensor.py              # Complex: Sensor fields + composites
│   └── network.py             # Simple: Network status fields
│
├── message/                    # Message definitions
│   ├── sensor.py              # Sensor-related messages
│   ├── network.py             # Network-related messages
│   └── __init__.py            # ALL_MESSAGES list
│
├── protocol_config.py         # SysEx configuration
├── plugin_paths.py            # Output paths configuration
└── README.md                  # This file
```

## 🎯 What This Example Demonstrates

### 1. **Primitive Fields** (`field/color.py`, `field/network.py`)
Simple single-value fields:
```python
color_rgb = PrimitiveField('color', type_name=Type.UINT32)
sensor_id = PrimitiveField('sensorId', type_name=Type.UINT8)
sensor_value = PrimitiveField('value', type_name=Type.FLOAT32)
```

### 2. **Composite Fields** (`field/sensor.py`)
Grouped fields that form a structure:
```python
# SensorReading: 4 fields grouped together
sensor_reading = [
    sensor_id,          # uint8
    sensor_value,       # float32
    sensor_timestamp,   # uint32
    sensor_is_error     # bool
]
```

### 3. **Composite Field Arrays** (`field/sensor.py`)
Arrays of composite structures:
```python
# Array of up to 8 sensor readings
sensor_readings_array = CompositeField(
    'readings',
    fields=sensor_reading,  # The composite structure
    array=8                 # Max 8 elements
)
```

### 4. **Nested Composites** (`field/sensor.py`)
Composites that reference other composites:
```python
sensor_info = [
    sensor_id,
    sensor_name,
    sensor_type,
    sensor_color,       # ← References color_rgb (from color.py)
    sensor_is_active,
    sensor_battery_level
]
```

### 5. **Simple Messages** (`message/sensor.py`)
Messages using primitive fields:
```python
SENSOR_READING_SINGLE = Message(
    description='Single sensor reading',
    fields=[
        sensor_id,       # uint8
        sensor_value,    # float32
        sensor_timestamp # uint32
    ]
)
```

### 6. **Complex Messages** (`message/sensor.py`)
Messages using composite field arrays:
```python
SENSOR_LIST = Message(
    description='List of all sensors',
    fields=[
        sensor_count,       # uint8 - How many sensors
        sensor_info_array   # Array[16] of SensorInfo structs
    ]
)
```

## 🔧 How to Generate Code

**Note:** This is a dry-run example - the protocol generator needs to be functional first (Phase 2).

Once Phase 2 is complete, you would run:

```bash
# From repository root
protocol-codegen generate \
  --method sysex \
  --messages examples/simple-sensor-network/message/__init__.py \
  --config examples/simple-sensor-network/protocol_config.py \
  --output-cpp examples/simple-sensor-network/generated/cpp \
  --output-java examples/simple-sensor-network/generated/java
```

## 📊 Generated Code Examples

### C++ Usage (Embedded - Arduino/Teensy)

**Simple message:**
```cpp
#include "SensorProtocol/Encoder.hpp"
#include "SensorProtocol/struct/SensorReadingSingleMessage.hpp"

// Send single sensor reading
SensorReadingSingleMessage msg;
msg.sensorId = 1;
msg.value = 23.5f;
msg.timestamp = millis();

uint8_t buffer[64];
size_t len = SensorProtocol::Encoder::encode(msg, buffer);
Serial.write(buffer, len);
```

**Complex message with nested arrays:**
```cpp
#include "SensorProtocol/struct/SensorListMessage.hpp"

// Send list of sensors
SensorListMessage msg;
msg.sensorCount = 3;

// Fill array of sensor info
msg.sensors[0].sensorId = 1;
msg.sensors[0].sensorName = "Temperature";
msg.sensors[0].sensorType = 0;
msg.sensors[0].color = 0xFF0000;  // Red
msg.sensors[0].isActive = true;
msg.sensors[0].batteryLevel = 85;
msg.sensors[0].updateInterval = 1000;

msg.sensors[1].sensorId = 2;
msg.sensors[1].sensorName = "Humidity";
// ... etc

uint8_t buffer[512];
size_t len = SensorProtocol::Encoder::encode(msg, buffer);
Serial.write(buffer, len);
```

### Java Usage (Host - Desktop/Android)

**Decode simple message:**
```java
import com.example.sensor.Decoder;
import com.example.sensor.struct.SensorReadingSingleMessage;

// Receive sensor reading
byte[] sysex = midiInput.readSysEx();
SensorReadingSingleMessage msg = Decoder.decodeSensorReadingSingle(sysex);

System.out.println("Sensor " + msg.sensorId +
                   ": " + msg.value +
                   " at " + msg.timestamp);
```

**Decode complex message with arrays:**
```java
import com.example.sensor.struct.SensorListMessage;

// Receive sensor list
byte[] sysex = midiInput.readSysEx();
SensorListMessage msg = Decoder.decodeSensorList(sysex);

System.out.println("Received " + msg.sensorCount + " sensors:");
for (int i = 0; i < msg.sensorCount; i++) {
    var sensor = msg.sensors[i];
    System.out.println("  - " + sensor.sensorName +
                       " (ID: " + sensor.sensorId + ")" +
                       " Battery: " + sensor.batteryLevel + "%");
}
```

## 🎓 Learning Points

### Type Composition Hierarchy

```
Level 1: Primitive Fields
    ↓
Level 2: Composite Fields (groups of primitives)
    ↓
Level 3: Composite Field Arrays (arrays of composites)
    ↓
Level 4: Messages (using primitives, composites, or arrays)
```

### Example Hierarchy in This Project

```
color_rgb (PrimitiveField - UINT32)
    ↓ used in
sensor_info (Composite - 7 fields including color_rgb)
    ↓ used in
sensor_info_array (CompositeField array - 16 elements)
    ↓ used in
SENSOR_LIST (Message - includes sensor_info_array)
```

### Memory Considerations

**Small message (SENSOR_READING_SINGLE):**
- sensor_id: 1 byte
- sensor_value: 4 bytes (float32)
- sensor_timestamp: 4 bytes
- **Total:** ~9 bytes (+ SysEx framing)

**Large message (SENSOR_LIST with 16 sensors):**
- sensor_count: 1 byte
- sensor_info_array: 16 sensors × ~40 bytes = ~640 bytes
- **Total:** ~641 bytes (+ SysEx framing)

**SysEx overhead:**
- Start byte: 1 byte (0xF0)
- Manufacturer ID: 1 byte
- Device ID: 1 byte
- 7-bit encoding: 8→14 bits per byte (~75% overhead)
- End byte: 1 byte (0xF7)

**Example:** 641 bytes → ~1121 bytes SysEx (within 512 byte limit needs adjustment!)

## ⚠️ Design Considerations

1. **Keep arrays small** - SysEx has size limits (~512 bytes typical)
2. **Use batch messages wisely** - Sending 16 sensors at once might be too much
3. **Consider chunking** - For large datasets, use multiple smaller messages
4. **String lengths** - Limit strings to avoid size explosion (max 32 chars here)

## 📝 Message Flow Examples

### Scenario 1: Sensor Discovery
```
Host → Device: REQUEST_SENSOR_LIST (empty)
Device → Host: SENSOR_LIST (sensor_count=3, sensors[0..2] filled)
```

### Scenario 2: Continuous Monitoring
```
Device → Host: SENSOR_READING_SINGLE (sensor 1)
Device → Host: SENSOR_READING_SINGLE (sensor 2)
Device → Host: SENSOR_READING_SINGLE (sensor 3)
... every 1000ms
```

### Scenario 3: Batch Update
```
Device → Host: SENSOR_READING_BATCH (readings[0..7] = 8 sensors)
... every 5000ms (less frequent, more data)
```

### Scenario 4: Configuration
```
Host → Device: SENSOR_CONFIG_SET (id=1, interval=500, thresholds)
Device → Host: SENSOR_READING_SINGLE (sensor 1 now updates at 500ms)
```

## 🚀 Next Steps

After Phase 2 is complete, this example can be used to:

1. **Test the generator** - Verify code generation works
2. **Validate composites** - Ensure nested types work correctly
3. **Check memory usage** - Profile generated C++ code
4. **Demonstrate features** - Show users how to structure protocols

---

**Status:** 📋 Example ready, waiting for Phase 2 (generator refactoring)
