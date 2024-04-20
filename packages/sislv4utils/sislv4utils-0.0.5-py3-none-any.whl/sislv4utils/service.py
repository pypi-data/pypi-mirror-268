import os
import sys
import getopt
import resource
import logging
import falcon
import random
import string
from abc import abstractmethod, ABCMeta
from wsgiref.simple_server import make_server

from sislv4utils.config import Config
from sislv4utils.message import MessageQueue
from sislv4utils.mqtt import MqttClient

class Service(object, metaclass=ABCMeta):
    # region members

    _interactive = False
    _config: Config = None

    ERR_UNKNOWN_ERRORMSG = 'Exception caught {0} => ( {1} )'

    # endregion
    
    # region methods

    # starts the service
    def start(self) -> None:
        try:
            # let us parse the configuration parameters
            # and check if weed to run in interactive mode
            opts, _ = getopt.getopt(sys.argv[1:], "i")
            for opt, _ in opts:
                if opt in ("-i"):
                    Service._interactive = True

            # set appropriate mode i.e. interactive vs daemon
            self._set_mode()
            self.start_server()

            sys.exit(0)
    
        except getopt.GetoptError as err:
            print(str(err))
            sys.exit(1)

        except Exception as err:
            logging.error(str(err))
            sys.exit(1)

    # a pure virtual method that will be implemented 
    # in subsequent derived classes
    @abstractmethod
    def start_server(self) -> None:
        pass

    # sets the running mode (i.e. interactive vs daemon)
    def _set_mode(self) -> None:
        cf: Config = Service._config

        # if we are running on interactive mode
        # start logging and return from here
        if Service._interactive:
            return cf.start_logging(console=True)

        # fork accordingly
        if os.fork() != 0:
            sys.exit(0)
        os.setsid()
        if os.fork() != 0:
            sys.exit(0)

        # close all open files and streams
        maxfd = resource.getrlimit(resource.RLIMIT_NOFILE)[1]
        if maxfd == resource.RLIM_INFINITY:
            maxfd = 1024
        for fd in range(0, maxfd):
            try:
                os.close(fd)
            except OSError:
                pass

        # duplicate stdout & stdin
        os.open(os.devnull, os.O_RDWR)
        os.dup2(0, 1)
        os.dup2(0, 2)

        # start logging in the logfile
        return cf.start_logging(console=False)
    
    # generates a random string
    def get_random_string(self, prefix: str = '', width: int = 6) -> str:
        random_string = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(width))
        return (prefix + random_string)

    # endregion

class MQService(Service, metaclass=ABCMeta):
    # region methods
    def __init__(self, name: str = ''):
        self._name = self.get_random_string(
            "mqservice-", 8) if not name else name

    # starts the service and listens for incoming messages
    def start_server(self) -> None:
        cf: Config = Service._config

        # listen to a particuler queue with a given binding key
        logging.info('listening on {0}:{1}...'.format(cf.mq_binding_exchange, cf.mq_binding_key))
        with MessageQueue(cf=cf) as ch:
            ch.listen(exchange_name=cf.mq_binding_exchange, queue_name=self._name, 
                binding_key=cf.mq_binding_key, event_handler=self, event_callback_func='_callback_func_')

    # callback method: called when we received a message
    def _callback_func_(self, ch, method, properties, body, binding_key):
        del ch, method, properties, binding_key
        try:self.process(body)
        except Exception as e:
            logging.error(Service.ERR_UNKNOWN_ERRORMSG.format("_callback_func_", str(e)))

    # a pure virtual method that will be implemented 
    # in subsequent derived classes
    @abstractmethod
    def process(self, message: str) -> None:
        pass

    #endregion

class WebService(Service, metaclass=ABCMeta):
    #region methods
    def __init__(self, name: str = ''):
        self._name = self.get_random_string(
            "webservice-", 8) if not name else name
    
    # starts the service and listens for incoming requests
    def start_server(self) -> None:
        cf: Config = Service._config

        # check if we are asked tor run on all interfaces
        # they will be marked as * or all in config file
        iface = cf.apphost
        if iface == '*' or iface == 'all':
            iface = ''

        # add your routes here
        self._app= falcon.App()
        self._app.add_sink(self._callback_func_, '/')

        # run falcon webserver
        logging.info('serving on {0}:{1}...'.format(cf.apphost, cf.appport))
        with make_server(iface, cf.appport, self._app) as httpd:
            try: httpd.serve_forever()
            except KeyboardInterrupt: return

    # callback method: called when we receive a request
    def _callback_func_(self, req: falcon.Request, resp: falcon.Response) -> None:
        try:
            resp.content_type = falcon.MEDIA_TEXT
            self.process(req, resp)

        # catch all exceptions
        except Exception as e:
            resp.status, resp.text = (falcon.HTTP_500,
                Service.ERR_UNKNOWN_ERRORMSG.format('_callback_func_', str(e)))
    
    # a pure virtual method that will be implemented 
    # in subsequent derived classes
    @abstractmethod
    def process(self, req: falcon.Request, resp: falcon.Response) -> None:
        pass

    #endregion

class MQTTService(Service, metaclass=ABCMeta):
    #region methods
    def __init__(self, name: str = ''):
        self._name = self.get_random_string(
            "mqttservice-", 8) if not name else name

    # starts the service and listens for incoming messages
    def start_server(self) -> None:
        cf: Config = Service._config

        # listen for a particuler topic
        with MqttClient(cf=cf, name=self._name) as channel:
            channel.listen(cf.mqtt_topic, self, '_callback_func_')

    # callback method: called when we received a message
    def _callback_func_(self, client, userdata, message) -> None:
        del client, userdata
        self.process(message.payload)

    # a pure virtual method that will be implemented 
    # in subsequent derived classes
    @abstractmethod
    def process(self, payload: str) -> None:
        pass

    #endregion