import streamlit as st 
from PIL import Image
import webbrowser
import spacy 
from textblob import TextBlob
import time 
from gensim.summarization import summarize
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

## Links 
github = 'https://github.com/FadelNasereddin'
linkedin = 'https://www.linkedin.com/in/fadelnasereddin/'

## Images 
fadelImg = Image.open("FadelNewNew.jpg")
mainImg = Image.open('mainPhoto.jpg')


## Readeable Files 
aboutFileMain = open('About.txt','r')
whatFileSide = open('whatIsNLPStop.txt','r')
howFileSide = open('HowToUse.txt','r')

aboutFileMain_read = aboutFileMain.read()
whatFileSide_read = whatFileSide.read()
howFileSide_read = howFileSide.read()



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
    # Hiding Watermarks
    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
    
    # Headers
    st.markdown("# NLP Stop: A Natural Language App :rocket:")
    st.image(mainImg,width=690,caption = 'Art Borrowed From Real Python')
    st.markdown(aboutFileMain_read)
    st.write('')
    st.subheader('**How To Use This Site**')
    st.warning(howFileSide_read)
    st.write("Click on the '>' icon in the top left of the page to find more about NLP Stop")
    st.write('')
    st.subheader("**Serving all your NLP needs here - Check the service you would like to use!**")
    


    # Sidebar
    st.sidebar.title('Developed By 👨‍💻 ')
    st.sidebar.text('Fadel Nasereddin\n4A Management Engineering\nUniversity of Waterloo ')
    st.sidebar.image(fadelImg,width=200)
    st.sidebar.title("What is NLP Stop?")
    st.sidebar.markdown(whatFileSide_read)
    st.sidebar.markdown('# Follow Me :iphone:')
    if st.sidebar.button('LinkedIn'):
        webbrowser.open_new_tab(linkedin)
    if st.sidebar.button('Github'):
        webbrowser.open_new_tab(github)

    # if st.checkbox('yoooooo'):
    # Tokenization
    showTokens = st.checkbox("Show Tokens & Lemma")
    if showTokens:
        st.subheader("Tokenize your text:")
        st.info("Tokenization is the task of chopping up a sequence of text into pieces called tokens")
        tokenMessage = st.text_area("Place the text you would like to tokenize here","Type here...")
        submitButton = st.button("Submit")
        if submitButton:
            tokenResult = textAnalyzer(tokenMessage)
            st.json(tokenResult)
            
    # Named Entity
    entity = st.checkbox("Show general word definitions")
    if entity:
        st.subheader("Extract Entities:")
        entityMessage = st.text_area("Enter Text","Type here...")
        extractButton = st.button("Extract")
        if extractButton:
            entityResult = entityAnalyzer(entityMessage)
            st.json(entityResult) 

    # Sentiment Analysis
    sentiment = st.checkbox("Show The Sentiment of Your Text")
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