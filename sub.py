import paho.mqtt.client

class SubNode:
    def __init__(self):
        self._client = paho.mqtt.client.Client(userdata=self,
                                          protocol=paho.mqtt.client.MQTTv5,
                                          transport="tcp")
        self._client.connect("localhost")

        self._client.subscribe([("logging", paho.mqtt.client.SubscribeOptions(qos=1)),
                                ("hello", paho.mqtt.client.SubscribeOptions(qos=1))])
        self._client.message_callback_add("logging", self._callback)
        self._client.message_callback_add("hello", self._rpc_callback)
        self.a = 0

    def loop(self):
        self._client.loop_start()

    @staticmethod
    def _callback(client, userdata, message):
        userdata.a = userdata.a + 1
        print("{}".format(userdata.a))

    @staticmethod
    def _rpc_callback(client, userdata, message):
        print("Message from: {}".format(message.payload))
        userdata._client.publish(message.properties.ResponseTopic, "yo, {}".format(message.payload))

a = SubNode()
a.loop()
while True:
    pass;
