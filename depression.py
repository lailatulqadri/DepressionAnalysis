import streamlit as st
import pandas as pd

from empath import Empath
lexicon = Empath()


st.title("Extracting Depression Linguistic Features by using Natural Language Processing")
#user may add text for analysis
st.text("Let's play with empath library to extract general linguistic features from text")
txt_input = st.text_area('Please add text to analyze', ''' Not wanting to do anything. Not wanting to be anything. Not wanting to be at all. I don't necessarily want to die. I just want to have never existed.
    ''')

  

empath_output = st.button("Empath Analyse")

if empath_output:
    st.write("Empath Output")
    output = lexicon.analyze(txt_input, normalize=True)
    #st.write(output)
    df = pd.DataFrame([output])
    st.dataframe(df)
    




#st.write('Analyse:', run_sentiment_analysis(txt_input))
