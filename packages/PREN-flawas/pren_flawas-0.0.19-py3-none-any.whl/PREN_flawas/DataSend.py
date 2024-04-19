import requests
import logging
import logging.config
from os import path

# JSON Format
# {
#  "time": 32,
#  "energy": 0.5
# }
#


log_file_path = path.join(path.dirname(path.abspath(__name__)), 'logger.config')
logging.config.fileConfig(log_file_path)
logger = logging.getLogger("DataSend")

def send(url, time, energy):
    reply = requests.post(url=url, json={"time": time, "energy": energy})
    logging.debug(reply.json())
    if reply.status_code == 200:
        return True
    else:
        return False