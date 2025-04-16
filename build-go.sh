rm -rf client-go

docker run -u $(id -u ${USER}):$(id -g ${USER}) --rm -v "${PWD}:/local" openapitools/openapi-generator-cli:v7.12.0 generate \
    -i /local/openapi.yaml \
    -g go \
    -o /local/client-go \
    --additional-properties=projectName=carstack-client,packageVersion=1.0.0
