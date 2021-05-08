#docker run --rm -v ${PWD}:/local  openapitools/openapi-generator-cli generate \
    #-i /local/papahana_demo_2.yaml \
    #-g python-flask \
    #-o /local/papahana_flask_server_demo \
    #-v

docker run --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli-v3 generate \
    -i /local/papahana_demo.yaml \
    -l python-flask \
    -o /local/papahana_flask_server_demo \
    -v
