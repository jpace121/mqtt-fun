import paho.mqtt.subscribe as subscribe

topics = ['#']

def call(client, userdata, message):
    print(message.payload)

subscribe.callback(call, '#', hostname='localhost')
