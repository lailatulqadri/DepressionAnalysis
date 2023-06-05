import streamlit as st
import pandas as pd

st.title("Extracting Depression Linguistic Features by using Natural Language Processing")

#user may add text for analysis

txt_input = st.text_area('Please add text to analyze', '''
    Example: It was the best of times, it was the worst of times, it was
    the age of wisdom, it was the age of foolishness, it was
    the epoch of belief, it was the epoch of incredulity, it
    was the season of Light, it was the season of Darkness, it
    was the spring of hope, it was the winter of despair, (...)
    ''')

def run_empath():
    st.write("Empath")
st.button("Analyse", on_click = run_empath)

#st.write('Analyse:', run_sentiment_analysis(txt_input))
