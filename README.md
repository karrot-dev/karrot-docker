# _karrot_ docker setup

This lets you run everything you need in a docker-compose setup.

## Getting started

```
If you have not already, [install docker-compose](https://docs.docker.com/compose/install/)

git clone https://github.com/yunity/karrot-docker.git
cd karrot-docker
git clone https://github.com/yunity/karrot-frontend.git
git clone https://github.com/yunity/karrot-backend.git
docker-compose up -d
```

(_note: you might want to switch to the git+ssh protocol urls later if you have an SSH key setup at GitHub_)

You can wait for everything to become ready by watching the `wait` container logs:

```
docker-compose logs -f wait
```

If you want to run more commands it's best to start a shell for either the frontend/backend or both.

It's up to you to manage your frontend and backend repos, we won't update them. You can switch branches as you desire. You might need to restart frontend or backend after doing so.

We make use of docker volumes to store data, so most useful things should stay around even if you remove the containers with `docker-compose down`.

### Frontend

Enter a shell by running:

```
./scripts/shell frontend
```

Now you can run commands such as:
* `yarn lint` lint your files
* `yarn add <foo>` add the `foo` dependency

### Backend

Enter a shell by running:

```
./scripts/shell backend
```

Now you can run django commands such as:
* `./manage.py create_sample_data` to create sample data in your database
* `./manage.py test` to run the tests
* `./manage.py test --parallel 4 --failfast --keepdb` run tests with some cool options
- or in the form of: `docker-compose run --no-deps --rm backend ./manage.py` which might be more convenient, because the shell history inside docker is not saved

_note: karrot-docker uses its own local settings file, located at `./docker/backend/local_settings.py`, which shadows the file you typically create at `./karrot-backend/config/local_settings.py`._ So take care to edit the correct file or change `docker-compose.yml`.



## Services

Once everything is up and running you can access:

| Name | URL | Description |
|---|---|---|
| main site | [localhost:8080](http://localhost:8080) | |
| swagger backend | [localhost:8000/docs](http://localhost:8000/docs) | view and use the REST API |
| maildev | [localhost:1080](http://localhost:1080) | catchs emails sent by app |
| pgweb | [localhost:5050](http://localhost:5050) | see/view/manage postgres database |
| grafana | [localhost:4000](http://localhost:4000) admin:admin | see [stats](#stats) section for setup info |

## Useful commands

Watch logs for all containers:
```
docker-compose logs -f
```

Watch logs for a specific container:
```
docker-compose logs -f frontend
```

Seed the database:
```
docker-compose exec backend ./manage.py create_sample_data
```

Restart backend:
```
docker-compose restart backend
```

Drop and recreate db:
```
./scripts/resetdb
```

## Stats

_karrot_ reports stats to influxdb using
[django-influxdb-metrics](https://github.com/bitlabstudio/django-influxdb-metrics).

We can use grafana to visualize them.

Configure datasource:
```
curl -XDELETE http://admin:admin@localhost:4000/api/datasources/name/influxdb
curl -XPOST -H 'Content-Type: application/json' http://admin:admin@localhost:4000/api/datasources -d@stats/datasource.json
```

Configure dashboard:
```
curl -XDELETE http://admin:admin@localhost:4000/api/dashboards/db/requests
curl -XPOST -H 'Content-Type: application/json' http://admin:admin@localhost:4000/api/dashboards/db -d@stats/dashboard.json
```

Then visit [localhost:4000/dashboard/db/requests](http://localhost:4000/dashboard/db/requests) and watch the requests!
