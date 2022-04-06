# Observing Database API

## papahana.yaml
OpenAPI specification file

## controller_helper.py
Used to query database. These functions are to be added to the server controller section. Providing the RestFull API server read/write access to the database.

# run
in odb_api directory:
  python3 -m papahana
  
to leave running without hang-ups:
  nohup python3 -m papahana & >> /dev/null &

# Testing
in the test directory (odb_api/papahana/test) the tests can be run individually
    python3 -m unittest -v test_containers_controller
    
Or run all tests together:
    nosetest

# Generate models from the OpenAPI specification files:

swagger-codegen generate -i papahana.yaml -l python-flask -c config.json

where the config.json:
{
    "packageName" : "papahana",
    "packageVersion" : "0.0.1"
}