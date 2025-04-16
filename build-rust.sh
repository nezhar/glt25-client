rm -rf client-rust

docker run -u $(id -u ${USER}):$(id -g ${USER}) --rm -v "${PWD}:/local" openapitools/openapi-generator-cli:v7.12.0 generate \
    -i /local/openapi.yaml \
    -g rust \
    -o /local/client-rust \
    --additional-properties=projectName=carstack-client,packageVersion=1.0.0,useSingleRequestParameter=true
