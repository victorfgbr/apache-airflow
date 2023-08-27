#!/bin/bash

cd $( dirname $0 )

echo "Running Apache Airflow"

# Activate virtual env
source .venv/bin/activate
rc=$?
[ ! $rc -eq 0 ] \
    && echo "Error on venv activate, run 'python3 -m venv .venv'" \
    && exit 1

# Export Airflow HOME
airflow_home=$( echo $PWD )
echo "export AIRFLOW_HOME=$airflow_home"
export AIRFLOW_HOME=$airflow_home

# Create Logs directory
airflow_logs="${airflow_home}/logs/"
mkdir -p $airflow_logs

# Run Airflow Scheduler
airflow scheduler >$airflow_logs/airflow.scheduler.log 2>&1 &

# Run Airflow Webserver
airflow webserver >$airflow_logs/airflow.webserver.log 2>&1 &
