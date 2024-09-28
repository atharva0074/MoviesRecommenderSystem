
# Movie Recommender System 🎬

[View Movie Recommender System](https://moviesrecommendersystem-iryvqvheouxgycfhwypkhs.streamlit.app/)
## Overview

The Movie Recommender System is a web application built using Streamlit. It recommends movies based on user input using a similarity matrix derived from movie features. The app allows users to select a movie from a dropdown menu and displays a list of recommended movies along with their posters.

## Features

- **Movie Recommendations:** Provides a list of recommended movies based on the selected movie.
- **Movie Posters:** Displays movie posters for recommended movies.

## Technologies Used

- **Python:** Programming language used for developing the app.
- **Streamlit:** Framework used for building the interactive web application.
- **Pandas:** Library used for data manipulation and analysis.
- **Requests:** Library used for making HTTP requests to fetch movie posters.
- **Gdown:** Library used for downloading files from Google Drive.
- **Pickle:** Python library used for serializing and deserializing objects.
- **Scikit-learn:** Library used for machine learning, specifically for feature extraction and similarity computation.
- **NLTK:** Library used for natural language processing, specifically for stemming.

## Installation

### Prerequisites

Ensure you have Python 3.7 or higher installed on your system.

## Download Required Files

The app requires two files to function correctly:

1. **`similarity.pkl`**: Contains the similarity matrix used to find similar movies.
2. **`movie_dict.pkl`**: Contains the movie data needed for recommendations.

To ensure that the app works properly:

1. **Update the `file_url` Variable:**

   - In the `app.py` script, update the `file_url` variable with the Google Drive link to the `similarity.pkl` file.
   - The `file_url` should look something like this: `https://drive.google.com/uc?id=<your-file-id>`.

   Example:
   ```python
   file_url = "https://drive.google.com/uc?id=1nRxFIkLs-lfRtUVozJCUAEssNkiigzd8"


## How It Works

### Data Preprocessing and Model Building

#### Data Loading:
- Load movie data and credits from CSV files.
- Merge the datasets on movie titles to consolidate information.
- Retain only the relevant columns: `movie_id`, `title`, `overview`, `genres`, `keywords`, `cast`, and `crew`.

#### Data Cleaning:
- Handle missing values by dropping rows with null entries.
- Convert JSON-like structures in columns (e.g., `genres`, `keywords`, `cast`, `crew`) to lists of relevant attributes.
- Extract specific information such as genre names, keywords, and cast members for further processing.

#### Feature Engineering:
- Combine multiple columns (`overview`, `genres`, `keywords`, `cast`, `crew`) into a single `tags` column to create a unified text representation of each movie.
- Preprocess the text data by:
  - Converting it to lowercase for uniformity.
  - Applying stemming to reduce words to their base forms (e.g., "loved", "loving", and "love" become "love").

#### Model Building:
- Use `CountVectorizer` to convert the processed text data into feature vectors.
- Compute cosine similarity between these vectors to create a similarity matrix that captures the relationships between movies.

#### Recommendation Function:
- Define a function to recommend movies based on a selected movie title using the similarity matrix.
- Fetch the top 5 most similar movies and their respective posters.

#### Pickle Files:
- Save the processed movie data and similarity matrix as pickle files (`movie_dict.pkl` and `similarity.pkl`) for efficient loading in the Streamlit app.

## Configuration

You can configure the app by updating the following variables in the script:

- [Download Similarity Matrix](https://drive.google.com/file/d/1617bonCSiYrqK2jQtEM_mgixC_Hkl8k8/view?usp=sharing): This link provides the `similarity.pkl` file required by the app.
- Update the `api_key` in the `fetch_poster` function with your own TMDB API key if needed to fetch movie posters.


## View the App

You can view the live Movie Recommender System app by clicking on the link below:

[View Movie Recommender System](https://moviesrecommendersystem-iryvqvheouxgycfhwypkhs.streamlit.app/)


## Contact

For any questions, suggestions, or feedback, please feel free to reach out:

- **Atharva Pathak**
- **Email:** atharvapathak034@gmail.com
- **GitHub:** https://github.com/atharva0074
- **LinkedIn:** https://www.linkedin.com/in/atharva034/


### Install Dependencies

Clone the repository and install the required packages:

```bash
git clone <https://github.com/adityapathak0007/MovieRecommenderSystem>
cd <MovieRecommenderSystem>
pip install -r requirements.txt
