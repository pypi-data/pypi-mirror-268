from nomad_media_pip.exceptions.api_exception_handler import _api_exception_handler

import requests

def _start_schedule(AUTH_TOKEN, URL, ID, SKIP_CLEANUP_ON_FAILURE, DEBUG):

    if SKIP_CLEANUP_ON_FAILURE == None:
        SKIP_CLEANUP_ON_FAILURE = False

    API_URL = f"{URL}/api/admin/schedule/{ID}/start?skipCleanupOnFailure={SKIP_CLEANUP_ON_FAILURE}"

    HEADERS = {
        "Authorization": "Bearer " + AUTH_TOKEN,
        "Content-Type": "application/json"
    }

    if DEBUG:
        print(f"URL: {API_URL},\nMETHOD: POST")

    try:
        RESPONSE = requests.post(API_URL, headers= HEADERS)

        if not RESPONSE.ok:
            raise Exception()
        
        return RESPONSE.json()
    except:
        _api_exception_handler(RESPONSE, "Start Schedule Failed")
