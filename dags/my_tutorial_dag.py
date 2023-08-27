
from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
import pandas as pd
import requests
import json


def fn_captura_conta_dados():
    url = 'https://data.cityofnewyork.us/resource/rc75-m7u3.json'
    reponse = requests.get(url)
    df = pd.DataFrame(json.loads(reponse.content))
    qtd = len(df.index)
    return qtd

def fn_e_valido(task_instance):
    qtd = task_instance.xcom_pull(task_ids = 'captura_conta_dados')

    if (qtd > 1000):
        return 'valido'
    
    return 'nvalido'

with DAG ('my_tutorial_dag', 
          start_date = datetime(2021, 12, 1),
          schedule_interval = '30 * * * *',
          catchup = False
        ) as dag:
    
    # task
    captura_conta_dados = PythonOperator (
        task_id = 'captura_conta_dados',
        python_callable = fn_captura_conta_dados
    )

    # task
    e_valido = BranchPythonOperator (
        task_id = 'e_valido',
        python_callable = fn_e_valido
    )

    # task
    valido = BashOperator (
        task_id = 'valido',
        bash_command = "echo 'Quantidade OK'"
    )

    # task
    nvalido = BashOperator (
        task_id = 'nvalido',
        bash_command = "echo 'Quantidade não OK'"
    )

    captura_conta_dados >> e_valido >> [valido, nvalido]