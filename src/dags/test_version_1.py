#!/usr/bin/env python3
"""Back to the V1 syntax"""
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

from helpers import settings


def python_func():
    print("Ssssssuck my ass")


with DAG(
    "test_version_1", default_args=settings.default_args(schedule_interval="@once")
) as dag:
    t_starting = BashOperator(
        task_id="starting", bash_command="echo 'Fuck You Miss Daisy!'"
    )

    t_also_starting = PythonOperator(
        task_id="also_starting",
        python_callable=python_func,
    )

    t_combined = BashOperator(task_id="combined", bash_command="echo 'Well fuck'")

    [t_starting, t_also_starting] >> t_combined
