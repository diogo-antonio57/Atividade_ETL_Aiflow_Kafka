# ETL usando Airflow e Kafka

Atividade da trilha IBM Data Engineering - etl and data pipelines shell airflow kafka.

## Sobre

Esa atividade coniste no aprendizado de Extração, Tranformção e Carregamento dos dados (ETL). A primeira etapa de extração é responsável pela aquisição dos arquivos e extrair de forma que possam ser acessados, a segunda etapa que é transformação realiza a preparação dos dados par que fiquem no formato correto para a utilização e a última etapa de carregamento dos dados é responsável pela publicação dos dados.

## Dependências

Para executar os arquivos é necessário ter o python, kafka e ariflow instalado na máquina.

## Estrutura de diretórios

```
├── LICENSE
├── README.md
├── Dados <- Diretório contendo os dados brutos.
│ ├── ._tollplaza-data.tsv 
│ ├── ._vehicle-data.csv
│ ├── csv_data.csv
│ ├── extracted_data.csv
│ ├── fileformats.txt
│ ├── fixed_width_data.csv
│ ├── payment-data.txt
│ ├── tolldata.tgz
│ ├── tollplaza-data.tsv
│ ├── tsv_data.csv
│ ├── tsv_data.txt
│ ├── vehicle-data.csv
│
├── Codigos <- Contém scripts em python.
│ ├── ETL_toll_data.py
│ ├── streaming_data_reader.py
│ ├── toll_traffic_generator.py
```
