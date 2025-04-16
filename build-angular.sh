rm -rf client-angular

docker run -u $(id -u ${USER}):$(id -g ${USER}) --rm -v "${PWD}:/local" openapitools/openapi-generator-cli:v7.12.0 generate \
    -i /local/openapi.yaml \
    -g typescript-angular \
    -o /local/client-angular \
    --additional-properties=npmName=@carstack/rest-client,npmVersion=1.0.0,useSingleRequestParameter=true

cd client-angular
npm install --force
npm run build
