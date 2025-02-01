import logging
import os

LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOGGER = logging.getLogger("AdminFreeExecLogger")
LOGGER.setLevel(logging.DEBUG)

LOG_FORMAT = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

console_handler = logging.StreamHandler()
console_handler.setFormatter(LOG_FORMAT)
LOGGER.addHandler(console_handler)

file_handler = logging.FileHandler(os.path.join(LOG_DIR, "app_debug.log"), mode="a", encoding="utf-8")
file_handler.setFormatter(LOG_FORMAT)
LOGGER.addHandler(file_handler)

def debug_print(message, level="DEBUG"):
    level = level.upper()
    
    if level == "DEBUG":
        LOGGER.debug(message)
    elif level == "INFO":
        LOGGER.info(message)
    elif level == "WARNING":
        LOGGER.warning(message)
    elif level == "ERROR":
        LOGGER.error(message)
    elif level == "CRITICAL":
        LOGGER.critical(message)
    else:
        LOGGER.debug(f"Nivel desconocido '{level}', mensaje: {message}")
