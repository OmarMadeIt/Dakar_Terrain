import streamlit as st
import pandas as pd

# Données du tableau
data = {
    "Zone": ["Keur Massar", "Almadies 2", "Kounoune", "Sacré Cœur"],
    "Type de papier": ["Bail", "TF", "Délibération", "TF"],
    "Surface (M2)": [150, 170, 300, 160],
    "Contact": ["keurmassar@gmail.com", "keurmassar@gmail.com", "kounoune@gmail.com", "dakar@gmail.com"]
}

df = pd.DataFrame(data)

# Interface utilisateur Streamlit
st.title("Recherche de terrains")
st.sidebar.header("Critères de recherche")

# Filtres pour chaque colonne
zone_filter = st.sidebar.selectbox("Zone", df["Zone"].unique())
type_papier_filter = st.sidebar.selectbox("Type de papier", df["Type de papier"].unique())
surface_filter = st.sidebar.number_input("Surface (M2)", min_value=0)

# Filtrer les données en fonction des critères choisis
filtered_data = df[
    (df["Zone"].str.contains(zone_filter, case=False)) &
    (df["Type de papier"] == type_papier_filter) &
    (df["Surface (M2)"] >= surface_filter)
]

# Afficher les résultats
st.subheader("Résultats de la recherche")

if filtered_data.empty:
    st.info("Nous n'avons pas trouvé de terrain correspondant à vos critères.")
else:
    st.table(filtered_data)
