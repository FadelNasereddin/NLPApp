import streamlit as st 
import spacy 
from textblob import TextBlob
import time 

def textAnalyzer(myText):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(myText)
    allData = [('Token:{},\n lemma:{}'.format(token.text,token.lemma_)) for token in doc]
    return allData


def main():
    # Headers
    st.title("Fadel's NLP Application")
    st.subheader("Serving all your NLP needs here!")


    # Sidebar
    st.sidebar.header('About this site')
    st.write('TODO')
    st.sidebar.header('How to Use this site')
    st.sidebar.info("TODO")

    # Tokenization
    showTokens = st.checkbox("Show Tokens & Lemma")
    
    
    if showTokens:
        st.subheader("Tokenize your text")
        st.info("Tokenization is ...")
        message = st.text_area("Enter your desired text:","Type here...")
        submitButton = st.button("Submit")
        if submitButton:
            result = textAnalyzer(message)
            st.json(result)
            



    # Sentiment Analysis 

    # Summary


if __name__ == '__main__':
    main()