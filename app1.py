import pickle
import streamlit as st
import requests
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies_name = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
          # Debugging line
        recommended_movies_name.append(movies.iloc[i[0]].title)
    return recommended_movies_name,
st.header("Movie Recommendation System using ML")
# Ensure these paths are correct
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movie_list = movies['title'].values
selected_movie = st.selectbox(
    'Type or select a movie to get recommendation',
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movies_name= recommend(selected_movie)
    col1,col2,col3,col4,col5= st.columns(5)
    with col1:
        st.text(recommended_movies_name[0])





