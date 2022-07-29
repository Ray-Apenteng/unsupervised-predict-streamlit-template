"""

    Content-based filtering for item recommendation.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: You are required to extend this baseline algorithm to enable more
    efficient and accurate computation of recommendations.

    !! You must not change the name and signature (arguments) of the
    prediction function, `content_model` !!

    You must however change its contents (i.e. add your own content-based
    filtering algorithm), as well as altering/adding any other functions
    as part of your improvement.

    ---------------------------------------------------------------------

    Description: Provided within this file is a baseline content-based
    filtering algorithm for rating predictions on Movie data.

"""

# Script dependencies
import os
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import pickle

# Importing data
movies = pd.read_csv('resources/data/movie_key_words.csv', sep = ',')
onlyfiles = next(os.walk('resources/data/'))[2]
lm_loaded = pickle.load(open("resources/models/lm1_df.pkl", 'rb'))

# Load all rating csv files 
# rtng_csv = []
# for i, file_name in enumerate(onlyfiles):
#     directory = 'resources/data/ratings/'+file_name
#     df = pd.read_csv(directory)
#     rtng_csv.append(df)

# # Merge the prediction files
# ratings = pd.concat(rtng_csv, ignore_index=True)
# movies.dropna(inplace=True)

# def data_preprocessing(subset_size):
#     """Prepare data for use within Content filtering algorithm.

#     Parameters
#     ----------
#     subset_size : int
#         Number of movies to use within the algorithm.

#     Returns
#     -------
#     Pandas Dataframe
#         Subset of movies selected for content-based filtering.

#     """
    
#     # Subset of the data
#     movies_subset = movies[:subset_size]
#     return movies_subset

# !! DO NOT CHANGE THIS FUNCTION SIGNATURE !!
# You are, however, encouraged to change its content.  
def content_model(movie_list,top_n=10):
    """Performs Content filtering based upon a list of movies supplied
       by the app user.

    Parameters
    ----------
    movie_list : list (str)
        Favorite movies chosen by the app user.
    top_n : type
        Number of top recommendations to return to the user.

    Returns
    -------
    list (str)
        Titles of the top-n movie recommendations to the user.

    """
    # Initializing the empty list of recommended movies
    # recommended_movies = []
    # data = data_preprocessing(40000)
    # # Instantiating and generating the count matrix
    # count_vec = TfidfVectorizer(analyzer='word', ngram_range=(1,2),
    #                  min_df=0, stop_words='english')


    m1, m2, m3= movie_list
# #     Initializing the empty list of recommended movies
#     recommended_movies = []
#     data = data_preprocessing(27000)
# #     Instantiating and generating the count matrix
#     count_vec = CountVectorizer()
#     count_matrix = lm_loaded
#   indices = pd.Series(data['title'])
    a1= np.array(lm_loaded.loc[m1]).reshape(1,-1)
    a2= np.array(lm_loaded.loc[m2]).reshape(1,-1)
    a3= np.array(lm_loaded.loc[m3]).reshape(1,-1)
    # Getting the index of the movie that matches the title
#     idx_1 = indices[indices == movie_list[0]].index[0]
#     idx_2 = indices[indices == movie_list[1]].index[0]
#     idx_3 = indices[indices == movie_list[2]].index[0]
    
    # Creating a Series with the similarity scores in descending order
#     rank_1 = cosine_sim[idx_1]
#     rank_2 = cosine_sim[idx_2]
#     rank_3 = cosine_sim[idx_3]
    rank_1= cosine_similarity(lm_loaded, a1).reshape(-1)
    rank_2= cosine_similarity(lm_loaded, a2).reshape(-1)
    rank_3= cosine_similarity(lm_loaded, a3).reshape(-1)
    # Calculating the scores
#     score_series_1 = pd.Series(rank_1).sort_values(ascending = False)
#     score_series_2 = pd.Series(rank_2).sort_values(ascending = False)
#     score_series_3 = pd.Series(rank_3).sort_values(ascending = False)
    dictDf1= {'content':rank_1}
    dictDf2= {'content':rank_2}
    dictDf3= {'content':rank_3}
    # Getting the indexes of the 10 most similar movies
#     listings = score_series_1.append(score_series_1).append(score_series_3).sort_values(ascending = False)
    similar_movies1= pd.DataFrame(dictDf1, index=lm_loaded.index)
    similar_movies2= pd.DataFrame(dictDf2, index=lm_loaded.index)
    similar_movies3= pd.DataFrame(dictDf3, index=lm_loaded.index)

    similar_movies= pd.concat([similar_movies1, similar_movies2, similar_movies3], axis=0)
    similar_movies= similar_movies.reset_index()
    similar_movies= similar_movies.drop_duplicates(subset='index', keep='first')
    similar_movies= similar_movies.sort_values('content', ascending=False)
    
    # Store movie names
    recommended_movies = []
#     # Appending the names of movies
#     top_50_indexes = list(listings.iloc[1:50].index)
#     # Removing chosen movies
#     top_indexes = np.setdiff1d(top_50_indexes,[idx_1,idx_2,idx_3])
    n= 0
    for i in similar_movies['index'][:50]:
        if i not in movie_list:
            recommended_movies.append(i)
    recommended_movies= recommended_movies[:10]
    return recommended_movies
