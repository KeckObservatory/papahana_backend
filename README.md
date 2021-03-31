# papahana_backend
Observer planning tool backend and database

# papahana.yaml
OpenAPI spec maps out Papahana backend calls as defined [here](https://keckobservatory.atlassian.net/wiki/spaces/DSI/pages/808779858/DDOI-005+Programmatic+Web+Interface+Resources). This file can be used by the Swagger Editor to autogenerate a server and client applications. See [these instructions](https://keckobservatory.atlassian.net/wiki/spaces/DSI/pages/875429896/Using+Open+API+3.0)

# generate_data.ipynb
This notebook generates randomized dictionary objects representing artificial observation blocks as desribed in [these pages](https://keckobservatory.atlassian.net/wiki/spaces/DSI/pages/808321035/Change+controlled+documents). 

Data is stored on a local MongoDB collection.
Finally a few function calls are made to query observation blocks.

# controller_helper.py
Used to query database. These functions are to be added to the server controller section. Providing the RestFull API server read/write access to the database.
