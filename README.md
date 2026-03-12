# 🎥 Intelligent Movie Recommender: Hybrid Engine

> **Multi-engine Recommendation System** leveraging Content-Based Filtering, Collaborative Filtering, and Hybrid architectures to provide hyper-personalized movie suggestions using the TMDb dataset (45k+ titles).

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Latest-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)

---

## 🎯 Project Architecture
This system was designed to solve the "Cold Start" and "Sparsity" problems common in recommendation engines by combining three distinct approaches:

### 1. Content-Based Filtering (NLP)
* **Technique:** TF-IDF Vectorization + Sigmoid Kernel.
* **Logic:** Analyzes metadata (genres, cast, overview, keywords) to find mathematical similarity between titles.
* **Accuracy:** 78%



### 2. Collaborative Filtering (User-Item Interaction)
* **Technique:** KNN with Matrix Factorization (SVD).
* **Logic:** Predicts user preferences based on the behavior of similar users.
* **Accuracy:** 85%

### 3. Hybrid Model (Best of Both Worlds)
* **Logic:** An ensemble approach that weights both content similarity and user behavior to deliver the most robust recommendations.
* **Accuracy:** **89%**

---

## 🛠️ Tech Stack
* **Machine Learning:** Scikit-learn, TensorFlow (for Matrix Factorization).
* **Data Processing:** Pandas, NumPy.
* **Deployment:** Streamlit (Web UI), Docker (Containerization).
* **Dataset:** The Movies Dataset (TMDb) - 45,000+ movies.

---

## 📊 Performance Benchmark

| Model Architecture | Accuracy | Recall | F1-Score |
| :--- | :---: | :---: | :---: |
| Content-Based | 78% | 75% | 0.76 |
| Collaborative | 85% | 82% | 0.83 |
| **Hybrid System** | **89%** | **87%** | **0.88** |

---

## 🚀 Live Demo & Usage
You can interact with the system live here: 
👉 [**Access Live App**](https://movie-recommendation-system-uyvctcun8jhhtm4jkenqwa.streamlit.app/)

### Local Execution:
```bash
git clone [https://github.com/giuliabugatti09/Movie-Recommendation-System.git](https://github.com/giuliabugatti09/Movie-Recommendation-System.git)
pip install -r requirements.txt
streamlit run movie_recommendation.py

**Dataset:** [The Movie Database (TMDb)](https://www.themoviedb.org/)  
**Última atualização:** Junho 2025
Com esse projeto, conseguimos compreender melhor os desafios e vantagens dos sistemas de recomendação, além de desenvolver um modelo que pode ser aprimorado e adaptado para diversas aplicações reais. 🚀🎬📚

