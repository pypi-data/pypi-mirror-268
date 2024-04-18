import string
import random
import time
import paho.mqtt.client as mqttc

class MqttClient(object):
    #region members

    ERR_NOT_CONNECTED = 'not connected to any message queue'

    #endregion
    #region constructor / destructor

    def __init__(self, host: str, port: int, username: str, password: str, 
        randname: str = "", randsize: int = 6):

        self._host: str = host
        self._port: int = port

        self._conn = mqttc.Client(mqttc.CallbackAPIVersion.VERSION2,
            client_id= self.get_random_string(randname, randsize))
        self._conn.username_pw_set(username, password)
        self._connected = False

    def __enter__(self):
        # create a blocking connection
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        del exc_type, exc_value, exc_traceback
        self.close()

    #endregion
    #region methods

    def connect(self):
        if self._connected: return
        if self._conn.connect(self._host, self._port) == 0:
            self._connected = True

    def close(self):
        if not self._connected: return
        if self._conn.disconnect() == 0:
            self._connected = False

    def publish(self, topic: str, message: str) -> None:
        # check if we have a valid connection
        if not self._connected:
            raise Exception(MqttClient.ERR_NOT_CONNECTED)
        
        self._conn.loop_start()
        self._conn.publish(topic, message)
        time.sleep(1)
        self._conn.loop_stop()

    def listen(self, topic: str):
       # check if we have a valid connection
       if not self._connected:
            raise Exception(MqttClient.ERR_NOT_CONNECTED)

       self._conn.subscribe(topic)
       self._conn.loop_forever()

    def get_random_string(self, prefix: str = '', width: int = 6):
        random_string = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(width))
        return (prefix + random_string)
 
    #endregion
