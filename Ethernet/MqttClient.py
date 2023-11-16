from paho.mqtt import client as mqtt_client


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
            pass
        pass

    def subscribe(self):
        def on_message(client, userdata, msg):
            pass
        pass

    def run(self):
        pass
