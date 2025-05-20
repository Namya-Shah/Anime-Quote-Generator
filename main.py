import streamlit as st
import random
import pandas as pd

st.title("Anime Motivator")

data = pd.read_csv("data.csv")

quotes = data["Quote"]
character = data["Character"]
anime = data["Anime"]

if 'index' not in st.session_state:
    st.session_state.index = 0

st.markdown(f"Quote: **{quotes[st.session_state.index]}**")
st.markdown(f"Character: **{character[st.session_state.index]}**")
st.markdown(f"Anime: **{anime[st.session_state.index]}**")

if st.button("Show Next"):
    if st.session_state.index < len(quotes) - 1:
        st.session_state.index += 1
    else:
        st.session_state.index = 0