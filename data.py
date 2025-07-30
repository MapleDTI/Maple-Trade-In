import streamlit as st
import pandas as pd
import requests
from io import BytesIO

# ✅ Corrected direct export links to download Excel content
MAPLE_FILE_URL = "https://docs.google.com/spreadsheets/d/1Gq2-JHjJEvQGTNpHIKts5KcLjPZOkzNS/export?format=xlsx"
CASHIFY_FILE_URL = "https://docs.google.com/spreadsheets/d/1d6DzTul-3sadHf1jcXe2ybG8oXLnvjfD/export?format=xlsx"
SPOC_FILE_URL = "https://docs.google.com/spreadsheets/d/1dbWaoHKj2vRASXQ2Zw1yUFgMM3bQXdZg/export?format=xlsx"

@st.cache_data(show_spinner="🔄 Loading data...")
def load_excel_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return pd.read_excel(BytesIO(response.content), engine="openpyxl")
    except Exception as e:
        st.error(f"❌ Failed to load Excel file from:\n{url}\n\nError: {e}")
        return None

def load_all_data():
    if "maple_data" not in st.session_state:
        st.session_state.maple_data = load_excel_from_url(MAPLE_FILE_URL)
        if st.session_state.maple_data is None:
            st.stop()

    if "cashify_data" not in st.session_state:
        st.session_state.cashify_data = load_excel_from_url(CASHIFY_FILE_URL)
        if st.session_state.cashify_data is None:
            st.stop()

    if "spoc_data" not in st.session_state:
        st.session_state.spoc_data = load_excel_from_url(SPOC_FILE_URL)
        if st.session_state.spoc_data is None:
            st.stop()
