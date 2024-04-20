## Seamless V4 Utilities
(code-url: https://github.com/sislv4/sislv4utils)

Companion utility library for Seamless v4 architecture

**Install**
```
pip3 install sislv4utils
```

**Uninstall**
```
pip3 uninstall sislv4utils
```

## Version History

**v0.0.5**
+ MessageQueue constructor now accepts Config object instead of host, port etc
+ MqttcClient constructor now accepts Config object instead of host, port etc
+ ObjectStore constructor now accepts Config object instead of host, port etc
+ Service class and its derived classes have been modified accordingly

**v0.0.4**
+ Overall code improved. 
+ New abstruct classes like WebService, MQService, MqttService inherited from Service have been introduced
+ Config class is improved. Now loading standard s3 settings, MQ settings and MQTT settings is just a function call away
+ app.py have become very minimal. Service class start method now takes care of outer exception handling
+ Few defects in MqttClient has been resolved

**v0.0.3**
+ Fixed github [issue #1](https://github.com/sislv4/sislv4utils/issues/1)

**v0.0.2**
+ MQTT support added
+ Dependency on protobuf version is fixed to (== 3.20.3) from (>= 3.20.3)
+ Created basic content for this README.md

**v0.0.1**
+ Create Initial version
