import datetime
import logging
import azure.functions as func
from .Config.AppConfig import config
from .Services.GraphClient import GraphAPIClient
from .Services.ParquetUploader import upload_to_blob

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()

    logging.info('Python timer trigger function ran at %s', utc_timestamp)

    graph_client = GraphAPIClient(config)
    files = graph_client.get_recent_files()

    for file in files:
        df = graph_client.download_excel_as_dataframe(file)
        if df is not None:
            parquet_path = f"/tmp/{file.name.replace('.xlsx', '.parquet')}"
            df.to_parquet(parquet_path, engine="pyarrow")
            upload_to_blob(parquet_path, file.name.replace('.xlsx', '.parquet'), config)
            logging.info(f"Processed and uploaded: {file.name}")
