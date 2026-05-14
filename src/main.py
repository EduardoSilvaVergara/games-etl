from ingest import ingest_data
from clean import clean_data
from transform import transform_data
from validate import (
    structural_validation,
    semantic_validation
)
from load import load_to_neon


def main():

    # =========================
    # INGESTA
    # =========================

    df = ingest_data("data/games.csv")

    if df is None:
        return

    # =========================
    # VALIDACIÓN ESTRUCTURAL
    # =========================

    if not structural_validation(df):
        return

    # =========================
    # LIMPIEZA
    # =========================

    df_clean = clean_data(df)

    # =========================
    # TRANSFORMACIÓN
    # =========================

    df_transformed = transform_data(
        df_clean
    )

    # =========================
    # VALIDACIÓN SEMÁNTICA
    # =========================

    if not semantic_validation(
        df_transformed
    ):
        return

    # =========================
    # EXPORTAR CSV LIMPIO
    # =========================

    df_transformed.to_csv(
        "data/games_cleaned.csv",
        index=False
    )

    print(
        "CSV limpio generado en data/games_cleaned.csv"
    )

    # =========================
    # LOAD
    # =========================

    load_to_neon(df_transformed)

    print("Pipeline ETL terminado")


if __name__ == "__main__":
    main()