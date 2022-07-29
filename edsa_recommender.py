"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","Overview","About"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('First Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                #try:
                with st.spinner('Crunching the numbers...'):
                    top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                st.title("We think you'll like:")
                for i,j in enumerate(top_recommendations):
                    st.subheader(str(i+1)+'. '+j)
                # except:
                #     st.error("Oops! Looks like this algorithm does't work.\
                #               We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Overview":
        st.title("Introduction To Recommender Systems")
        st.image(('resources/imgs/recommm.png'),caption=None)
        st.markdown(open('resources/markdowns/intro rec.md').read())
        st.write("To read more on recommender systems, click [here](https://bit.ly/3Jhu0Td)")
        st.markdown(open('resources/markdowns/youtube.md').read())
        # st.image(('resources/imgs/Colab based.png'),caption=None)
        st.video("https://www.youtube.com/watch?v=Eeg1DEeWUjA")

    
    # Building out the "About" page
    if page_selection == "About":
        st.title("About Us:")

        st.markdown(open("resources/markdowns/VIMI.md").read())

        st.markdown(open("resources/markdowns/meettheteam.md").read())

        st.image(('resources/imgs/Ubong Ben.jpg'),caption=None, width=250)
        st.info("Ubong Ben - BUSINESS ANALYST")

        st.image(('resources/imgs/Me wlp.jpg'),caption=None, width=250)
        st.info("Raymond Apenteng - BUSINESS STRATEGIST")

        st.image(('resources/imgs/David Kambo.jpg'),caption=None, width=250)
        st.info("David Kambo - DATA SCIENTIST")

        st.image(('resources/imgs/McDonald.JPG'),caption=None, width=250)
        st.info("Daniel McDonald - MACNINE LEARNING SPECIALIST")

        st.image(('resources/imgs/Ekele1.png'),caption=None, width=250)
        st.info("Ekele Dinneya-Onuoha - SALES MANAGER")

        


    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
