# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 12:05:12 2024

@author: Awarri User
"""

import streamlit as st

def display_page():
    st.title("Log In Page")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Log In"):
        st.success("Log in successful!")
        st.session_state.page = "Home"  # Redirect to Home after logging in
        st.experimental_rerun()
    
    if st.button("Back to Home"):
        st.session_state.page = "Home"
        st.experimental_rerun()
