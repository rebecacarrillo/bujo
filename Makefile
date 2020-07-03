start:
	python3 bujo/bujo-cli.py

spinup:
    docker pull rcarrillo9/bujo-cli:latest \
    docker build -t rcarrillo9/bujo-cli . \
    docker run rcarrillo9/bujo-cli \
    python3 bujo/bujo-cli.py
