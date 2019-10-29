# Jekeiti API

A Python wrapper for the JKT48 Unofficial API Client

![Python 3.7](https://img.shields.io/badge/python-v3.7-blue) [![Release](https://img.shields.io/github/v/release/muhbayu/jeketi_api)](https://github.com/MuhBayu/jekeiti_api/releases)

## Features
- Accounts
	* Profile info (✓)
	* History points (✓)
	* Jadwal oshimen (✓)
	* Ticket purchase history (todo)
	* Order history (todo)

## Documentation
Available soon

## Install
Install with pip:
```bash
pip install git+https://git@github.com/MuhBayu/jekeiti_api
```

### Usage :
The examples/ are a good source of detailed sample code on how to use the clients, including a simple way to save the auth cookie for reuse

Example Login:
```python
from jeketi_api import Client
api = Client(username, password)
print(api.my_page)
```

### Avoiding Re-login
You are advised to persist/cache the auth cookie details to avoid logging in every time you make an api call.