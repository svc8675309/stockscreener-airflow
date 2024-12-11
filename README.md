# stockscreener-airflow

( This is a work in progress - Expected changes.)

This project shows how to install apache airflow and run a simple task to get stocks using yahoo-fin.

It's the bases for a larger project that takes this stock data and expands on it which has not been yet written.

This has been written for a Mac.

# Setup

## Install Python

### Install virtualenv dependency
We will run airflow in its own `virtual environment` that we create here locally to control dependencies.  
* First ensure that your python has virtualenv installed.
    ```
    $ virtualenv --version
    virtualenv X.X.X  ( if this does not display then run )
    $ pip install virtualenv ( or if not available ) pip3 install virtualenv

    ( We want virtualenv available in your default python installation )
    ```

### Ensure that Python 3.11 is installed 

A local copy of python is placed in ./`venv` directory. We will be using python 3.11.
* I use brew which installed symbolic link to it on my box at /usr/local/bin/python3.11
  ```
  ls -la /usr/local/bin/python3.11

  lrwxr-xr-x  1 scott  admin  44 Dec 11 03:51 /usr/local/bin/python3.11 -> ../Cellar/python@3.11/3.11.11/bin/python3.11
  ``` 

*  Note: If you don't want to use 3.11 then change this value in this Makefile
    ```
    export PYTHON_VERSION=3.11
    ``` 

* To get it all running execute
  ```
  make all
  ``` 

* Once sucessful you should see airflow start up in the terminal ( after this only execute $`make run` to start it up again).
  ```
  | ____    |__( )_________  __/__  /________      __
  | ____  /| |_  /__  ___/_  /_ __  /_  __ \_ | /| / /
  | ___  ___ |  / _  /   _  __/ _  / / /_/ /_ |/ |/ /
  | _/_/  |_/_/  /_/    /_/    /_/  \____/____/|__/
  ```
* http://0.0.0.0:8080 admin/( the password is in a generated file in this dir named `standalone_admin_password.txt`)  

* Execute DAG `stock_analysis`
* See directory `.\data\ticker` Fill with all my favorite stock quotes
* This list was provided by `.\data\exchanges\my_picks.csv`
* Currently airflow is pointed to the src dir, so any python you want to experiment with put under there.

 

