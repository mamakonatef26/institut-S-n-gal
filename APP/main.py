import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(layout="wide")
st.title("Cartographie des Instituts et Réseaux au Sénégal")

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "index.html")

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        html_data = f.read()
        components.html(html_data, height=700, scrolling=True)
except FileNotFoundError:
    st.error("Le fichier index.html est introuvable dans le dossier APP.")
