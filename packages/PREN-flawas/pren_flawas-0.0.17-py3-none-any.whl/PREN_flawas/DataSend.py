import requests
import logging
import logging.config

# JSON Format
# {
#  "time": 32,
#  "energy": 0.5
# }
#

logging.config.fileConfig('logger.conf')
logger = logging.getLogger("DataSend")

def send(url, time, energy):
    reply = requests.post(url=url, json={"time": time, "energy": energy})
    logging.debug(reply.json())
    if reply.status_code == 200:
        return True
    else:
        return False