# apache-airflow

#### Para atiar o venv (mantém as bibliotecas do python em um ambiente virtual)
source .venv/bin/activate

#### Exportar path do airflow
export AIRFLOW_HOME=$PWD

#### Iniciar o banco de dados do Airflow
airflow db init

#### Cadastrar usuário admin
airflow users create \
    --username admin \
    --firstname Victor \
    --lastname Goulart \
    --role Admin \
    --email victor.goulart@email.com

#### Iniciar WebServer
airflow webserver -p 8084

#### Iniciar o Scheduler
airflow scheduler
