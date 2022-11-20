# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 12:05:21 2022

@author: PIHOUSE
"""
from datetime import datetime
import streamlit as st
import pandas as pd
import numpy as np
import time
#from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
stop_factory = StopWordRemoverFactory()

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

def space(num_lines=1):
    """Adds empty lines to the Streamlit app."""
    for _ in range(num_lines):
        st.write("")
st.set_page_config(layout="centered", page_title="sns driven products app")

#tw_image = np.array(Image.open("D:/TSDN22/twitter.png"))

topics = ["alat olahraga","alat yoga", "sneakers ventela", "iphone14","sneakers compass"]
text_input = st.selectbox("Pilih topik...",topics)
space(1)
# CSS to inject contained in a string
hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)

#toped = pd.read_csv("D:/TSDN22/tokopedia.csv")
#shopi = pd.read_csv("D:/TSDN22/shopi.csv")
    
tweets = pd.read_csv("datas/contoh_data.csv", encoding_errors='ignore')
tweets = tweets.drop(tweets.columns[[0]], axis=1)
st.dataframe(tweets)
if text_input:
    with st.spinner('Wait for it...'):
        tweets = tweets[tweets['tweet'].str.contains(text_input)] 
        st.header("Total "+str(tweets.shape[0])+" tweets")
        st.table(tweets.head())

def cloud(text, max_word, max_font, random):
    wc = WordCloud(background_color="white", colormap="hot", max_words=max_word,max_font_size=max_font, random_state=random)

    # generate word cloud
    wc.generate(text)
    plt.imshow(wc)
    plt.axis("off")
    plt.show()
    #st.pyplot()
    #tweets["content"].str.cat(sep=' ')

from PIL import Image
image = Image.open('images/wordcloud_result.jpeg')

st.image(image, caption='Wordcloud of the Tweets')
# st.image(cloud(tweets["tweet"].str.cat(sep=' '), 20, 90, 2))
