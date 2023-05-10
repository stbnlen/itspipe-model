import pandas as pd
from utils.clean_dataframe import clean_dataframe

def load_data(file_path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None
    df = clean_dataframe(df)
    return df