import pandas as pd


def clean_data(df):

    df = df.copy()

    # =========================
    # ELIMINAR DUPLICADOS
    # =========================

    df = df.drop_duplicates()

    # =========================
    # LIMPIEZA DE TEXTO
    # =========================

    text_columns = [
        "Title",
        "Team",
        "Genres",
        "Summary",
        "Reviews"
    ]

    for col in text_columns:

        df[col] = (
            df[col]
            .astype(str)
            .str.strip()
        )

    # =========================
    # LIMPIAR COLUMNAS NUMÉRICAS
    # =========================

    numeric_columns = [
        "Rating",
        "Times Listed",
        "Number of Reviews",
        "Plays",
        "Playing",
        "Backlogs",
        "Wishlist"
    ]

    for col in numeric_columns:

        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

    # =========================
    # REEMPLAZAR NULOS
    # =========================

    for col in numeric_columns:

        median = df[col].median()

        df[col] = df[col].fillna(median)

    # =========================
    # FECHAS
    # =========================

    df["Release Date"] = pd.to_datetime(
        df["Release Date"],
        errors="coerce"
    )

    # Eliminar fechas inválidas
    df = df.dropna(subset=["Release Date"])

    print("Limpieza completada")

    return df