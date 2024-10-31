## DAG CON SPARK STANDALONE- AIRFLOW - DOCKER

Questo progetto mostra come si possono somministrare dag in locale ad un cluster spark con 2 worker usando airflow (webserver + scheduler) tramite
l'operatore SparkSubmitOperator. Il progetto è configurato per usare python 3.12, quindi usa un immagine specifica "apache/airflow:latest-python3.12"
per adattarsi all'immagine ufficiale "bitnami/spark:latest" che al momento sfrutta la stessa versione python.

Nella UI ricordarsi di impostare la connessione tra airflow e il master in Admin->Connections:
