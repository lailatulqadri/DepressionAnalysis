import streamlit as st
import pandas as pd

from empath import Empath
lexicon = Empath()

from LeXmo import LeXmo

#list - important text features for depression identification:
# 1) absolute words 
absolutist_word =['absolutely','all','always','complete','completelt','constant','constantly','definitely','entire','ever','every','everyone','everything','full','must','never','nothing','totally','whole']
# 2) first person singular & plurl (sometimes we use plural to refer to ourselve)
first_person_singular = ['me','myself', 'i', 'mine', 'my', 'ourself']
first_person_plural = ['we', 'us', 'our', 'ours', 'ourselves']



st.title("Extracting Depression Linguistic Features by using Natural Language Processing")
#user may add text for analysis
st.text("Let's play with empath library to extract general linguistic features from text")
txt_input = st.text_area('Please add text to analyze', ''' Not wanting to do anything. Not wanting to be anything. Not wanting to be at all. I don't necessarily want to die. I just want to have never existed.
    ''')

col1, col2, col3 = st.columns(3)

with col1:
    empath_output = st.button("Analyse Empath")
    if empath_output:
        st.write("Empath Output")
        output = lexicon.analyze(txt_input, normalize=True)
        #st.write(output)
        df = pd.DataFrame([output])
        st.dataframe(df.T)

with col2:
    emotion_output = st.button("Analyse Emotion")
    if emotion_output:
        st.write("Emotion Output")
        emo=LeXmo.LeXmo(txt_input)
        df_emo = pd.DataFrame([emo])
        st.dataframe(df_emo.T)

with col3:
    prnoun_output = st.button("Analyse Pronoun")
    st.write("In progress")







#st.write('Analyse:', run_sentiment_analysis(txt_input))
