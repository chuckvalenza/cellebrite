"""
Written By: Nir Zaltsman
from IDumper import IDumper
import time
class DumperMMC(IDumper):
    def dump(self, start_block = 0 , end_block=None, ram_address=0x56C00000, chunk_size=20480, blocks_per_read=256, hw_version = 0, name=""):
        finally: