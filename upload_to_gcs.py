from google.cloud import storage


def upload_to_gcs(bucket_name, source_file_name, destination_blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)

bucket_name = 'redis123'
tables = ['customer', 'orders', 'lineitem', 'supplier', 'part', 'partsupp', 'nation', 'region']
for table in tables:
    source_file_name = f'./tpch-dbgen/{table}.tbl'
    destination_blob_name = f'tpch/{table}.csv'
    upload_to_gcs(bucket_name, source_file_name, destination_blob_name)
    print(f'Uploaded {source_file_name} to {destination_blob_name}')
