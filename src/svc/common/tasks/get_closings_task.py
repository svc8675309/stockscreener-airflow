from airflow.decorators import task
from svc.common.stocks.stock_data import StockData
from typing import Dict


@task(task_id="get_closings")
def get_closings(ds=None, **kwargs):
    
    # Ultimately we need this as a parameter
    # must match data/exchanges/XXX.csv
    exchange: str = "my_picks"
    
    # Read the tickers
    resource_dir: str = "./data/exchanges"
    with open(f"{resource_dir}/{exchange}.csv") as f:
        lines: list = f.read().splitlines()
    
    ticker_by_chars = StockData.group_by_char(lines)
    
    for tickers in ticker_by_chars:
        print(f"Getting : {tickers}")
        StockData.get_data(tickers=tickers, data_dir=f"./data/ticker/{exchange}", look_back_days=90)
    
    # https://airflow.apache.org/docs/apache-airflow/stable/howto/operator/python.html
    # """Print the Airflow context and ds variable from the context."""
    #pprint(kwargs)
    #print(ds)
    #return "Whatever you return gets printed in the logs"
