"""
Arduino in Junying's setup.

Sends out TTL pulses to NI-DAQ.
TTL pulses trigger acquisition and convey stimulus information.

"""

import logging
import time

import serial

from trigger_count.log import get_basic_logger

BAUD_RATE = 9600
PORT = "/dev/ttyACM0"
POSSIBLE_STIM_TRIGGERS = ["A", "B"]


class TtlArduino:
    """Class to handle serial communication with arduino."""
    def __init__(self, port: str = PORT, logger: logging.Logger | None = None) -> None:
        # params
        self.port = port
        self.logger = logger

        # go
        if self.logger is None:
            self.logger = get_basic_logger("arduino")
        self.serial_connection = serial.Serial(
            port=port,
            baudrate=BAUD_RATE,
        )
        self.logger.info(f"Serial connection established: {PORT}")
        time.sleep(1)

    def send_acquisition_trigger(self) -> None:
        self.serial_connection.write("T".encode())
        self.logger.info("Acquisition trigger sent.")

    def send_stim_trigger(self, code: str = "A") -> None:
        assert code in POSSIBLE_STIM_TRIGGERS
        self.serial_connection.write(code.encode())
        self.logger.info(f"Stim trigger sent: {code}")

    def confirm(self) -> None:
        reply = self.serial_connection.readline()
        reply = reply.decode().strip()
        assert reply == "X", f"{reply=}"
        self.logger.info(f"Received confirmation: {reply}")

    def close(self) -> None:
        self.serial_connection.close()
        self.logger.info(f"Serial connection closed: {PORT}")