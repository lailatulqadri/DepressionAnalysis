import streamlit as st
import pandas as pd

from empath import Empath
lexicon = Empath()

from LeXmo import LeXmo

from nltk.tokenize import word_tokenize

#import string


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
    # we will start with text preprocessing - need to tokenize the sentence into word by word
    #use nltk wordtokenization    
    #remove punctuations
    txt_input1 = txt_input.translate(str.maketrans('', '', string.punctuation))
    #st.write(txt_input1)
    #set to lower case
    list_word = word_tokenize(txt_input1.lower())
    st.write(list_word)
    pronoun_first_person = []
    for word in list_word:
        if word in first_person_singular:
            pronoun_first_person.append(word)
            st.write(word)
        elif word in first_person_plural:
            pronoun_first_person.append(word)
            st.write(word)
            
    st.write(pronoun_first_person)







#st.write('Analyse:', run_sentiment_analysis(txt_input))
