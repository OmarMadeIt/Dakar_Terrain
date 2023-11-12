import streamlit as st
import pandas as pd

# Données du tableau
data = {
    "Zone": ["Keur Massar", "Almadies 2", "Kounoune", "Sacre Cœur"],
    "Type de papier": ["Bail", "TF", "Délibération", "TF"],
    "Surface (M2)": [150, 170, 300, 160],
    "Contact": ["338320001", "338320002", "338320003", "338320004"]
}

df = pd.DataFrame(data)

st.set_page_config(page_title='Moma Immobilier', page_icon=":tada:", layout='wide')
# Interface utilisateur Streamlit
st.title("Recherche de terrains :house:")
st.sidebar.header("Criteres de recherche")

# Filtres pour chaque colonne
zone_filter = st.sidebar.selectbox("Zone", df["Zone"].unique())
type_papier_filter = st.sidebar.selectbox("Type de papier", df["Type de papier"].unique())
surface_filter = st.sidebar.number_input("Surface (M2)", min_value=0)

# Ajouter un bouton "Rechercher"
button_search = st.sidebar.button("Rechercher")

# Filtrer les données en fonction des critères choisis
if button_search:
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
