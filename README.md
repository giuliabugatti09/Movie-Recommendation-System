Seu `README.md` estava com uma estrutura muito boa, mas como você está no último ano de IA na **FIAP**, vamos dar aquele toque de **Sênior**. O segredo é equilibrar a explicação técnica (o "como") com o valor de negócio (o "porquê").

Aqui está a versão corrigida, profissional e totalmente em inglês (essencial para o mercado de tech):

---

```markdown
# 🎬 Movie Recommender AI: NLP-Powered Engine

> **Content-Based Recommendation System** leveraging Natural Language Processing (NLP) to provide hyper-personalized movie suggestions using the TMDb dataset.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Latest-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)

---

## 🎯 Project Overview
This project is an AI-driven recommendation engine designed to solve the "discovery" problem. Instead of simple genre matching, it analyzes the **semantic meaning** of movie overviews to find hidden patterns between films.

### How it Works (The Math)
1.  **Text Preprocessing:** Cleans and tokenizes movie overviews and metadata.
2.  **TF-IDF Vectorization:** Converts text into a high-dimensional sparse matrix, weighing the importance of specific words (Term Frequency-Inverse Document Frequency).
3.  **Sigmoid Kernel Similarity:** Calculates the probability of similarity between two movie vectors, generating a similarity score from 0 to 1.

---

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Machine Learning:** Scikit-learn (TfidfVectorizer, Sigmoid Kernel)
* **Data Manipulation:** Pandas, NumPy
* **Web Interface:** Streamlit
* **Dataset:** TMDb 5000 Movies Dataset (Metadata & Credits)

---

## 🚀 Getting Started

### 1. Prerequisites
Make sure you have Python installed. Then, clone the repository:
```bash
git clone [https://github.com/giuliabugatti09/Movie-Recommendation-System.git](https://github.com/giuliabugatti09/Movie-Recommendation-System.git)
cd Movie-Recommendation-System
```

### 2. Installation
Install the required dependencies:
```bash
pip install -r requirements.txt
```

### 3. Running the App
Launch the Streamlit interface:
```bash
streamlit run app.py
```

---

## 📊 Feature Highlights
* **Real-time Search:** Search for any of the 4,800+ titles in the database.
* **Semantic Matching:** Finds recommendations based on plot depth, not just genre tags.
* **Optimized Performance:** Uses `@st.cache_resource` for instant similarity matrix lookups.
* **Responsive UI:** Clean, modern interface designed for a professional user experience.

---

## 📂 Project Structure
```text
├── dataset/
│   ├── tmdb_5000_credit.csv
│   └── tmdb_5000_movies.csv
├── app.py              # Main Streamlit application
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

---

## 👩‍🔬 About the Author
Developed by **Giulia Bugatti** *Artificial Intelligence Student at FIAP (Faculdade de Informática e Administração Paulista)* Expected Graduation: **December 2026**

---
**Dataset Source:** [Kaggle - TMDb 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
```
