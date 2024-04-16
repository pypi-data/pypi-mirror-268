import os
from pathlib import Path

import pandas as pd
import requests


def fetch_data(
    base_url: str,
    output_path: str,
    columns: list[str],
) -> pd.DataFrame:
    """
    Purpose:
    Download dataset from the specified url and save it to the provided path.

    This function is capable of downloading datasets from exoplanetarchive.

    The dataset is saved under data/raw/Y-M-D_planet-systems.csv,
    along with its processed version under data/processed/planet-systems.csv by default.

    Documentation for constructing a TPA call to retrieve the dataset:
    https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=PS

    Parameters:
    - base_url (str): The URL from which to fetch the data.
    - output_path (str): The file path where the fetched raw data will be saved. This 
        specifies the location on the local filesystem where the downloaded dataset should be stored.
    - columns (list[str]): A list of column names to be fetched from the dataset. 
        This parameter defines which attributes or fields of the data should be included 
        in the query and subsequently in the returned DataFrame. For instance, if accessing 
        a database with many columns, this list explicitly states which columns to retrieve, 
        optimizing the fetching process and ensuring that only relevant data is loaded.
        
    Returns:
    - pd.DataFrame: A pandas DataFrame containing the fetched data.

    """
    # define the directories where we will store the data
    dataset_name = "planet-systems"
    raw_data_dir = Path("data") / "raw"
    default_out_path = raw_data_dir / f"{dataset_name}.csv"
    raw_data_path = output_path or default_out_path

    # make directory where we store our raw data
    os.makedirs(raw_data_dir, exist_ok=True)

    # download the raw data as CSV under the raw data directory using a TPA query
    base_url = base_url or "https://exoplanetarchive.ipac.caltech.edu"
    query = f"select+{','.join([column for column in columns])}+from+ps"
    format = "csv"
    url = f"{base_url}/TAP/sync?query={query}&format={format}"

    print(f"Downloading Planet Systems dataset from {url}\nunder {raw_data_path}")

    # send an HTTP request to the url
    try:
        response = requests.get(url)
        raw_data = response.content
    except requests.exceptions.RequestException:
        print(f"ERROR: Error while trying to download the dataset from {url}")
        raise

    # write downloaded content into a file under the raw data directory
    with open(raw_data_path, "wb") as f:
        f.write(raw_data)

    # df holds the expolanet dataset as a DataFrame object
    df = pd.read_csv(raw_data_path)

    print(f"Successfully loaded dataset from {raw_data_path}")

    return df
