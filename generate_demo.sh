docker run --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli-v3 generate \
    -i https://github.com/KeckObservatory/papahana_backend/blob/main/papahana_demo_2.yaml \
    -l python-flask \
    -o /papahana_flask_server_demo \
    -v
