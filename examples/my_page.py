import os
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

def start():
    USERNAME = ''
    PASSWORD = ''
    api = Client(USERNAME, PASSWORD)
    print(api.my_page)

if __name__ == '__main__':
    start()