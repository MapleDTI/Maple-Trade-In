import streamlit as st

users = {
    "mahesh_shetty": {"password": "Maple2025!", "name": "Mahesh Shetty"},
    "sandesh_kadam": {"password": "TradeIn@2025", "name": "Sandesh Kadam"},
    "vishwa_sanghavi": {"password": "Analytics#2025", "name": "Vishwa Sanghavi"},
    "kavish_shah": {"password": "Cashify2025$", "name": "Kavish Shah"},
    "hardik_shah": {"password": "Hardik@2025", "name": "Hardik Shah"},
    "manil_shetty": {"password": "Manil@2025", "name": "Manil Shetty"},
}

def is_authenticated():
    return st.session_state.get("authenticated", False)

def login():
    st.sidebar.header("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Login"):
        if username in users and users[username]["password"] == password:
            st.session_state.authenticated = True
            st.session_state.username = username
            st.sidebar.success(f"Welcome, {users[username]['name']}!")
            st.experimental_rerun()
        else:
            st.sidebar.error("Invalid username or password")

def logout():
    if st.sidebar.button("Logout"):
        for key in ['authenticated', 'username', 'maple_data', 'cashify_data', 'spoc_data']:
            if key in st.session_state:
                del st.session_state[key]
        st.sidebar.success("Logged out successfully")
        st.experimental_rerun()
