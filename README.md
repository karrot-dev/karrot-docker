# _karrot_ docker setup

This lets you run everything you need in a docker-compose setup.

## Getting started

```
git clone https://github.com/yunity/karrot-docker.git
cd karrot-docker
git clone https://github.com/yunity/karrot-frontend.git
git clone https://github.com/yunity/karrot-backend.git
docker-compose up -d
```

You can wait for everything to become ready by watching the `wait` container logs:
```
docker-compose logs -f wait
```

You probably want to have some data to play with then:

```
docker-compose exec backend ./manage.py create_sample_data
```

It's up to you to manage your frontend and backend repos, we won't update them. You can switch branches as you desire. You might need to restart frontend or backend after doing so.

We make use of docker volumes to store data, so most useful things should stay around even if you remove the containers with `docker-compose down`.

## Services

Once everything is up and running you can access:

| Name | URL | Description |
|---|---|---|
| main site | [localhost:8080](http://localhost:8080) | |
| swagger backend | [localhost:8000/docs](http://localhost:8000/docs) | view and use the REST API |
| maildev | [localhost:1080](http://localhost:1080) | catchs emails sent by app |
| pgadmin | [localhost:5050](http://localhost:5050) pgadmin4@pgadmin.org:admin then use "db" for host/user/pass | see/view/manage postgres database |
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

Watch for changes, and run tests in parallel:
```
docker-compose exec backend sh -c "find foodsaving -name '*.py' | entr ./manage.py test --parallel 4 --failfast --keepdb"
```

Restart backend:
```
docker-compose restart backend
```

Drop db:
```
docker-compose stop backend pgadmin
docker-compose run backend ./manage.py reset_db --noinput
docker-compose up -d
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
