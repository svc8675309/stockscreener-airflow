from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow.models import TaskInstance
from svc.common.custom_bash_operator import CustomBashOperator

def print_xcom(**kwargs):
    ti: TaskInstance = kwargs['ti']
    output = ti.xcom_pull(task_ids='bash_task')
    print(output)

available_choices = ['option1', 'option2', 'option3']

with DAG(
    'bash_operator_output',
    start_date=datetime(2024, 12, 5),
    schedule_interval=None,
    params={"selected_option": "option1"},
) as dag:

# By default, any operator that returns a value creates an XCom
    bash_who_am_i_task = CustomBashOperator(
        task_id='bash_who_am_i_task',
        bash_command='echo "Current user: $(whoami)"'
    )

    # By default, any operator that returns a value creates an XCom
    bash_task = CustomBashOperator(
        task_id='bash_task',
        bash_command='kubectl -n microflow-perf-test get pods'
    )
    
    python_task = PythonOperator(
        task_id='python_task',
        python_callable=print_xcom
    )

    bash_who_am_i_task >> bash_task >> python_task