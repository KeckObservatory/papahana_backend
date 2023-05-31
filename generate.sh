#!/bin/bash

#swagger-codegen generate -i papahana.yaml -l python-flask -c python_codegen_config.json 
openapi-generator-cli generate -i papahana.yaml -g python-flask -c python_codegen_config.json 

