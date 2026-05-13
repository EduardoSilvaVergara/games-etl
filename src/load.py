from sqlalchemy import create_engine
from dotenv import load_dotenv
import os


load_dotenv()


def load_to_neon(df):

    try:

        database_url = os.getenv(
            "DATABASE_URL"
        )

        engine = create_engine(database_url)

        df.to_sql(
            "games",
            engine,
            if_exists="replace",
            index=False
        )

        print("Carga completada en Neon")

    except Exception as e:

        print(f"Error en carga: {e}")