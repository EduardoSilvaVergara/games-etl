def structural_validation(df):

    expected_columns = [
        "Title",
        "Release Date",
        "Team",
        "Rating",
        "Times Listed",
        "Number of Reviews",
        "Genres",
        "Summary",
        "Reviews",
        "Plays",
        "Playing",
        "Backlogs",
        "Wishlist"
    ]

    missing_columns = []

    for col in expected_columns:

        if col not in df.columns:
            missing_columns.append(col)

    if missing_columns:

        print("Faltan columnas:")
        print(missing_columns)

        return False

    print("Validación estructural OK")

    return True


def semantic_validation(df):

    errors = []

    # =========================
    # VALIDAR RATING
    # =========================

    invalid_rating = df[
        (df["Rating"] < 0) |
        (df["Rating"] > 10)
    ]

    if len(invalid_rating) > 0:
        errors.append("Ratings fuera de rango")

    # =========================
    # VALIDAR NEGATIVOS
    # =========================

    numeric_columns = [
        "Plays",
        "Playing",
        "Backlogs",
        "Wishlist"
    ]

    for col in numeric_columns:

        invalid = df[df[col] < 0]

        if len(invalid) > 0:
            errors.append(
                f"Valores negativos en {col}"
            )

    # =========================
    # VALIDAR TÍTULOS VACÍOS
    # =========================

    empty_titles = df[
        df["Title"]
        .astype(str)
        .str.strip() == ""
    ]

    if len(empty_titles) > 0:
        errors.append("Existen títulos vacíos")

    # =========================
    # RESULTADO
    # =========================

    if errors:

        print("Errores encontrados:")

        for err in errors:
            print(f"- {err}")

        return False

    print("Validación semántica OK")

    return True