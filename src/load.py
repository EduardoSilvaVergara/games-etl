from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os


load_dotenv()


def load_to_neon(df):

    try:

        # =========================
        # CONEXIÓN
        # =========================

        database_url = os.getenv(
            "DATABASE_URL"
        )

        engine = create_engine(
            database_url
        )

        # =========================
        # ELIMINAR TABLA SI EXISTE
        # =========================

        with engine.connect() as conn:

            conn.execute(
                text(
                    """
                    DROP TABLE IF EXISTS games
                    """
                )
            )

            conn.commit()

        print(
            "Tabla anterior eliminada"
        )

        # =========================
        # CARGAR NUEVA TABLA
        # =========================

        df.to_sql(
            "games",
            engine,
            index=False
        )

        print(
            "Datos cargados correctamente a Neon"
        )

    except Exception as e:

        print(
            f"Error cargando datos: {e}"
        )