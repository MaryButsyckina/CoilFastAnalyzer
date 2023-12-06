from Ethernet.MqttClient import MqttClient
from Files.FileManager import ConfigFile


if __name__ == '__main__':
    config = ConfigFile().open()
    mqtt_client_config = config['MqttClient']

    client = MqttClient(mqtt_client_config['broker'],
                        mqtt_client_config['port'],
                        mqtt_client_config['topic'],
                        mqtt_client_config['topic_pub'],
                        mqtt_client_config['client_id'])
    client.run()
