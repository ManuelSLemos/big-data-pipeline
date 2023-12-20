refresh:
	git pull

docker-start:
	docker compose up

start-notebook:
	docker compose up notebook

bash:
	docker run --rm \
	-w /app \
	-v ${PWD}:/app \
	-it python:3.10 bash