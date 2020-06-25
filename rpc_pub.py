import paho.mqtt.client
from paho.mqtt.packettypes import PacketTypes

def callback(client, userdata, message):
    print(message.payload)

client = paho.mqtt.client.Client(userdata=None,
                                 protocol=paho.mqtt.client.MQTTv5,
                                 transport="tcp")
client.connect("localhost")
client.subscribe("hello_resp")
client.message_callback_add("hello_resp", callback)

client.loop_start()

props = paho.mqtt.client.Properties(PacketTypes.PUBLISH)
props.ResponseTopic = "hello_resp"
client.publish("hello", "James", properties=props)

while True:
    pass;
