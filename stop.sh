#!/bin/bash

# stop webserver
ps aux | grep "airflow webserver" | awk '{ print $2 }' | xargs kill

# stop scheduler
ps aux | grep "airflow scheduler" | awk '{ print $2 }' | xargs kill
