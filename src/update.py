import requests
from debug import debug_print

UPDATE_URL = 'https://raw.githubusercontent.com/rompelhd/AdminFreeExec/refs/heads/main/version'
CURRENT_VERSION = '0.2.1'
LATEST_VERSION = None

def check_update_applicationfor_update():
    response = requests.get(UPDATE_URL)
    response.raise_for_status()

    LATEST_VERSION = response.text.strip()
    debug_print(f"Response status code: {response.status_code} Latest version fetched: {LATEST_VERSION}", "INFO")
        
    
def result_update():
    try:
        if LATEST_VERSION != CURRENT_VERSION:
            return True
        return False
    except Exception as e:
        debug_print(f"Error checking for update: {e}", "ERROR")
        return False
    
def update_application():
    debug_print(f"Actualizando", "INFO")
