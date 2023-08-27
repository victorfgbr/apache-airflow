#!/bin/bash

cd $( dirname $0 )

airflow_webserver=$( ps aux | grep "airflow webserver" | awk '{ print $2 }' )
[ ! -z "$airflow_webserver" ] \
    && echo "Killing Airflow Webserver [$airflow_webserver]" \
    && kill $airflow_webserver

airflow_scheduler=$( ps aux | grep "airflow scheduler" | awk '{ print $2 }' )
[ ! -z "$airflow_scheduler" ] \
    && echo "Killing Airflow Scheduler [$airflow_scheduler]" \
    && kill $airflow_scheduler
