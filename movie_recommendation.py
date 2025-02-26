import streamlit as st
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import sigmoid_kernel

# Títulos do App
st.title("🎬 Sistema de Recomendação de Filmes")
st.write("Descubra filmes semelhantes aos seus favoritos com IA!")

# Links dos datasets
credits_csv = "https://raw.githubusercontent.com/giuliabugatti09/Movie-Recommendation-System/main/tmdb_5000_credits.csv"
movies_csv = "https://raw.githubusercontent.com/giuliabugatti09/Movie-Recommendation-System/main/tmdb_5000_movies.csv"

# Carregar os datasets
@st.cache_data
def load_data():
    credits = pd.read_csv(credits_csv, encoding="utf-8", on_bad_lines="skip")
    movies = pd.read_csv(movies_csv, encoding="utf-8", on_bad_lines="skip")
    return credits, movies

credits, movies = load_data()

# Renomeando colunas para evitar conflitos
credits.rename(columns={"movie_id": "id"}, inplace=True)
movies_merge = movies.merge(credits, on="id")

# Removendo colunas desnecessárias
movies_cleaned = movies_merge.drop(columns=["homepage", "title_x", "title_y", "status", "production_countries"])

# Preenchendo valores nulos em 'overview'
movies_cleaned["overview"] = movies_cleaned["overview"].fillna("")

# Vetorização TF-IDF
tfv = TfidfVectorizer(min_df=3, max_features=None, strip_accents="unicode",
                      analyzer="word", token_pattern=r"\w{1,}", ngram_range=(1, 3),
                      stop_words="english")

# Criando a matriz TF-IDF
tfv_matrix = tfv.fit_transform(movies_cleaned["overview"])

# Cálculo da similaridade usando Sigmoid Kernel
sig = sigmoid_kernel(tfv_matrix, tfv_matrix)

# Criando um índice de títulos de filmes
indices = pd.Series(movies_cleaned.index, index=movies_cleaned["original_title"]).drop_duplicates()

# Função para recomendar filmes
def give_recommendations(title, sig=sig):
    if title not in indices:
        return ["Filme não encontrado 😢"]
    
    idx = indices[title]
    sig_scores = list(enumerate(sig[idx]))
    sig_scores = sorted(sig_scores, key=lambda x: x[1], reverse=True)[1:11]
    movie_indices = [i[0] for i in sig_scores]
    
    return movies_cleaned["original_title"].iloc[movie_indices]

# Interface do Streamlit
st.subheader("🔍 Busque um Filme")
movie_choice = st.selectbox("Digite ou escolha um filme:", movies_cleaned["original_title"].unique())

if st.button("Recomendar 🎥"):
    recommendations = give_recommendations(movie_choice)
    st.write("**Filmes Recomendados:**")
    for rec in recommendations:
        st.write(f"- {rec}")
