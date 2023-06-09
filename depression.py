import streamlit as st
import pandas as pd

from empath import Empath
lexicon = Empath()

from LeXmo import LeXmo

from nltk.tokenize import word_tokenize

import string

import contractions
import json

from read_symptoms_lexicon import*
from depressed_analyser import*


#list - important text features for depression identification:
# 1) absolute words - source: https://speakai.co/absolutist-words/
absolutist_word =['absolutely','all','always','complete','completely','constant','constantly','definitely','entire','ever','every','everyone','everything','full','must','never','nothing','totally','whole']
# 2) first person singular & plurl (sometimes we use plural to refer to ourselve)
first_person_singular = ['me','myself', 'i', 'mine', 'my', 'ourself']
first_person_plural = ['we', 'us', 'our', 'ours', 'ourselves']

st.title("Extracting Depression Linguistic Features by using Natural Language Processing")

#user may add text for analysis
st.write("The aim of this tool is to extract depression linguistic features in a depressed text such as depression symptoms, first person singular & plural, absolute words, emotions[LeXmo library] and lexical categories/ topic modelling [Empath library]. Add text and let's start analysing! ")
txt_input = st.text_area('Please add text to analyze', ''' Not wanting to do anything. Not wanting to be anything. Not wanting to be at all. I don't necessarily want to die. I just want to have never existed. ''')
# firstly we need to clean the data. We will be using contractions dictionary. Contractions example: I'll -> I will
#contraction output will be used for pronoun & absolute word identification.
expended_text = contractions.fix(txt_input) 
#st.write(expended_text)
depressed_button = st.button("Analyse this sentence")
#if depressed_button:
#  output_depressed = predict_text(expended_text)
#  st.write(output_depressed)
  

symptom_list = read_file()
#st.write(symptom_list)
#depression_symptoms.hello()
#check if depression signal 1 in input sentence
symptoms = []
for s_list in symptom_list:
  for s in s_list:
      if s in expended_text.lower():
          symptoms.append(s)
          #st.write(s,' signal detected')
          

col1, col2, col3 , col4, col5= st.columns(5)

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
    pronoun_output = st.button("Analyse Pronoun")
    if pronoun_output:
        # we will start with text preprocessing - need to tokenize the sentence into word by word
        #use nltk wordtokenization    
        #remove punctuations
        st.write("Pronoun output")
        txt_input1 = expended_text.translate(str.maketrans('', '', string.punctuation))
        #st.write(txt_input1)
        #set to lower case
        list_word = word_tokenize(txt_input1.lower())
        st.write("number of words in input text: ",len(list_word))
        pronoun_first_person = []
        for word in list_word:
            if word in first_person_singular:
                pronoun_first_person.append(word)
            elif word in first_person_plural:
                pronoun_first_person.append(word)
        st.write("First person pronoun in input text:")
        #st.write(*pronoun_first_person)
        st.write(pronoun_first_person)
        st.write("percentage of fist person words in the input text :", len(pronoun_first_person)/len(list_word))

with col4:
    absolute_output = st.button("Analyse Absolute")
    if absolute_output:
        st.write("Absulte output")
        txt_input1 = expended_text.translate(str.maketrans('', '', string.punctuation))
        #st.write(txt_input1)
        #set to lower case
        list_word = word_tokenize(txt_input1.lower())
        #st.write(list_word)
        st.write("number of words in input text: ",len(list_word))
        absolute_word_list = []
        for word in list_word:
            if word in absolutist_word:
                absolute_word_list.append(word)
        st.write("Absulute words in input text:")
        st.write(absolute_word_list)
        st.write("percentage of fist person words in the input text :", len(absolute_word_list)/len(list_word))
with col5:
    extract_symptoms = st.button("Extract Symptoms")
    if extract_symptoms:
       st.write(symptoms)
    
