import streamlit as st
import pickle
import pandas as pd
import gdown
import requests


def download_file(url, filename):
    try:
       
        gdown.download(url, filename, quiet=False)

    except Exception as e:
        st.error(f"Failed to download file: {e}")


def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    try:
        data = requests.get(url).json()
        poster_path = data.get('poster_path')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"
        else:
            return "https://via.placeholder.com/500x750?text=Poster+Not+Available"
    except Exception as e:
        st.error(f"Failed to fetch poster: {e}")
        return "https://via.placeholder.com/500x750?text=Poster+Not+Available"


def recommend(movie):
    try:
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:6]

        recommended_movies = []
        recommended_movies_posters = []
        for i in movies_list:
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movies.append(movies.iloc[i[0]].title)
            recommended_movies_posters.append(fetch_poster(movie_id))
        return recommended_movies, recommended_movies_posters
    except Exception as e:
        st.error(f"Error during recommendation: {e}")
        return [], []


# Inject custom CSS
st.markdown(
    """
    <style>
    /* Apply dark theme to entire app */
    .css-1y0tad9 {
        background-color: #121212; /* Dark background color */
        color: #e0e0e0; /* Light text color */
    }

    /* Style buttons */
    .stButton > button {
        background-color: #333;
        color: #e0e0e0;
        border: none;
    }

    .stButton > button:hover {
        background-color: #444;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Download and load similarity matrix
file_url = "https://drive.google.com/uc?id=1617bonCSiYrqK2jQtEM_mgixC_Hkl8k8"  # Direct download link
download_file(file_url, 'similarity.pkl')

try:
    with open('similarity.pkl', 'rb') as file:
        similarity = pickle.load(file)
except Exception as e:
    st.error(f"Error loading pickle file: {e}. Please check if the file is a valid pickle file.")
# Load movie dictionary
try:
    with open('movies_dict.pkl', 'rb') as file:
        movies_dict = pickle.load(file)
        movies = pd.DataFrame(movies_dict)
except Exception as e:
    st.error(f"Error loading movies pickle file: {e}")

st.title('🎬 Movie Recommender System')

if not movies.empty:
    selected_movie_name = st.selectbox(
        'Select a movie from the dropdown below:',
        movies['title'].values
    )

    if st.button('Show Recommendations'):
        if 'similarity' in locals():
            with st.spinner('Generating recommendations...'):
                recommended_movies, recommended_movies_posters = recommend(selected_movie_name)
            if recommended_movies:
                st.subheader(f"Recommendations for '{selected_movie_name}':")
                cols = st.columns(5)
                for col, movie, poster in zip(cols, recommended_movies, recommended_movies_posters):
                    with col:
                        st.image(poster, use_column_width=True)
                        st.write(movie)
            else:
                st.warning("No recommendations available at the moment.")
        else:
            st.error("Similarity matrix is not loaded. Please check the file.")
else:
    st.error("Movies data is not loaded. Please check the file.")

