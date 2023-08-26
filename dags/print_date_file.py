
from __future__ import annotations

import datetime

import pendulum

import airflow
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import timedelta

default_args = {
    'owner': 'airflow',
    'start_date': airflow.utils.dates.days_ago(2)
}

dag = DAG(
    dag_id='save_date_in_file_txt',
    schedule="0 0 * * *",
    default_args=default_args,
    schedule_interval=timedelta(days=1),
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    dagrun_timeout=timedelta(minutes=60),
    tags=['print_date_file']
)

# Imprime a data na saída padrão.
t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag
)

# Cria a pasta tmp caso ela não exista.
t2 = BashOperator(
    task_id="make_directory",
    bash_command="mkdir -p /home/vgoulart/git/apache-airflow/tmp",
    dag=dag
)

# Faz uma sleep de 5 segundos.
t3 = BashOperator(
    task_id='sleep',
    bash_command='sleep 5',
    retries=3,
    dag=dag
)

# Salve a data em um arquivo texto.
t4 = BashOperator(
    task_id='save_date',
    bash_command='date > /home/vgoulart/git/apache-airflow/tmp/date_output.txt',
    retries=3,
    dag=dag
)

# Fluxo de execução das tasks
t1 >> t2 >> t3 >> t4 

if __name__ == "__main__":

    dag.test()

