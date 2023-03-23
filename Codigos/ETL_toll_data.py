# import the libraries
from datetime import timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to write tasks!
from airflow.operators.bash_operator import BashOperator
# This makes scheduling easy
from airflow.utils.dates import days_ago

#defining DAG arguments
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'Diogo',
    'start_date': days_ago(0),
    'email': ['diogoantonio57@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# define the DAG
dag = DAG(
    dag_id = 'ETL_toll_data',
    default_args = default_args,
    description = 'Apache Airflow Final Assignment',
    schedule_interval = timedelta(days=1),
)

# define the tasks
# First task the unzip data
unzip_data = BashOperator(
    task_id = 'unzip_data',
    bash_command = 'tar -xf ~/Documentos/Projetos\ Python/Projeto_ETL_Coursera/Dados/tolldata.tgz',
    dag = dag,
)

# Extract data from vehicle-data.csv
extract_data_from_csv = BashOperator(
    task_id = 'extract_data_from_csv',
    bash_command = 'cat ~/Documentos/Projetos\ Python/Projeto_ETL_Coursera/Dados/vehicle-data.csv | cut -d "," -f1,2,3,4 > csv_data.csv',
    dag = dag
)

# Extract data from tollplaza-data.tsv
extract_data_from_tsv = BashOperator(
    task_id = 'extract_data_from_tsv',
    bash_command = "cat ~/Documentos/Projetos\ Python/Projeto_ETL_Coursera/Dados/tollplaza-data.tsv |"\
                   "awk '{print $9, $10, $11}' | tr $' ' ',' > tsv_data.csv",
    dag = dag
)

# Extract data from payment-data.txt
extract_data_from_fixed_width = BashOperator(
    task_id = 'extract_data_from_fixed_width',
    bash_command = "cat ~/Documentos/Projetos\ Python/Projeto_ETL_Coursera/Dados/payment-data.txt | " \
                   "awk '{print $10, $11}' | tr ' ' ',' > fixed_width_data.csv",
    dag = dag
)

# Consolidate data extracted from previous tasks
consolidate_data = BashOperator(
    task_id = 'consolidate_data',
    bash_command = fr"paste -d ',' " \
                   fr"~/Documentos/Projetos\ Python/Projeto_ETL_Coursera/Dados/csv_data.csv " \
                   fr"~/Documentos/Projetos\ Python/Projeto_ETL_Coursera/Dados/tsv_data.csv " \
                   fr"~/Documentos/Projetos\ Python/Projeto_ETL_Coursera/Dados/fixed_width_data.csv " \
                   fr"| tr -d '\r' > extracted_data.csv",
    dag = dag
)

# transform and load the data
transform_data = BashOperator(
    task_id = 'transform_data',
    bash_command = "cat extracted_data.csv | awk -F',' '{print $1,$2,$3,toupper($4),$5,$6,$7,$8,$9}' OFS=',' > transformed_data.csv",
    dag = dag
)

unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width >> consolidate_data >> transform_data