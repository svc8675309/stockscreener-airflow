#!/bin/bash
source `pwd`/venv/bin/activate
export AIRFLOW_HOME=`pwd`
# Override some airflow.cfg settings without changing the file
# https://airflow.apache.org/docs/apache-airflow/stable/howto/set-config.html
export AIRFLOW__CORE__DAGS_FOLDER=`pwd`/src
# export AIRFLOW__WEBSERVER__WORKER_REFRESH_INTERVAL=6000
airflow standalone
