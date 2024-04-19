import requests, json
from requests.structures import CaseInsensitiveDict
import logging
import logging.config
from os import path

log_file_path = path.join(path.dirname(path.abspath(__name__)), 'logger.config')
logging.config.fileConfig(log_file_path)
logger = logging.getLogger("DataVerify")

def checkAvailability(url):
    payload = {}
    headers = {}
    logging.info("Checking availability of " + url)
    response = requests.request("GET", url)
    if response.status_code == 200:
        logging.debug("checkAvailability" + response.content)
        return True
    else :
        logging.debug("checkAvailability" + response.content)
        return False


def sendStatus(url, token):
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    headers["Auth"] = token
    resp  = requests.post(url, headers=headers)
    logging.debug("sendStatus" + resp.content)
    if resp.status_code == 204:
        logging.debug("sendStatus replied status OK")
        return True
    else:
        logging.debug("sendStatus something went wrong")
        return False


def sendData(url, token, time, config):
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    headers["Auth"] = token
    data = {"time": time,
            "config": config}
    logging.debug("sendData" + json.dumps(data))
    resp = requests.post(url, headers=headers, data=config)
    if resp.status_code == 200:
        logging.debug("sendData replied status OK")
        return True
    else:
        logging.debug("sendData something went wrong")
        return False