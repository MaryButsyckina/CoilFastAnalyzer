from paho.mqtt import client as mqtt_client
import json


class MqttClient:
    def __init__(self, broker, port, topic, topic_pub, client_id):
        self.broker = broker
        self.port = port
        self.topic = topic
        self.topic_pub = topic_pub
        self.client_id = client_id
        self.client = None

    def connect(self):
        def on_connect(client, userdata, flags, rc):
            if not rc:
                print("Connected to server")
            else:
                print('Connection failed')
        self.client = mqtt_client.Client(self.client_id)
        self.client.on_connect = on_connect
        self.client.connect(self.broker, self.port)
        return self.client

    def subscribe(self):
        def on_message(client, userdata, msg):
            data = json.loads(str(msg.payload.decode('utf-8')))
        self.client.subscribe(self.topic)
        self.client.on_message = on_message

    def run(self):
        self.connect()
        self.subscribe()
        self.client.loop_forever()
