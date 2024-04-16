from colorama import Fore
from pathlib import Path
from .ultilities import make_dir


class DataPipeLine:
    def __init__(self, query: str):
        self.query = query
        self.status = f'{Fore.LIGHTBLUE_EX}🤖 JDBC:{Fore.RESET}'

    def run_presto_to_df(
            self,
            use_polars: bool = True,
            save_path: Path = None,
            verbose: bool = True
    ):
        from concurrent.futures import ThreadPoolExecutor
        from time import sleep
        from datetime import datetime
        import trino
        import os
        import pandas as pd
        import polars as pl
        from tqdm import tqdm

        # connection
        username, password = os.environ['PRESTO_USER'], os.environ['PRESTO_PASSWORD']
        conn = trino.dbapi.connect(
            host='presto-secure.data-infra.shopee.io',
            port=443,
            user=username,
            catalog='hive',
            http_scheme='https',
            source=f'(50)-(vnbi-dev)-({username})-(jdbc)-({username})-(SG)',
            auth=trino.auth.BasicAuthentication(username, password)
        )
        cur = conn.cursor()

        # verbose
        start = datetime.now()
        print(f"{self.status} Start to query {start.strftime("%Y-%m-%d %H:%M:%S")}")
        if verbose:
            thread = ThreadPoolExecutor(1)
            async_result = thread.submit(cur.execute, self.query)

            bar_queue = tqdm()
            while not async_result.done():
                memory = cur.stats.get('peakMemoryBytes', 0) * 10 ** -9
                perc = 0
                stt = cur.stats.get('state', '')
                if stt == "RUNNING":
                    perc = round((cur.stats.get('completedSplits', 0) * 100.0) / (cur.stats.get('totalSplits', 0)), 2)
                status = f"🤖 JDBC Status: {stt} {perc}%, Memory {memory:,.0f}GB"
                bar_queue.set_description(status)
                bar_queue.update(1)
                sleep(5)
            bar_queue.close()
        else:
            cur.execute(self.query)
        records = cur.fetchall()

        # result
        columns = [i[0] for i in cur.description]
        if use_polars:
            df = pl.DataFrame(records, orient='row', schema=columns)
        else:
            df = pd.DataFrame(records, columns=columns)

        if save_path:
            make_dir(save_path.parent)
            if use_polars:
                df.write_parquet(save_path)
            else:
                df.to_parquet(save_path, index=False, compression='zstd')

        end = datetime.now()
        print(
            f"{self.status} Finish {end.strftime("%Y-%m-%d %H:%M:%S")} in {(end - start).total_seconds()}s \n"
            f"{self.status} Data Shape: {df.shape}"
        )
        return df
