cmake_minimum_required(VERSION 3.5)
project("mqtt-cpp-examples"
    VERSION "0.0.0"
    LANGUAGES CXX
)

find_package(PahoMqttCpp REQUIRED)
find_package(Threads REQUIRED)

add_executable(pub src/pub.cpp)
target_link_libraries(pub PRIVATE PahoMqttCpp::paho-mqttpp3)

add_executable(sub src/sub.cpp)
target_link_libraries(sub PRIVATE PahoMqttCpp::paho-mqttpp3)
