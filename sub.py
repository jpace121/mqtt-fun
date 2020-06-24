import paho.mqtt.client

class SubNode:
    def __init__(self):
        self._client = paho.mqtt.client.Client(userdata=self,
                                          protocol=paho.mqtt.client.MQTTv5,
                                          transport="tcp")
        self._client.connect("localhost")

        self._client.subscribe("logging")
        self._client.message_callback_add("logging", self._callback)
        self.a = 0

    def loop(self):
        self._client.loop_forever()

    @staticmethod
    def _callback(client, userdata, message):
        print("Got one")

a = SubNode()
a.loop()
