# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 10:34:11 2024

@author: Awarri User
"""
import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Health Streamlit App", layout="wide")

# Initialize session state for page tracking
if 'page' not in st.session_state:
    st.session_state.page = 'Home'

# Display the selected page
if st.session_state.page == 'Home':
    st.title("Home Page")
    st.write("Welcome to the Multi-Page Streamlit App!")
    
    if st.button("Sign Up"):
        st.session_state.page = "Sign Up"
        st.experimental_rerun()  # Reload to update page
    if st.button("Log In"):
        st.session_state.page = "Log In"
        st.experimental_rerun()  # Reload to update page

elif st.session_state.page == 'Log In':
    import log_in  # Ensure this file exists
    log_in.display_page()

elif st.session_state.page == 'Sign Up':
    import sign_up  # Ensure this file exists
    sign_up.display_page()