import streamlit as st 
import spacy 
from textblob import TextBlob
import time 
from gensim.summarization import summarize
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

## Readeable Files 
f= open('About.txt','r')
yo = f.read()

## Summary Function
def summaryAnalyzer(doc):
    parser = PlaintextParser.from_string(doc,Tokenizer("english"))
    lex_summarizer = LexRankSummarizer()
    summary = lex_summarizer(parser.document,3)
    summary_list = [str(sentence) for sentence in summary]
    result = ' '.join(summary_list)
    return result 

## Tokenizer Function
def textAnalyzer(myText):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(myText)
    allData = [('Token:{},\n lemma:{}'.format(token.text,token.lemma_)) for token in doc]
    return allData

## Entity Function
def entityAnalyzer(myText):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(myText)
    entities = [(entity.text,entity.label_) for entity in doc.ents]
    return entities

# Main Method
def main():
    # Headers
    st.title("NLP Stop - A Natural Language WebApp")
    st.subheader(yo)
    st.subheader("Serving all your NLP needs here!")


    # Sidebar
    st.sidebar.header('Developed By:')
    st.sidebar.text('Fadel Nasereddin\n4A Management Engineering')
    st.sidebar.header('How to Use this site')
    st.sidebar.info("TODO")

    if st.checkbox('yoooooo'):
        # Tokenization
        showTokens = st.checkbox("Show Tokens & Lemma")
        if showTokens:
            st.subheader("Tokenize your text")
            st.info("Tokenization is the task of chopping up a sequence of text into pieces called tokens")
            tokenMessage = st.text_area("Place the text you would like to tokenize here","Type here...")
            submitButton = st.button("Submit")
            if submitButton:
                tokenResult = textAnalyzer(tokenMessage)
                st.json(tokenResult)
                
        # Named Entity
        entity = st.checkbox("Show general word definitions")
        if entity:
            st.subheader("Extract Entities")
            entityMessage = st.text_area("Enter Text","Type here...")
            extractButton = st.button("Extract")
            if extractButton:
                entityResult = entityAnalyzer(entityMessage)
                st.json(entityResult) 

        # Sentiment Analysis
        sentiment = st.checkbox("Show The Sentiment of Your Text!")
        if sentiment:
            st.subheader("Sentiment Analysis:")
            sentimentMessage = st.text_area("Analyze the sentiment of your text here","Type here...")
            if st.button("Analyze Sentiment"):
                blob = TextBlob(sentimentMessage)
                sentimentResult = blob.sentiment
                st.success(sentimentResult)

        # Text Summarization 
        if st.checkbox("Summarize a long paragraph"):
            summarizerList=['gensim','sumy']
            summarizerSelect = st.selectbox("Select Summarizer:",summarizerList)
            st.subheader("Sumarize your text:")
            summaryMessage = st.text_area("Place long essay/pargraph here","Type here...")
            if st.button("Summarize"):
                if summarizerSelect =='gensim':
                    summaryResult= summarize(summaryMessage)
                    with st.spinner("Summarizing your text..."):
                        time.sleep(3)
                    st.success("Finished!")


                elif summarizerSelect =="sumy":
                    summaryResult= summaryAnalyzer(summaryMessage)
                    with st.spinner("Summarizing your text..."):
                        time.sleep(3)
                    st.success("Finished!")
                

                else:
                    st.warning("Invalid selection. Using Default Summarizer (gensim)")
                    summaryResult= summarize(summaryMessage)

                st.info(summaryResult)
                


if __name__ == '__main__':
    main()