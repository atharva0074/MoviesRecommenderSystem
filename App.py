import streamlit as st
import pandas as pd
import pickle
import requests
import gdown
def download_file(url, filename):
    try:
       
        gdown.download(url, filename, quiet=False)

    except Exception as e:
        st.error(f"Failed to download file: {e}")


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_lists = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies=[]
    recommended_movies_posters =[]
    for idx in movies_lists:
        movie_id =movies.iloc[idx[0]].movie_id
        recommended_movies.append(movies.iloc[idx[0]].title)
        #fetch Poster from Api

        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters


st.title('Movie Recommender System')
movies_dict = pickle.load (open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
# Download and load similarity matrix
file_url = "https://drive.google.com/file/d/1617bonCSiYrqK2jQtEM_mgixC_Hkl8k8/view?usp=drive_link"
download_file(file_url, 'similarity.pkl')

try:
    with open('similarity.pkl', 'rb') as file:
        similarity = pickle.load(file)
except Exception as e:
    st.error(f"Error loading pickle file: {e}")


selected_movie_name = st.selectbox('How would you like to be contacted',movies['title'].values)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])




