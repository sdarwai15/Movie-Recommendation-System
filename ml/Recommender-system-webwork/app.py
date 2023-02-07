import requests
import streamlit as st
import pickle
import pandas as pd

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=a0521aa03b16256de0ec2cf36e771203&language=en-US'.format(movie_id))
    data = response.json()
    return 'https://image.tmdb.org/t/p/w780/' + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    recommended_movies =[]
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        # FETCHING POSTER FROM API
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

#https://api.themoviedb.org/3/movie/{movie_id}?api_key=<<api_key>>&language=en-US
#a0521aa03b16256de0ec2cf36e771203



movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

st.title('Movie Recommender System')

similarity = pickle.load((open('similarity.pkl','rb')))

selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    (movies['title'].values))

if st.button('Recommend'):
    names,poster = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
        st.text(names[2])
        st.image(poster[2])
    with col3:
        st.text(names[3])
        st.image(poster[3])
    with col4:
        st.text(names[4])
        st.image(poster[4])
    with col5:
        st.text(names[1])
        st.image(poster[1])

    col6, col7, col8, col9, col10 = st.columns(5)
    with col6:
        st.text(names[5])
        st.image(poster[5])
    with col7:
        st.text(names[6])
        st.image(poster[6])
    with col8:
        st.text(names[7])
        st.image(poster[7])
    with col9:
        st.text(names[8])
        st.image(poster[8])
    with col10:
        st.text(names[9])
        st.image(poster[9])

