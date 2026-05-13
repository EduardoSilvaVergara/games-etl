import pandas as pd


def ingest_data(path):

    try:

        df = pd.read_csv(path)

        print("Ingesta completada")
        print(df.head())

        return df

    except Exception as e:

        print(f"Error en ingesta: {e}")
        return None