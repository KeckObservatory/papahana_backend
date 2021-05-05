docker run --rm -v ${PWD}:/local openapitools/openapi-generator-cli generate \
    -i /local/papahana_demo_2.yaml \
    -g python-flask \
    -o /local/out
    -v
