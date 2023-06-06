import streamlit as st
import pandas as pd

from empath import Empath
lexicon = Empath()

from LeXmo import LeXmo


st.title("Extracting Depression Linguistic Features by using Natural Language Processing")
#user may add text for analysis
st.text("Let's play with empath library to extract general linguistic features from text")
txt_input = st.text_area('Please add text to analyze', ''' Not wanting to do anything. Not wanting to be anything. Not wanting to be at all. I don't necessarily want to die. I just want to have never existed.
    ''')

 
empath_output = st.button("Analyse Empath")
emotion_output = st.button("Analyse Emotion")

if empath_output:
    st.write("Empath Output")
    output = lexicon.analyze(txt_input, normalize=True)
    #st.write(output)
    df = pd.DataFrame([output])
    st.dataframe(df.T)

if emotion_output:
    st.write("Emotion Output")
    emo=LeXmo.LeXmo(txt_input)
    df_emo = pd.DataFrame([emo])
    st.dataframe(df_emo.T)




#st.write('Analyse:', run_sentiment_analysis(txt_input))
