import sys
import os
if sys.version_info[0] < 3:
    raise Exception("Python3 required! Current (wrong) version: {ver}".format(sys.version_info))

base_dir = "/home/cgil/PycharmProjects/cgflask"
os.chdir(base_dir)
sys.path.insert(0, base_dir)
from routes import app as application

