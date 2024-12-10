
# Global CONSTANT Airflow ENV Variables ----------------
export SQLALCHEMY_SILENCE_UBER_WARNING=1
export NO_PROXY=* #https://github.com/apache/airflow/discussions/24463
export AIRFLOW__CORE__LOAD_EXAMPLES=False

# Version of python to use
export PYTHON_VERSION=3.11

# Version of airflow to use
export AIRFLOW_VERSION=2.7.3

# Creates a python virtual environment
venv:
	virtualenv venv -p $(PYTHON_VERSION)
	echo "[global]" > ./venv/pip.conf
	echo "timeout = 30" >> ./venv/pip.conf
	echo "index-url = https://pypi.org/simple/" >> ./venv/pip.conf

# Nuke everything that was generated
clean:
	git clean -Xdf

# Install Airflow to the local virtual environment ( venv )
install:
	sh ./install.sh $(AIRFLOW_VERSION)
	
requirements:
	./venv/bin/pip install -r requirements.txt

run:
	sh ./run.sh			

# tells the make file to always ignore what it thinks the state of these targets are AKA no more - make: <target> is up to date.
.PHONY: all clean venv install requirements run

all: clean venv install requirements run
