from google.cloud import bigquery


def load_data_to_bigquery(dataset_id, table_id, source_uri):
    client = bigquery.Client()
    dataset_ref = client.dataset(dataset_id)
    table_ref = dataset_ref.table(table_id)
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        autodetect=True,
    )
    load_job = client.load_table_from_uri(
        source_uri, table_ref, job_config=job_config
    )
    load_job.result()

dataset_id = 'tpch_dataset'
bucket_name = 'redis123'
for table in ['customer', 'orders', 'lineitem', 'supplier', 'part', 'partsupp', 'nation', 'region']:
    source_uri = f'gs://{bucket_name}/tpch/{table}.csv'
    load_data_to_bigquery(dataset_id, table, source_uri)
