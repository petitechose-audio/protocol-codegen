"""
Output Paths Configuration

Defines where to generate the C++ and Java code.
"""

PLUGIN_PATHS = {
    "plugin_name": "sensor-network",
    "plugin_display_name": "Sensor Network Example",
    "output_cpp": {
        "base_path": "generated/cpp",
        "encoder": "generated/cpp/",
        "messageid": "generated/cpp/",
        "registry": "generated/cpp/",
        "structs": "generated/cpp/struct/",
        "constants": "generated/cpp/",
    },
    "output_java": {
        "base_path": "generated/java/com/example/sensor",
        "package": "com.example.sensor",
        "encoder": "generated/java/com/example/sensor/",
        "messageid": "generated/java/com/example/sensor/",
        "registry": "generated/java/com/example/sensor/",
        "structs": "generated/java/com/example/sensor/struct/",
        "constants": "generated/java/com/example/sensor/",
    },
    "options": {
        "cpp_namespace": "SensorProtocol",
        "java_package": "com.example.sensor",
        "generate_validation": True,
        "generate_debug": True,
    },
}
