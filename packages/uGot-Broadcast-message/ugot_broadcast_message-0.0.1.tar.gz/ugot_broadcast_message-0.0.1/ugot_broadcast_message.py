import socket
from io import BytesIO
from typing import Optional
import time
import threading

from ugot_broadcast_message_pb2 import broadcast_message_header, broadcast_message_payload

DEFAULT_CHANNEL_ID = 0
DEFAULT_BIND_HOST = '0.0.0.0'
DEFAULT_BROADCAST_ADDRESS = '255.255.255.255'

HEADER_INDICATE = 0xDB
BASE_CHANNEL_PORT = 25880


class ugot_broadcast_channel:

    def __init__(self, bind_host: Optional[str] = None, channel: int = 0):
        """initialization udp socket

        :param bind_host: bind network interface. Default: All available interfaces
        :param channel: communication channel. Range: [0~99]. Default: 0
        """
        self.bind_host = bind_host
        self.channel = channel
        self.callback = None
        self.enable = False

        self.recv_sock = None

    def __del__(self):
        self.__release_udp__()

    def set_channel(self, channel: int):
        if channel > 99 or channel < 0:
            return
        self.channel = channel
        self.__init_udp__()

    def set_enable(self, enable: bool):
        self.enable = enable
        if enable:
            self.__init_udp__()
        else:
            self.__release_udp__()

    def set_message_received_callback(self, callback):
        self.callback = callback

    def __init_udp__(self):
        if not self.enable:
            return
        self.__release_udp__()
        time.sleep(1)
        self.recv_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.recv_sock.bind((DEFAULT_BIND_HOST if self.bind_host is None else self.bind_host, self.get_port()))

        def receive_loop():
            while self.enable:
                try:
                    valid, message_content = self.__receive_message_impl__()
                    if self.callback is not None:
                        self.callback(message_content)
                except:
                    pass

        threading.Thread(target=receive_loop, daemon=True).start()

    def __release_udp__(self):
        if self.recv_sock is not None:
            self.recv_sock.close()

    def get_port(self):
        return BASE_CHANNEL_PORT + self.channel

    def __crc_sum__(self, data, offset=0, length=-1):
        if length < 0:
            length = len(data)

        crc = 0
        for i in range(length):
            crc ^= data[i + offset]
            for j in range(8):
                if crc & 0x80:
                    crc = crc << 1 ^ 0x07
                else:
                    crc = crc << 1
        return (crc ^ 0x55) & 0xFF

    def __receive_message_impl__(self):
        data, address = self.recv_sock.recvfrom(4096)

        data_size = len(data)

        if data_size < 3:
          return False, None

        if data[0] != HEADER_INDICATE:
          return False, None

        header_size = data[1]

        if data_size < 3 + header_size:
          return False, None

        header_bytes = data[2: 2 + header_size]
        if self.__crc_sum__(header_bytes) != data[2 + header_size]:
          return False, None

        header = broadcast_message_header()
        header.ParseFromString(header_bytes)

        if header.attr != broadcast_message_header.PUSH or header.dev != 2 or header.cmd != 2700:
          return False, None

        payload_size = header.dataLen

        if data_size < 4 + header_size + payload_size:
            return False, None

        payload_bytes = data[3 + header_size: 3 + header_size + payload_size]
        if self.__crc_sum__(payload_bytes) != data[3 + header_size + payload_size]:
            return False, None

        payload = broadcast_message_payload()
        payload.ParseFromString(payload_bytes)

        return True, payload.value

    def send_broadcast_message(self, message_value: str):
        self.__send_broadcast_message_impl__(message_value)

    def send_message_to(self, message_value: str, address: Optional[str]):
        self.__send_broadcast_message_impl__(message_value, address)

    def __send_broadcast_message_impl__(self, message_value: str, address: Optional[str] = None):
        """Send communication message
        :param message_value: message content
        :param address: target address. Default: None, broadcast to 255.255.255.255
        """
        if not self.enable:
            return

        payload = broadcast_message_payload()
        payload.name = "BMSG"
        payload.value = message_value[:19]  # Truncate for max 20 characters
        payload_bytes = payload.SerializeToString()

        header = broadcast_message_header()
        header.dev = 2
        header.cmd = 2700
        header.attr = broadcast_message_header.PUSH
        header.dataLen = len(payload_bytes)
        header_bytes = header.SerializeToString()

        message = BytesIO()
        message.write(bytes([HEADER_INDICATE]))
        message.write(bytes([len(header_bytes)]))
        message.write(header_bytes)
        message.write(bytes([self.__crc_sum__(header_bytes)]))
        message.write(payload_bytes)
        message.write(bytes([self.__crc_sum__(payload_bytes)]))
        message_bytes = message.getvalue()

        if self.bind_host is None:
            interfaces = socket.getaddrinfo(host=socket.gethostname(), port=None, family=socket.AF_INET)
            broadcast_interfaces = set([ip[-1][0] for ip in interfaces])
        else:
            broadcast_interfaces = [self.bind_host]

        # Remove loopback interface
        if '127.0.0.1' in broadcast_interfaces:
            broadcast_interfaces.remove('127.0.0.1')

        broadcast_address = (
          DEFAULT_BROADCAST_ADDRESS if address is None else address,
          self.get_port()
        )

        for interface in broadcast_interfaces:
            try:
                # Broadcast for each network interface
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
                sock.bind((interface, 0))
                sock.sendto(message_bytes, broadcast_address)
                sock.close()
            except:
                pass


if __name__ == '__main__':
    channel = ugot_broadcast_channel()

    # Optional set communication channel, default is 0
    # channel.set_channel(0)

    # Enable broadcast function, default is off
    channel.set_enable(True)

    # Set message received callback #1: use lambda
    channel.set_message_received_callback(lambda message_content: print(message_content))

    # Set message received callback #2: use regular function
    def message_received_handler(message_content: str):
        print(message_content)

    channel.set_message_received_callback(message_received_handler)

    # Set message received callback #3: use annotation
    @channel.set_message_received_callback
    def message_received_handler(message_content: str):
        print(message_content)

    # Send broadcast message to current channel
    channel.send_broadcast_message('Hello world')

    # Send unicast message to specify address
    channel.send_message_to('Hello world', address='10.11.12.13')

    while True:
        time.sleep(1)
