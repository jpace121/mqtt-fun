import paho.mqtt.publish as publish

publish.single("logging", "logging", hostname="localhost")
