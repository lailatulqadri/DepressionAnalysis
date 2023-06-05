import streamlit as st
import pandas as pd
from empath import Empath
lexicon = Empath()

st.title("Extracting Depression Linguistic Features by using Natural Language Processing")

#user may add text for analysis

txt_input = st.text_area('Please add text to analyze', '''
Not wanting to do anything. Not wanting to be anything. Not wanting to be at all. I don't necessarily want to die. I just want to have never existed.
    ''')

def run_empath():
    st.write("Empath")
    output = lexicon.analyze(txt_input, normalize=True)
    #st.write(output)
    df = pd.DataFrame([output])
    st.dataframe(df)
  
    
    
    
st.button("Analyse", on_click = run_empath)

#st.write('Analyse:', run_sentiment_analysis(txt_input))
