# papahana_backend
Observer planning tool frontend, backend, and database

## papahana.yaml
OpenAPI spec maps out Papahana backend calls as defined [here](https://keckobservatory.atlassian.net/wiki/spaces/DSI/pages/808779858/DDOI-005+Programmatic+Web+Interface+Resources). This file can be used by the Swagger Editor to autogenerate a server and client applications. See [these instructions](https://keckobservatory.atlassian.net/wiki/spaces/DSI/pages/875429896/Using+Open+API+3.0)

## generate_data.ipynb
This notebook generates randomized dictionary objects representing artificial observation blocks as desribed in [these pages](https://keckobservatory.atlassian.net/wiki/spaces/DSI/pages/808321035/Change+controlled+documents). 

## generate_gridfs_data.ipynb
[GridFS](https://docs.mongodb.com/manual/core/gridfs/) stores files that exceed BSON's document size limit of 16MB. Files are encoded as ascii readible characters using [base64](https://docs.python.org/3/library/base64.html). This notebook provides basic read/write functions on a local MongoDB.

Data is stored on a local MongoDB collection.
Finally a few function calls are made to query observation blocks.

## controller_helper.py
Used to query database. These functions are to be added to the server controller section. Providing the RestFull API server read/write access to the database.

# papahana_flask_server_demo
Demo of autogenerated flask server, with database calls
