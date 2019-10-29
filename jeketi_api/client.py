from .endpoints import (
    AccountsEndpoint
)
from .contstants import Constants
import requests

class Client(AccountsEndpoint, Constants):
    cookie = None
    def __init__(self, email, password, **kwargs):
        self.session = requests.Session()
        self.headers = {
            'Cache-Control':'no-cache',
            'Accept-Language': 'en,en-US;q=0,5',
            'User-Agent': self.USER_AGENT,
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'jkt48.com',
            'Referer': 'https://jkt48.com',
            'Connection': 'keep-alive',
            'Accept': '*/*',
        }
        self.session.headers.update(self.headers)
        self.email = email
        self.password = password
        self.on_login = kwargs.pop('on_login', None)

        user_settings = kwargs.pop('settings', {})
        if user_settings:
            self.cookie = (
                kwargs.pop('cookie', None) or user_settings.get('cookies')
            )
        self.login()
        super(Client, self).__init__()
        
    @property
    def settings(self):
        return {
            'cookies': self.cookie
        }