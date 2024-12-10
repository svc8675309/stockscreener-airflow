# **billing-ops-airflow**

```
# **Quick Setup**
* Make sure `billing-airflow` project is clonned in the parent directory while developing this project locally. An editable version of `billing-airflow` is installed by Makefile step dev_requirement and the following error message is displayed if its not available while executing `make dev`.
  ```
  Makefile:43: *** billing-airflow does not exist in parent folder!. Stop.
  ```
* `Install virtualenv dependency`. We will run airflow in its own `virtual environment` that we create here locally to control dependencies. It's much like npm_modules for web development. First ensure that your python has virtualenv installed.
  ```
  $ virtualenv --version
  virtualenv X.X.X  ( if this does not display then run )
  $ pip install virtualenv ( or if not available ) $pip3 install virtualenv
  ```
* `Create a new virtual environment`, a local copy of python is placed in `venv` directory. We will be using python 3.11 [https://airflow.apache.org/docs/apache-airflow/stable/installation/installing-from-pypi.html]
  ```
  $ virtualenv venv -p 3.11
  If you see an error >> RuntimeError: failed to find interpreter for Builtin discover of python_spec='3.11 then this is a possibility
          I use homebrew ( you don't have too, miniconda is great ) if you wan to to then follow along.
          Note: This takes a while... it installs a bunch of python versions ( ls /usr/local/opt/python* shows them all) <-- don't freak, you path is not modified. See [https://cloud.google.com/composer/docs/concepts/versioning/composer-versions

	        virtualenv venv -p 3.11
         
               $ brew install python@3.11
          Modify our .zshrc or .bash_profile and add
               export PATH="/usr/local/opt/python3/bin:$PATH"
          Homebrew will symlink to python3 and the alias used this instead of the default 2.x installed by the OS
               $ brew list | grep python
                  ...
                   python@3.11
                  ...
      
          # All we are doing here is updating symbolic links to python3 / pip3 ... I did unlink just be be sure, but not required.
               $ brew unlink python@3.9
               $ brew unlink python@3.7
               $ brew link --force python@3.11
          
          $ virtualenv venv -p 3.11

          Notice that a directory was created named venv and contained within is a python installation.
          Source it.... Meaning for the remainder of the time we use this project we want to use the python version that we created for it.
       
          $ source venv/bin/activate
          $ python --version
            Python 3.11.xx  

   Notice that your command prompt changes to (venv) ... $   <  this tells you that you are using this local python environment.
          Source this every time. The reason why is this creates an environment exactly like our target in airflow.
  ```
* `Execute for dev` the following command for setting up dev and `running airflow`.
   ```
   
   -- To set up credentials
  
   Log into the target environment. for example log into  into https://dev1.dev.clover.com/admin and extracts the internalSession
   In the terminal execute 
   $ export internalSession="XXXXX"

   Now 
   $ make dev

   Note: to modify the credentials at any time simply export internalSession execute $ make data.
   
   Looking at the Makefile, notice that the following targets were executed: clean venv airflow-install dev-env dev-tests dev-run
   ```
* `Execute for prod` the following command for setting up and `running airflow` which will look like it does in production.
   ```
   $ make prod
   
   Looking at the Makefile, notice that the following targets were executed: clean venv airflow-install env dist install run
   ```
* `If you want formatting` 
  ```
  $ source venv/bin/activate
  $ pip install black
  ```
  Under vscode settings search for "python format black" and make sure "Black Path" is set to 
  "${workspaceFolder}/venv/bin/black". Also make sure "Black Args" has "--line-length 120" and that the python formatting provider is black. 
  Then one can click on a file and select "format document"

# **BEFORE YOU COMMIT**
```
$ make test
```
The following executes lint which should be done prior to a commit.



### Code formatting
In python, code formatters, like everyting else is installed va pip. 
Ideally you would select the venv that was created for this env by calling `make dev-env`
In the lower right hand corner of VSCODE ( in the blue ) you will see the python interpreter.
Point that to your local-to-this-directory venv
From the command line source this env `$ source `pwd`/venv/bin/activate`. To manually do it use: 
`pip install black`
`python -m black --line-length=120 <fully qualified file>`