import streamlit as st
from auth import login, logout, is_authenticated
from data import load_all_data

def main():
    st.set_page_config(page_title="Maple vs Cashify Analytics", layout="wide")

    if not is_authenticated():
        login()
        return

    st.sidebar.write(f"👤 Logged in as: {st.session_state.get('username')}")
    logout()
    load_all_data()

    page = st.sidebar.radio("Select Page", ["Base Analysis", "Advanced Analytics"])

    if page == "Base Analysis":
        import pages._1_base_analysis as base_analysis
        base_analysis.app()
    else:
        import pages._2_advanced_analytics as advanced_analytics
        advanced_analytics.app()

if __name__ == "__main__":
    main()
