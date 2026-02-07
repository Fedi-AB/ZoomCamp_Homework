#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import click
from sqlalchemy import create_engine
from tqdm.auto import tqdm


@click.command()
@click.option('--pg-user', default='root', show_default=True, help='Postgres user')
@click.option('--pg-password', default='root', show_default=True, help='Postgres password')
@click.option('--pg-host', default='localhost', show_default=True, help='Postgres host')
@click.option('--pg-port', default=5433, show_default=True, type=int, help='Postgres port')
@click.option('--pg-database', default='ny_taxi', show_default=True, help='Postgres database name')
@click.option('--table_name', default='green_taxi_data', show_default=True, help='table name')
@click.option('--chunksize', default=100000, show_default=True, type=int, help='Parquet chunksize for ingestion')
def run(pg_user, pg_password, pg_host, pg_port, pg_database, table_name, chunksize):

    parquet_url = (
        "https://github.com/Fedi-AB/ZoomCamp_Homework/raw/main/"
        "Homework%201:%20Docker,%20SQL%20and%20Terraform/Document/"
        "green_tripdata_2025-11.parquet"
    )

    engine = create_engine(
        f'postgresql://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_database}'
    )

    print("📥 Lecture du fichier parquet...")
    df = pd.read_parquet(parquet_url)

    print(f"📊 Nombre total de lignes : {len(df)}")

    first = True

    for start in tqdm(range(0, len(df), chunksize)):
        end = start + chunksize
        df_chunk = df.iloc[start:end]

        if first:
            df_chunk.head(0).to_sql(
                name=table_name,
                con=engine,
                if_exists='replace'
            )
            first = False

        df_chunk.to_sql(
            name=table_name,
            con=engine,
            if_exists='append'
        )

    print("✅ Ingestion terminée avec succès")


if __name__ == '__main__':
    run()