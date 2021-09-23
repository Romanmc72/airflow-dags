#!/usr/bin/env python3
"""This is for settings common across DAGs"""
from datetime import datetime
from datetime import timedelta


def default_args(**kwargs) -> dict:
    """returns a dict of default args that can be overridden"""
    defaults = {
        "owner": "roman",
        "start_date": datetime(2021, 9, 22),
        "catchup": False,
        "max_active_runs": 1,
        "schedule_interval": None,
        "retries": 3,
        "execution_timeout": timedelta(minutes=1),
    }
    defaults.update(**kwargs)
    return defaults
