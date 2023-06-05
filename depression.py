import streamlit as st
import pandas as pd

from empath import Empath
lexicon = Empath()


st.title("Extracting Depression Linguistic Features by using Natural Language Processing")
container1 = st.container()
#user may add text for analysis
container1.text("Let's play with empath library to extract general linguistic features from text")
txt_input = container1.text_area('Please add text to analyze', ''' Not wanting to do anything. Not wanting to be anything. Not wanting to be at all. I don't necessarily want to die. I just want to have never existed.
    ''')

container2 = st.container()
def run_empath():
    container2.write("Empath")
    output = lexicon.analyze(txt_input, normalize=True)
    #st.write(output)
    df = pd.DataFrame([output])
    container2.dataframe(df)
    #st.expender(st.write("testing"))
  
    
    
    
st.button("Analyse", on_click = run_empath)



#st.write('Analyse:', run_sentiment_analysis(txt_input))
