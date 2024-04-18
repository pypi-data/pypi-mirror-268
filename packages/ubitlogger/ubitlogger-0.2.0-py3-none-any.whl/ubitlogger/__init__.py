"""
"""

__author__ = 'p4irin'
__email__ = 'p4irin.github.io@gmail.com'
__version__ = '0.2.0'


from threading import Thread, Event
from signal import signal, SIGINT, SIGTERM
from time import sleep
from serial import Serial
from serial.tools.list_ports import comports


def _exit_gracefully(signum, frame):
    if signum in [2, 15]:
        if signum == 2:
            msg = "\nExited by CTRL-C\n"
        if signum == 15:
            msg = "Exited by SIGTERM\n"
        msg += "Cleaning up thread\n"
        _stop_event.set()
    else:
        msg = f"Received signal: {signum}"
    print(msg)
    print(f"frame: {frame}")
    exit(1)

signal(SIGINT, handler=_exit_gracefully)
signal(SIGTERM, handler=_exit_gracefully)

_stop_event = Event()


class NoUBitFound(Exception):
    pass


class UBitLogger(object):

    _product_id = 516
    _vendor_id = 3368

    def __init__(
            self, handler = None,
            baudrate: int = 115200,
            timeout: float = 0.1,
            debug: bool = False
            ) -> None:
        
        self._debug = debug
        self.handler = handler or self._default_handler
        self._baudrate = baudrate
        self._timeout = timeout
        self._serial_port = self._scan()

    def _default_handler(self, line:str):
        print(line)

    def _scan(self) -> Serial:
        ports = comports()
        if len(ports) > 0:
            for port in ports:
                try:
                    if (port.pid == self._product_id) and (port.vid == self._vendor_id):
                        if self._debug:
                            print(f"Found a micro:bit on: {port.device}")

                        connection = Serial(
                            port.device,
                            timeout=self._timeout,
                            baudrate=self._baudrate
                            )
                        return connection
                except AttributeError:
                    continue
        raise NoUBitFound
    
    def _listen(self):
        self._serial_port.reset_input_buffer()
        while not _stop_event.is_set():
            if self._serial_port.in_waiting > 0:
                line = self._serial_port.readline().decode('utf-8').strip()
                self.handler(line)
            sleep(2)

    def start(self):
        if self._debug:
            connection = self._serial_port
            print(f"Listening on port {connection.port}")
            print(f"Baudrate: {connection.baudrate}")
            print(f"Data bits: {connection.bytesize}")
            print(f"Stop bits: {connection.stopbits}")
            print(f"Parity: {connection.parity}")
            print(f"timeout: {connection.timeout}")

        thread = Thread(target=self._listen)
        thread.start()
        thread.join()
    
    def stop(self):
        _stop_event.set()