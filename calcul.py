import pandas as pd


def calculer_proportions(df, col_surface="Surface (m²)"):
    """Calcule la proportion (%) et le cumul (%) de chaque surface."""
    df = df.copy()
    df = df.dropna(subset=[col_surface])

    total = df[col_surface].sum()
    if total <= 0:
        raise ValueError("La surface totale doit être supérieure à 0.")

    df = df.sort_values(col_surface, ascending=False).reset_index(drop=True)
    df["Proportion (%)"] = (df[col_surface] / total * 100).round(2)
    df["Cumul (%)"] = df["Proportion (%)"].cumsum().round(2)
    return df, total
