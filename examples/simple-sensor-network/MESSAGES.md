# Message Reference

Quick reference for all messages in the Sensor Network protocol.

## Message Summary

| Message ID | Name | Direction | Size | Complexity |
|------------|------|-----------|------|------------|
| 0x00 | SENSOR_READING_SINGLE | Device → Host | ~13 bytes | ⭐ Simple |
| 0x01 | SENSOR_READING_BATCH | Device → Host | ~120 bytes | ⭐⭐ Array |
| 0x02 | REQUEST_SENSOR_LIST | Host → Device | ~3 bytes | ⭐ Simple |
| 0x03 | SENSOR_LIST | Device → Host | ~650 bytes | ⭐⭐⭐ Nested Array |
| 0x04 | SENSOR_CONFIG_SET | Host → Device | ~15 bytes | ⭐⭐ Medium |
| 0x05 | SENSOR_CONFIG_GET | Host → Device | ~4 bytes | ⭐ Simple |
| 0x06 | SENSOR_ACTIVATE | Host → Device | ~4 bytes | ⭐ Simple |
| 0x07 | SENSOR_DEACTIVATE | Host → Device | ~4 bytes | ⭐ Simple |
| 0x08 | NETWORK_STATUS | Device → Host | ~50 bytes | ⭐⭐ Medium |
| 0x09 | REQUEST_NETWORK_STATUS | Host → Device | ~3 bytes | ⭐ Simple |

**Total:** 10 messages

## Message Details

### SENSOR_READING_SINGLE (0x00)
**Direction:** Device → Host
**Description:** Single sensor reading with timestamp

**Fields:**
- `sensorId` (UINT8) - Which sensor
- `value` (FLOAT32) - Reading value
- `timestamp` (UINT32) - Unix timestamp

**Size:** ~13 bytes (raw) → ~23 bytes (SysEx)

**Example:**
```cpp
SensorReadingSingleMessage msg;
msg.sensorId = 1;
msg.value = 23.5f;
msg.timestamp = 1234567890;
```

---

### SENSOR_READING_BATCH (0x01)
**Direction:** Device → Host
**Description:** Batch of sensor readings (up to 8)

**Fields:**
- `readings` (Array[8] of SensorReading) - Array of readings

**Composite:** Each reading contains:
- `sensorId` (UINT8)
- `value` (FLOAT32)
- `timestamp` (UINT32)
- `hasError` (BOOL)

**Size:** ~120 bytes (raw) → ~210 bytes (SysEx)

**Example:**
```cpp
SensorReadingBatchMessage msg;
msg.readings[0].sensorId = 1;
msg.readings[0].value = 23.5f;
msg.readings[0].timestamp = 1234567890;
msg.readings[0].hasError = false;
// ... up to msg.readings[7]
```

---

### REQUEST_SENSOR_LIST (0x02)
**Direction:** Host → Device
**Description:** Request list of all sensors

**Fields:** None

**Size:** ~3 bytes (SysEx framing only)

**Example:**
```cpp
RequestSensorListMessage msg;
// No fields to set
```

---

### SENSOR_LIST (0x03) ⭐ Most Complex
**Direction:** Device → Host
**Description:** Complete sensor list with info

**Fields:**
- `sensorCount` (UINT8) - Number of sensors
- `sensors` (Array[16] of SensorInfo) - Sensor information

**Composite:** Each SensorInfo contains:
- `sensorId` (UINT8)
- `sensorName` (STRING[32])
- `sensorType` (UINT8) - 0=temp, 1=humidity, 2=pressure
- `color` (UINT32) - RGB color (0xRRGGBB)
- `isActive` (BOOL)
- `batteryLevel` (UINT8) - 0-100%
- `updateInterval` (UINT16) - milliseconds

**Size:** ~650 bytes (raw) → ~1140 bytes (SysEx) ⚠️ **Large!**

**Example:**
```cpp
SensorListMessage msg;
msg.sensorCount = 3;

msg.sensors[0].sensorId = 1;
strcpy(msg.sensors[0].sensorName, "Temperature");
msg.sensors[0].sensorType = 0;
msg.sensors[0].color = 0xFF0000;  // Red
msg.sensors[0].isActive = true;
msg.sensors[0].batteryLevel = 85;
msg.sensors[0].updateInterval = 1000;
// ... etc
```

