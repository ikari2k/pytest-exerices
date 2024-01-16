import configparser
from pathlib import Path

configFile = 'petStoreConfigQa.ini'
configFolder = 'config'

config = configparser.ConfigParser()
BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
CONFIG_FILE = BASE_DIR.joinpath(configFolder).joinpath(configFile)
config.read(CONFIG_FILE)

def getPetAPIURL():
    return config['pet']['url']

def getStoreAPIURL():
    return config['store']['url']