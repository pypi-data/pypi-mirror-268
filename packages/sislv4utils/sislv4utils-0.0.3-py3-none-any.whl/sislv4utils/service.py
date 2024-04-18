import os
import sys
import getopt
import resource
import logging
import falcon
from abc import abstractmethod, ABCMeta
from wsgiref.simple_server import make_server

from sislv4utils.config import Config
from sislv4utils.message import MessageQueue

class Service(object, metaclass=ABCMeta):
    # region members

    _interactive = False
    _config: Config = None

    # endregion
    # region method

    def start(self) -> None:
        self.init_server()
        self.start_server()

    def init_server(self) -> None:
        # let us parse the configuration parameters
        # and check if weed to run in interactive mode
        opts, _ = getopt.getopt(sys.argv[1:], "i")
        for opt, _ in opts:
            if opt in ("-i"):
                Service._interactive = True

        # set appropriate mode i.e. interactive vs daemon
        self._set_mode()

    @abstractmethod
    def start_server(self) -> None:
        pass

    def start_server_ws(self, app: falcon.App) -> None:
        cf: Config = Service._config

        logging.info('serving on {0}:{1}...'.format(cf.apphost, cf.appport))

        # check if we are asked tor run on all interfaces
        # they will be marked as * or all in config file
        iface = cf.apphost
        if iface == '*' or iface == 'all':
            iface = ''

        # run falcon webserver
        with make_server(iface, cf.appport, app) as httpd:
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                return

    def start_server_qs(
        self,
        host: str,
        port: int,
        user: str,
        password: str,
        exchange: str,
        queue_name: str,
        binding: str,
        handler,
        func: str
    ) -> None:
        logging.info('listening on {0}:{1}...'.format(exchange, binding))

        # listen to a particuler queue with a given binding key
        with MessageQueue(host=host, port=port, username=user, password=password) as ch:
            ch.listen(exchange, queue_name, binding_key=binding, event_handler=handler, event_callback_func=func)

    def _set_mode(self) -> None:
        cf: Config = Service._config

        # if we are running on interactive mode
        # start logging and return from here
        if Service._interactive:
            return Service._config.start_logging(console=True)

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

    # endregion