---

### SENSOR_CONFIG_SET (0x04)
**Direction:** Host → Device
**Description:** Configure sensor thresholds and interval

**Fields:**
- `sensorId` (UINT8)
- `updateInterval` (UINT16) - milliseconds
- `thresholdMin` (FLOAT32)
- `thresholdMax` (FLOAT32)

**Size:** ~15 bytes (raw) → ~27 bytes (SysEx)

---

### SENSOR_CONFIG_GET (0x05)
**Direction:** Host → Device
**Description:** Request sensor configuration

**Fields:**
- `sensorId` (UINT8)

**Size:** ~4 bytes (raw) → ~8 bytes (SysEx)

---

### SENSOR_ACTIVATE (0x06)
**Direction:** Host → Device
**Description:** Activate a sensor

**Fields:**
- `sensorId` (UINT8)

**Size:** ~4 bytes (raw) → ~8 bytes (SysEx)

---

### SENSOR_DEACTIVATE (0x07)
**Direction:** Host → Device
**Description:** Deactivate a sensor

**Fields:**
- `sensorId` (UINT8)

**Size:** ~4 bytes (raw) → ~8 bytes (SysEx)

---

### NETWORK_STATUS (0x08)
**Direction:** Device → Host
**Description:** Network status information

**Fields:**
- `networkId` (UINT16)
- `networkName` (STRING[32])
- `sensorCount` (UINT8)
- `activeSensorCount` (UINT8)
- `isOnline` (BOOL)
- `rssi` (INT8) - Signal strength in dBm

**Size:** ~50 bytes (raw) → ~88 bytes (SysEx)

---

### REQUEST_NETWORK_STATUS (0x09)
**Direction:** Host → Device
**Description:** Request network status

**Fields:** None

**Size:** ~3 bytes (SysEx framing only)

---

## Type Reference

### Primitive Types

| Type | Size | Range/Description |
|------|------|-------------------|
| BOOL | 1 byte | true/false |
| UINT8 | 1 byte | 0-255 |
| INT8 | 1 byte | -128 to 127 |
| UINT16 | 2 bytes | 0-65535 |
| UINT32 | 4 bytes | 0-4294967295 |
| FLOAT32 | 4 bytes | IEEE 754 single precision |
| STRING | Variable | Max 32 chars (configurable) |

### Composite Types

**SensorReading:**
- sensorId (UINT8)
- value (FLOAT32)
- timestamp (UINT32)
- hasError (BOOL)

**SensorInfo:**
- sensorId (UINT8)
- sensorName (STRING)
- sensorType (UINT8)
- color (UINT32)
- isActive (BOOL)
- batteryLevel (UINT8)
- updateInterval (UINT16)

---

## Size Budget Analysis

### SysEx Overhead Formula

```
SysEx Size ≈ Raw Size × 1.75 + 4 bytes (framing)
```

**Framing:**
- 0xF0 (Start)
- Manufacturer ID
- Device ID
- 7-bit encoded data (8 bits → 14 bits = 1.75x)
- 0xF7 (End)

### Message Size Breakdown

| Category | Count | Total Size (SysEx) |
|----------|-------|-------------------|
| Small (<10 bytes) | 5 | ~40 bytes |
| Medium (10-100 bytes) | 3 | ~200 bytes |
| Large (>100 bytes) | 2 | ~1350 bytes |

**Total protocol overhead:** ~1590 bytes

---

## Usage Patterns

### Pattern 1: Continuous Monitoring
```
Device sends SENSOR_READING_SINGLE every 1 second
Total bandwidth: ~23 bytes/sec per sensor
```

### Pattern 2: Batch Updates
```
Device sends SENSOR_READING_BATCH every 5 seconds
Total bandwidth: ~42 bytes/sec for 8 sensors
```

### Pattern 3: Discovery
```
Host: REQUEST_SENSOR_LIST
Device: SENSOR_LIST (once at startup)
```

### Pattern 4: Configuration
```
Host: SENSOR_CONFIG_SET
Device: (applies config, starts sending at new interval)
```

---

**Generated by:** Protocol CodeGen v1.0.0
**Last updated:** 2024-11-16
