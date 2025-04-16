rm -rf client-python

docker run -u $(id -u ${USER}):$(id -g ${USER}) --rm -v "${PWD}:/local" \
    openapitools/openapi-generator-cli:v7.12.0 generate \
    -i /local/openapi.yaml \
    -g python \
    -o /local/client-python \
    --additional-properties=projectName=carstack,packageName=carstack,packageVersion=1.0.0,useSingleRequestParameter=true
