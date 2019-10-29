import os
import json
try:
    from jeketi_api import (
        Client, ClientError, ClientLoginError,
        __version__ as client_version)
except ImportError:
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from jeketi_api import (
        Client, ClientError, ClientLoginError,
        __version__ as client_version)

def onlogin_callback(api, setting_name):
    with open(setting_name, 'w') as f:
        f.write(json.dumps(api.settings))
        f.close()

def start():
    USERNAME = ''
    PASSWORD = ''
    cache_filename = 'cookies.txt'
    if os.path.exists(cache_filename):
        with open('cookies.txt', 'r') as f:
            cached_settings = f.read()
        api = Client(USERNAME, PASSWORD, settings=json.loads(cached_settings))
    else:
        api = Client(USERNAME, PASSWORD, on_login=lambda x: onlogin_callback(x, cache_filename))
    print(api.my_page)

if __name__ == '__main__':
    start()