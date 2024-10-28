# streamlit app to demonstrate all the functions

import streamlit as st
from Task1.main import get_random_cocktail
from TaskA.main import suggest_cocktail
from TaskB.testui import visualize_cocktail_recipe


get_random_cocktail()

def main():
    st.title("Leaf Space Assessment")
    st.sidebar.title("Task 1")
    st.sidebar.title("Task A")
    st.sidebar.title("Task B")
