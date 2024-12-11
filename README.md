# Stockscreener-airflow

```check out branch - v1.0-get-my-stocks``` 

This project installs apache airflow and run a simple DAG to get stocks using yahoo-fin.

It's the bases for a larger project that takes this stock data and expands on it which has not been yet written :-)

I use a Mac which some instructions below pertain too. 

# Setup

## Install Python

### Ensure that Python 3.11 is installed 

* I use brew which installed symbolic link to 3.11 on my box at /usr/local/bin/python3.11
  ```
  ls -la /usr/local/bin/python3.11

  lrwxr-xr-x  1 XXX  XXX  44 Dec 11 03:51 /usr/local/bin/python3.11 -> ../Cellar/python@3.11/3.11.11/bin/python3.11
  ```
  *  If 3.11  not installed `brew install python@3.11`
  *  If you don't want to use 3.11 then change this value in file Makefile to what you want ( I tested with 3.11 ).
    ```
    export PYTHON_VERSION=3.11
    ``` 

### Install virtualenv dependency
A local copy of python is placed in ./`venv` directory. 
The code runs airflow in its own `virtual environment` to control dependencies.  
* Verify virtualenv is installed.
    ```
    $ virtualenv --version
    virtualenv X.X.X  ( if this does not display then run )
    $ pip install virtualenv ( or if not available ) pip3 install virtualenv

    ( This makes virtualenv available to your default python installation )
    ```

* To get it all running execute
  ```
  make all
  ```
  * Each step in the Makefile may be run seperately [ clean venv install requirements run ]. 

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

 

