# momock
Quick amivapi mockup for momo to test beer/coffee purchase api.
Because I like bad puns it's therefore namend "momock" ;)

It provides a fraction of the API needed to process purchases.

There are two endpoints:

`users`: With the fields firstname, lastname and rfid only.
	All methods publicly accesible to be used easily.

`purchases`: With all fields as in the API.
	This is secured by authenication logic mimicking the need for an API key.
	In this test the key is hardcoded as "supersecretkey12".
	So adding a Basic Auhtentication header with username: "api key above" and 
	empty password works as it would with the API.

	This api key provides full access to purchases.

# Installation

```
(create venv)
> pip install eve
(clone this repository)
> python momock.py
```

The server is now running!
(Make sure a mongodb instance is running and set mongo user name etc. in
_settings.py_)
