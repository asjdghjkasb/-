from core.initialize import globals
from core.initialize import system
from core.initialize.printf import printfa
from core.initialize.printf import printToConsole
from core.initialize.printf import printToFile
from core.bin.OInitializeURL import OInitializeURL

def app():
    ObaseURL=OInitializeURL(globals.get_value("BaseURL_Path"))
    