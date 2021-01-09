import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import base64 # for enabling CSV download

st.title('NBA Player Stats')

st.markdown(""" This app performs simple webscraping of NBA player stats data!! """)

st.sidebar.header('User Input Features // Sidebar')
selectedYear = st.sidebar.selectbox('Select a Year', list(reversed(range(1950,2020))))

# Web Scraping of NBA players
@st.cache
def load_data(year):
    url = "https://www.basketball-reference.com/leagues/NBA_" + str(year) + "_per_game.html"
    html = pd.read_html(url, header = 0)
    df = html[0]

    return df

