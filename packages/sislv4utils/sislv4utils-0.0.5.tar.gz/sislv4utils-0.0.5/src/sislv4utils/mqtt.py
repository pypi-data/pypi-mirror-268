import time
import paho.mqtt.client as mqttc
from sislv4utils.config import Config

class MqttClient(object):
    #region members

    ERR_NOT_CONNECTED = 'Not connected to any broker'

    #endregion
    
    #region methods

    def __init__(self, cf: Config, name: str):

        self._host: str = cf.mqtt_host
        self._port: int = cf.mqtt_port
        self._conn: mqttc.Client = mqttc.Client(mqttc.CallbackAPIVersion.VERSION2, client_id= name)
        self._conn.username_pw_set(cf.appuser, cf.apppass)
        self._connected = False

    def __enter__(self):
        # create a blocking connection
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        del exc_type, exc_value, exc_traceback
        self.close()

    # connect to the broker
    def connect(self) -> None:
        if not self._connected and self._conn.connect(host= self._host, port= self._port) == 0:
            self._connected = True

    # disconnect from broker
    def close(self) -> None:
        if self._connected and self._conn.disconnect()== 0:            
            self._connected = False

    # publish to the nroker
    def publish(self, topic: str, message: str) -> None:
        if not self._connected:
            raise Exception(MqttClient.ERR_NOT_CONNECTED)
                
        self._conn.loop_start()
        self._conn.publish(topic, message)
        time.sleep(1)
        self._conn.loop_stop()

    # listens on a topic
    def listen(self, topic: str, event_handler: callable, event_callback_func: str) -> None:
        if not self._connected:
            raise Exception(MqttClient.ERR_NOT_CONNECTED)

        self._conn.on_message = lambda client, userdata, message: getattr(
            event_handler, event_callback_func)(client, userdata, message)

        try:
            self._conn.subscribe(topic)
            self._conn.loop_forever()
            
        except KeyboardInterrupt:
            pass
 
    #endregion
