"""
    Written by NirZ
import serial
class ConnectionSerial(IConnection.IConnection):
        if to_open_connection==True:
    def __repr__(self):
    def get_port(self):
    def connect_aux(self, blocking=False):
    def connect(self, blocking=False):        



    def close(self):
        self.dev.close()

    def send(self, data):
        return self.dev.write(data)

    def recv(self, num_bytes = 1024):

    def get_timeout(self):
    
        