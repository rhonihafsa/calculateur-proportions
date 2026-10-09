import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

from calcul import calculer_proportions

st.set_page_config(page_title="Calculateur de proportions")
st.title("Calculateur de proportions de surfaces")
st.caption("Les données ci-dessous sont fictives, à titre d'exemple.")

donnees = pd.DataFrame({
    "Élément": ["Dalle", "Murs", "Escaliers", "Balcons"],
    "Surface (m²)": [120.0, 85.5, 15.0, 22.5],
})

st.subheader("1. Saisie des surfaces")
df_saisie = st.data_editor(donnees, num_rows="dynamic")

if st.button("Calculer"):
    try:
        resultat, total = calculer_proportions(df_saisie)
    except ValueError as erreur:
        st.error(str(erreur))
    else:
        st.subheader("2. Résultats")
        st.metric("Surface totale (m²)", f"{total:.2f}")
        st.dataframe(resultat)

        st.subheader("3. Courbes")
        fig, ax = plt.subplots()
        ax.bar(resultat["Élément"], resultat["Proportion (%)"])
        ax.set_ylabel("Proportion (%)")

        ax2 = ax.twinx()
        ax2.plot(resultat["Élément"], resultat["Cumul (%)"],
                 color="red", marker="o")
        ax2.set_ylabel("Cumul (%)")
        ax2.set_ylim(0, 105)

        st.pyplot(fig)