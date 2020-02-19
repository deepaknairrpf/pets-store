#!/bin/sh
set -e

until psql postgres://$POSTGRES_USER:$POSTGRES_PASSWORD@$POSTGRES_HOST/pets_db -c '\l'; do
    >&2 echo "Postgres is unavailable - sleeping"
    sleep 1
done

>&2 echo "Postgres is up - continuing"

if [ "x$DJANGO_MANAGEPY_MIGRATE" = 'xon' ]; then
    python manage.py migrate --noinput
fi

exec "$@"