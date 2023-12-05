# apache-airflow

#### Para atiar o venv (mantém as bibliotecas do python em um ambiente virtual)
- python3 -m venv .venv
- source .venv/bin/activate
- pip install apache-airflow

#### Exportar path do airflow
export AIRFLOW_HOME=$PWD
echo $AIRFLOW_HOME

#### Iniciar o banco de dados do Airflow
airflow db init

#### Cadastrar usuário admin
airflow users create \
    --username vgoulart \
    --firstname Victor \
    --lastname Goulart \
    --role Admin \
    --email victor2.goulart@email.com

#### Iniciar WebServer
airflow webserver -p 8084

#### Iniciar o Scheduler
airflow scheduler
