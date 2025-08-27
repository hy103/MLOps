import streamlit as st 
import pickle
import pandas as pd
import requests


def fetch_poster_from_movie_id(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=908da38b23b6e6ee5847cd20f17100eb&language=en-US'.format(movie_id))
    data = response.json()
    return 'https://image.tmdb.org/t/p/w500' + data['poster_path']

def recommend(movie_name, movies_list):
    recommended_movies_list = []
    similarity_matrix = (movies_list[movies_list['title'] ==movie_name].index[0])
    top5_movies_list = sorted(list(enumerate(similarity[similarity_matrix])), reverse= True, key = lambda x : x[1])[1:6]

    poster_list = []
    for i in top5_movies_list:
        movie_id = movies_list.iloc[i[0]].movie_id
        recommended_movies_list.append(movies_list.iloc[i[0]].title)
        poster_list.append(fetch_poster_from_movie_id(movie_id))
    
    return recommended_movies_list, poster_list
movies = pickle.load(open('movie_dict.pkl', 'rb'))
movies_list = pd.DataFrame(movies)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Movie Recommendation System")
movie_option = st.selectbox('Pick a movie',movies_list['title'].values)

if st.button("Recommend"):
    recommendations,posters = recommend(movie_option, movies_list)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommendations[0])
        st.image(posters[0])

    with col2:
        st.text(recommendations[1])
        st.image(posters[1])
    with col3:
        st.text(recommendations[2])
        st.image(posters[2])
    with col4:
        st.text(recommendations[3])
        st.image(posters[3])
    with col5:
        st.text(recommendations[4])
        st.image(posters[4])


        
