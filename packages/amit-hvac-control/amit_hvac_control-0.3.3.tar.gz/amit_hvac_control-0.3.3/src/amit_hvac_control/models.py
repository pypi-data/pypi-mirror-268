from enum import Enum


class Config:
    def __init__(self, url: str, username: str, password: str):
        self.url = url
        self.username = username
        self.password = password


class HeatingMode(Enum):
    SCHEDULED = 0
    MINIMAL = 1
    COMFORT = 2

    def get_button(self):
        match self:
            case self.COMFORT:
                return "BTNSUB_g3"
            case self.MINIMAL:
                return "BTNSUB_g4"
            case self.SCHEDULED:
                return "BTNSUB_g5"


class Season(Enum):
    SUMMER = 0
    WINTER = 1

    def get_save_value(self):
        match self:
            case self.SUMMER:
                return {"BITEDIT_i1w4097s255t0j1k1g2": "-2", "BTNSUB_g2": "TOPENÍ"}
            case self.WINTER:
                return {"BITEDIT_i1w4097s255t0j1k1g2": "1", "BTNSUB_g2": "CHLAZENÍ"}


class VentilationMode(Enum):
    OFF = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    AUTO = 4

    def get_button(self):
        match self:
            case self.OFF:
                return "BTNSUB_g2"
            case self.LOW:
                return "BTNSUB_g3"
            case self.MEDIUM:
                return "BTNSUB_g4"
            case self.HIGH:
                return "BTNSUB_g5"
            case self.AUTO:
                return "BTNSUB_g6"
