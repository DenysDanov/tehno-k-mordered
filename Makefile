all:
	docker-compose build
	docker-compose run --rm extract cp -r /usr/local/lib/python3.9/dist-packages /host

start:
	docker-compose up

stop:
	docker-compose stop

runserver:
	docker-compose up runserver

shell:
	docker-compose run --rm shell /bin/bash

