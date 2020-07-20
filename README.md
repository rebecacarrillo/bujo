# THIS IS THE BUJO CLI


## Docker info

```
docker pull rcarrillo9/bujo-cli:latest
docker build -t bujo .
docker run rcarrillo9/bujo-cli

```

## Install Locally
```
python setup.py bdist_wheel
python -m pip install dist/bujocli-0.1-py3-none-any.whl
```

### Guidelines

1. When you install/import a new package, do `pip freeze > requirements.txt` 
to save the package to our requirements file. 

