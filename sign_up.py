# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 12:05:16 2024

@author: Awarri User
"""

import streamlit as st

def display_page():
    st.title("Sign Up Page")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Submit"):
        st.success("Sign up successful!")
        st.session_state.page = "Home"  # Redirect to Home after signing up
        st.experimental_rerun()
    
    if st.button("Back to Home"):
        st.session_state.page = "Home"
        st.experimental_rerun()
