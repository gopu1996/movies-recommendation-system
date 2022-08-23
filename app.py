import streamlit as st
import pickle
import requests
import json

def fetch_poster(movie_id):
    res = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=05f27b6fea5cf15605855be9cbe7b0a0&language=en-US'.format(movie_id))
    json_data = json.loads(res.text)
    path = "https://image.tmdb.org/t/p/w500" + str(json_data.get("poster_path"))
    return path

def fetch_movies_overview(movie_id):
    res = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=05f27b6fea5cf15605855be9cbe7b0a0&language=en-US'.format(movie_id))
    json_data = json.loads(res.text)
    return  json_data.get("overview")

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])  # for index we are using this enumerate
    recommend_movies = []
    recommend_movies_poster = []
    movies_overview = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_movies_poster.append(fetch_poster(movie_id))
        movies_overview.append(fetch_movies_overview(movie_id))
    return recommend_movies,recommend_movies_poster,movies_overview



st.title('Movies Recommender System')

movies = pickle.load(open('movies.pkl','rb'))
movies_list = movies['title'].values

similarity = pickle.load(open('similarity.pkl','rb'))

selected_movie_name = st.selectbox(
    "Type or select a movie from the dropdown",
    movies_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters, movies_overview = recommend(selected_movie_name)
    print(movies_overview)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(recommended_movie_posters[0])
        st.text(recommended_movie_names[0])
        st.text(movies_overview[0])
    with col2:
        st.image(recommended_movie_posters[1])
        st.text(recommended_movie_names[1])
        st.text(movies_overview[1])
    with col3:
        st.image(recommended_movie_posters[2])
        st.text(recommended_movie_names[2])
        st.text(movies_overview[2])
    with col4:
        st.image(recommended_movie_posters[3])
        st.text(recommended_movie_names[3])
        st.text(movies_overview[3])
    with col5:
        st.image(recommended_movie_posters[4])
        st.text(recommended_movie_names[4])
        st.text(movies_overview[4])
