def transform_data(df):

    df = df.copy()

    # =========================
    # AÑO DE LANZAMIENTO
    # =========================

    df["Release Year"] = (
        df["Release Date"]
        .dt.year
    )

    # =========================
    # SCORE DE POPULARIDAD
    # =========================

    df["Popularity Score"] = (
        df["Plays"] +
        df["Playing"] +
        df["Wishlist"]
    )

    # =========================
    # CLASIFICACIÓN DEL RATING
    # =========================

    def classify_rating(rating):

        if rating >= 8:
            return "Excelente"

        elif rating >= 6:
            return "Bueno"

        elif rating >= 4:
            return "Regular"

        return "Malo"

    df["Rating Category"] = (
        df["Rating"]
        .apply(classify_rating)
    )

    print("Transformación completada")

    return df