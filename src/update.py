import requests
from debug import debug_print

UPDATE_URL = 'https://raw.githubusercontent.com/rompelhd/AdminFreeExec/refs/heads/main/version'
CURRENT_VERSION = '0.2.0'
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

    URLUPD = "https://github.com/rompelhd/AdminFreeExec/releases/tag/v" + LATEST_VERSION
    response = requests.get(URLUPD)

    if "AdminFreeExec.exe" in response.text:
        download_url = "https://github.com/rompelhd/AdminFreeExec/releases/download/v" + LATEST_VERSION + "/AdminFreeExec.exe"
        exe_response = requests.get(download_url)

        if exe_response.status_code == 200:
            with open("AdminFreeExec.exe", "wb") as f:
                f.write(exe_response.content)
            debug_print("AdminFreeExec.exe descargado y sobrescrito", "INFO")
        else:
            debug_print("Error al descargar AdminFreeExec.exe", "ERROR")
    else:
        debug_print("AdminFreeExec.exe no encontrado", "WARNING")
