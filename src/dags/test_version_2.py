#!/usr/bin/env python3
"""This is my first DAG to explore airflow version 2."""
from airflow.decorators import dag
from airflow.decorators import task

from helpers import settings


@dag("test_version_2", default_args=settings.default_args(schedule_interval="@once"))
def my_test_dag():
    @task
    def extract():
        print("Extracting!")
        return {"a": 1, "b": 2, "c": 3}

    @task
    def transform(data):
        print("Transforming!")
        keys = []
        total = 0
        for key, value in data.items():
            keys.append(key)
            total += value

        keys.sort()
        return {"".join(keys): total}

    @task
    def load(transformed_data):
        print("Loading!")
        print(f"Loaded the data {transformed_data}")

    extracted_data = extract()
    transformed_data = transform(data=extracted_data)
    load(transformed_data=transformed_data)


test_version_2 = my_test_dag()
