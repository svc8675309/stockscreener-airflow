from airflow.operators.bash import BashOperator
from airflow.models import TaskInstance


class CustomBashOperator(BashOperator):
    def execute(self, context):
        # don't push twice
        self.do_xcom_push = False
        # Run the base class execute method
        return_value = super().execute(context)

        # Push XCom to a custom key
        ti: TaskInstance = context.get("ti")
        ti.xcom_push(key=context.get("run_id"), value=return_value)
        return return_value
