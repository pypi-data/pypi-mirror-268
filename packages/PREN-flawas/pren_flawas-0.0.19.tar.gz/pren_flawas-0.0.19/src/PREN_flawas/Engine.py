import json, time
import sys
import logging
import logging.config
import RPi.GPIO as GPIO
from os import path

log_file_path = path.join(path.dirname(path.abspath(__name__)), 'logger.config')
logging.config.fileConfig(log_file_path)
logger = logging.getLogger("Engine")


__config = {
    "Solenoid": [
        {
            "Red": 20,
            "Yellow": 16,
            "Blue": 26,
            "Weight": 23
        }, {
            "DelayColors": 1,
            "DelayWeight": 0.02
        }
    ],
    "Stepperengine": [
        {
            "Enable": 6,
            "Direction": 5,
            "Step": 13,
            "DelaySteps": 0.0005,
            "NumberOfSteps": 800
        }
    ],
    "Piezo": [{
        "GIPO": 12,
        "Time": 2
    }],
    "Inputs": [
        {
            "Start": 27,
            "EmergencyStop": 22,
            "EmergencyPressed": False
        }
    ]
}

__pos = {
    "Yellow": 1,
    "Red": 2,
    "Blue": 3
}

__AllActors = [__config["Solenoid"][0]["Red"], __config["Solenoid"][0]["Blue"], __config["Solenoid"][0]["Yellow"],
               __config["Solenoid"][0]["Weight"], __config["Stepperengine"][0]["Enable"]]


def setup():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(__config["Solenoid"][0]["Yellow"], GPIO.OUT)
    GPIO.setup(__config["Solenoid"][0]["Red"], GPIO.OUT)
    GPIO.setup(__config["Solenoid"][0]["Blue"], GPIO.OUT)
    GPIO.setup(__config["Solenoid"][0]["Weight"], GPIO.OUT)

    GPIO.setup(__config["Stepperengine"][0]["Enable"], GPIO.OUT)
    GPIO.setup(__config["Stepperengine"][0]["Direction"], GPIO.OUT)
    GPIO.setup(__config["Stepperengine"][0]["Step"], GPIO.OUT)
    GPIO.output(__config["Stepperengine"][0]["Enable"], GPIO.HIGH)

    GPIO.setup(__config["Piezo"][0]["GIPO"], GPIO.OUT)
    GPIO.setup(__config["Inputs"][0]["Start"], GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(__config["Inputs"][0]["EmergencyStop"], GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.add_event_detect(__config["Inputs"][0]["Start"], GPIO.FALLING, callback=button_start_callback, bouncetime=100)
    GPIO.add_event_detect(__config["Inputs"][0]["EmergencyStop"], GPIO.RISING, callback=button_pressed_callback,
                          bouncetime=100)
    PiezoPin = GPIO.PWM(__config["Piezo"][0]["GIPO"], 100)
    logging.debug("Engine setup done")

def wait_startButton():
    while True:
        if GPIO.event_detected(__config["Inputs"][0]["Start"]):
            break
        else:
            logging.info("Warten für Startknopf")
            time.sleep(1)


def wait_emergencyButton():
    while True:
        if __config["Inputs"][0]["EmergencyPressed"]:
            logging.warning("EmergencyButton gedrückt")
            sys.exit(0)
            logging.info("Alle Prozesse beendet")
        else:
            logging.debug("EmergencyButton OK")
            time.sleep(0.5)


def button_start_callback(channel):
    logging.info("Startknopf betätigt")


def button_pressed_callback(channel):
    logging.warning("Emergency pressed")
    # GPIO.output(__AllActors, GPIO.LOW)
    __config["Inputs"][0]["EmergencyPressed"] = True
    # ->Rückmeldung für Display


def turnRight():
    GPIO.output(__config["Stepperengine"][0]["Enable"], GPIO.LOW)
    time.sleep(0.01)
    for i in range(__config["Stepperengine"][0]["NumberOfSteps"]):
        GPIO.output(__config["Stepperengine"][0]["Direction"], GPIO.LOW)
        GPIO.output(__config["Stepperengine"][0]["Step"], GPIO.HIGH)
        time.sleep(__config["Stepperengine"][0]["DelaySteps"])
        GPIO.output(__config["Stepperengine"][0]["Step"], GPIO.LOW)
    GPIO.output(__config["Stepperengine"][0]["Enable"], GPIO.HIGH)
    logging.debug("Turn right")
    # incrementPosition()


def turnLeft():
    GPIO.output(__config["Stepperengine"][0]["Enable"], GPIO.LOW)
    time.sleep(0.01)
    for x in range(__config["Stepperengine"][0]["NumberOfSteps"]):
        GPIO.output(__config["Stepperengine"][0]["Direction"], GPIO.HIGH)
        GPIO.output(__config["Stepperengine"][0]["Step"], GPIO.HIGH)
        time.sleep(__config["Stepperengine"][0]["DelaySteps"])
        GPIO.output(__config["Stepperengine"][0]["Step"], GPIO.LOW)
    GPIO.output(__config["Stepperengine"][0]["Enable"], GPIO.HIGH)
    logging.debug("Turn left")
    # Todo: Decrement function


def incrementPosition():
    if __pos["Yellow"] == 4:
        __pos["Yellow"] = 1
    else:
        __pos["Yellow"] = __pos["Yellow"] + 1
    if __pos["Red"] == 4:
        __pos["Red"] = 1
    else:
        __pos["Red"] = __pos["Red"] + 1
    if __pos["Blue"] == 4:
        __pos["Blue"] = 1
    else:
        __pos["Blue"] = __pos["Blue"] + 1


def getIncrementPos(colorName):
    if colorName == "Blue":
        return __pos["Blue"]
    if colorName == "Red":
        return __pos["Red"]
    if colorName == "Yellow":
        return __pos["Yellow"]

def solYellow():
    GPIO.output(__config["Solenoid"][0]["Yellow"], GPIO.HIGH)
    time.sleep(__config["Solenoid"][1]["DelayColors"])
    GPIO.output(__config["Solenoid"][0]["Yellow"], GPIO.LOW)
    logging.info("Gelber Würfel gestossen")


def solRed():
    GPIO.output(__config["Solenoid"][0]["Red"], GPIO.HIGH)
    time.sleep(__config["Solenoid"][1]["DelayColors"])
    GPIO.output(__config["Solenoid"][0]["Red"], GPIO.LOW)
    logging.info("Roter Würfel gestossen")


def solBlue():
    GPIO.output(__config["Solenoid"][0]["Blue"], GPIO.HIGH)
    time.sleep(__config["Solenoid"][1]["DelayColors"])
    GPIO.output(__config["Solenoid"][0]["Blue"], GPIO.LOW)
    logging.info("Blauer Würfel gestossen")


def solWeight():
    GPIO.output(__config["Solenoid"][0]["Weight"], GPIO.HIGH)
    time.sleep(__config["Solenoid"][1]["DelayWeight"])
    GPIO.output(__config["Solenoid"][0]["Weight"], GPIO.LOW)
    logging.info("Gewicht losgelassen")


def piezo():
    GPIO.output(__config["Piezo"][0]["GIPO"], GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(__config["Piezo"][0]["GIPO"], GPIO.LOW)
    logging.info("Piezo tönt")