# Example of a REST API Client package using OpenAPI Generator

## Building Clients

The clients are generated from an OpenAPI specification file using [OpenAPI Generator](https://openapi-generator.tech/).

### Python Client

```bash
./build-python.sh
```
Follow the instructions from the readme located in the `client-python` directory.

#### Publish Python Client

The client can be optionally also build and published. This allows to use it as a dependency in other projects.

```bash
pip3 install setuptools wheel twine
python setup.py sdist bdist_wheel
twine upload dist/*
```

#### Example Usage

Create a virtual environment:

```bash
virtualenv venv
source ./venv/bin/activate
```

Install the python client:
```bash
pip install -e client-python
```

Run the example script:
```bash
python example.py
```

### Angular Client

```bash
./generate-angular.sh
```

Follow the instructions from the readme located in the `client-angular` directory.

#### Publish Client

The client can be optionally also build and published. This allows to use it as a dependency in other projects.

```bash
cd client
npm install --force
npm run build
npm run publish --access public
```

### Go Client

```bash
./generate-go.sh
```

Follow the instructions from the readme located in the `client-go` directory.


### Rust Client

```bash
./generate-rust.sh
```

Follow the instructions from the readme located in the `client-rust` directory.

