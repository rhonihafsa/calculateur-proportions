import pandas as pd
import pytest

from calcul import calculer_proportions


def test_proportions_et_total():
    df = pd.DataFrame({
        "Élément": ["A", "B"],
        "Surface (m²)": [75.0, 25.0],
    })
    resultat, total = calculer_proportions(df)

    assert total == 100.0
    assert resultat.loc[0, "Proportion (%)"] == 75.0
    assert resultat["Cumul (%)"].iloc[-1] == 100.0


def test_surface_totale_nulle():
    df = pd.DataFrame({
        "Élément": ["A"],
        "Surface (m²)": [0.0],
    })
    with pytest.raises(ValueError):
        calculer_proportions(df)