#!/bin/bash
source `pwd`/venv/bin/activate

# https://airflow.apache.org/docs/apache-airflow/stable/installation/installing-from-pypi.html
set AIRFLOW_VERSION=$1
echo "Airflow version is ${AIRFLOW_VERSION}"
EXACT_PYTHON_VERSION="$(./venv/bin/python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"
echo "Exact python version is ${EXACT_PYTHON_VERSION}"
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${EXACT_PYTHON_VERSION}.txt"
echo "CONSTRAINT_URL is ${CONSTRAINT_URL}"
pip install --upgrade pip
pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
export AIRFLOW_HOME=`pwd`
airflow db migrate