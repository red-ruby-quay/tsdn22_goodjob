# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 12:05:21 2022

@author: PIHOUSE
"""
from datetime import datetime
#import streamlit as st
import pandas as pd
import numpy as np
import time
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt


tweets = pd.read_csv("D:/TSDN22/sneakers_tw.csv", encoding_errors='ignore')

def cloud( text, max_word, max_font, random):
    wc = WordCloud(background_color="white", colormap="hot", max_words=max_word,max_font_size=max_font, random_state=random)

    # generate word cloud
    wc.generate(text)
    plt.imshow(wc)
    plt.axis("off")
    plt.show()
    #st.pyplot()
    #tweets["content"].str.cat(sep=' ')
cloud(tweets["tweet"].str.cat(sep=' '), 20, 90, 2)