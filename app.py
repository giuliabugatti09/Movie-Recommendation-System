import streamlit as st
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import sigmoid_kernel

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Movie Recommender AI",
    page_icon="🎬",
    layout="centered"
)

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #e63946;
        color: white;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        background-color: #d62828;
        color: white;
    }
    .movie-card {
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #e63946;
        margin-bottom: 10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# --- DATA LOADING ---
@st.cache_data
def load_data():
    # Links mantidos conforme seu código original
    credits_csv = "https://raw.githubusercontent.com/giuliabugatti09/Movie-Recommendation-System/main/dataset/tmdb_5000_credit.csv"
    movies_csv = "https://raw.githubusercontent.com/giuliabugatti09/Movie-Recommendation-System/main/dataset/tmdb_5000_movies.csv"
    
    credits = pd.read_csv(credits_csv, encoding="utf-8", on_bad_lines="skip")
    movies = pd.read_csv(movies_csv, encoding="utf-8", on_bad_lines="skip")
    
    # Merge logic
    credits.rename(columns={"movie_id": "id"}, inplace=True)
    movies_merge = movies.merge(credits, on="id")
    
    # Cleaning
    movies_cleaned = movies_merge.drop(columns=["homepage", "title_x", "title_y", "status", "production_countries"], errors='ignore')
    movies_cleaned["overview"] = movies_cleaned["overview"].fillna("")
    
    return movies_cleaned

# --- TITLE & HEADER ---
st.title("🎬 Movie Recommender Engine")
st.markdown("##### *Discover your next favorite film using NLP & AI*")
st.write("---")

with st.spinner('Loading movie database...'):
    movies_cleaned = load_data()

# --- AI MODELING ---
@st.cache_resource
def train_model(_df):
    tfv = TfidfVectorizer(min_df=3, max_features=None, strip_accents="unicode",
                          analyzer="word", token_pattern=r"\w{1,}", ngram_range=(1, 3),
                          stop_words="english")
    
    tfv_matrix = tfv.fit_transform(_df["overview"])
    sig = sigmoid_kernel(tfv_matrix, tfv_matrix)
    indices = pd.Series(_df.index, index=_df["original_title"]).drop_duplicates()
    return sig, indices

sig, indices = train_model(movies_cleaned)

# --- RECOMMENDATION LOGIC ---
def give_recommendations(title, sig=sig):
    if title not in indices:
        return None
    
    idx = indices[title]
    sig_scores = list(enumerate(sig[idx]))
    sig_scores = sorted(sig_scores, key=lambda x: x[1], reverse=True)[1:11]
    movie_indices = [i[0] for i in sig_scores]
    
    return movies_cleaned["original_title"].iloc[movie_indices]

# --- USER INTERFACE ---
st.subheader("🔍 Search for a Movie")
movie_choice = st.selectbox(
    "Select or type a movie you've enjoyed:", 
    movies_cleaned["original_title"].unique(),
    index=None,
    placeholder="Choose a movie..."
)

if st.button("Get Recommendations 🚀"):
    if movie_choice:
        recommendations = give_recommendations(movie_choice)
        
        if recommendations is not None:
            st.write(f"### Top 10 recommendations for fans of **{movie_choice}**:")
            
            # Displaying in two columns for a better visual
            col1, col2 = st.columns(2)
            for i, rec in enumerate(recommendations):
                if i % 2 == 0:
                    col1.markdown(f'<div class="movie-card">🎥 {rec}</div>', unsafe_allow_html=True)
                else:
                    col2.markdown(f'<div class="movie-card">🎥 {rec}</div>', unsafe_allow_html=True)
        else:
            st.error("Movie not found in database. 😢")
    else:
        st.warning("Please select a movie first!")

# --- FOOTER ---
st.write("---")
st.caption("AI Model powered by TF-IDF Vectorization & Sigmoid Kernel Similarity.")
st.caption("Developed by Giulia Bugatti")