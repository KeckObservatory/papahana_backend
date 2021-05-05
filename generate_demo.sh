docker run --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli-v3 generate \
    -i papahana_demo_2.yaml \
    -l python-flask \
    -o /papahana_flask_server_demo
