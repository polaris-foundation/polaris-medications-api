#!/bin/bash
SERVER_PORT=${1-5000}
export SERVER_PORT=${SERVER_PORT}
export DATABASE_HOST=localhost
export DATABASE_PORT=5432
export DATABASE_USER=dhos-medications-api
export DATABASE_PASSWORD=dhos-medications-api
export DATABASE_NAME=dhos-medications-api
export FLASK_APP=dhos_medications_api/autoapp.py
export ENVIRONMENT=DEVELOPMENT
export ALLOW_DROP_DATA=true
export LOG_LEVEL=${LOG_LEVEL:-DEBUG}
export LOG_FORMAT=${LOG_FORMAT:-COLOUR}

if [ -z "$*" ]
then
  flask db upgrade
  python -m dhos_medications_api
else
  flask $*
fi
