"""
    Written by NirZ
import serial
class ConnectionNull(IConnection.IConnection):

    def connect(self, blocking = False):
    def close(self):
        print "Device Disconnected"

    def send(self, data):

    def recv(self, num_bytes = 1024):

    def get_timeout(self):