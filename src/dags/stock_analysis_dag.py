from airflow import DAG
from airflow.operators.empty import EmptyOperator
from svc.common.tasks.get_closings_task import get_closings
from datetime import datetime

with DAG(
    'stock_analysis',
    start_date=datetime(2024, 12, 5),
    schedule_interval=None,
) as dag:
    end = EmptyOperator(task_id="end")
    
    get_closings() >> end
