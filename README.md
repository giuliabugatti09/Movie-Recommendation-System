![banner](https://github.com/giuliabugatti09/Movie-Recommendation-System/blob/main/images/image.jpeg)

![Python version](https://img.shields.io/badge/Python%20version-3.10%2B-lightgrey)
![GitHub repo size](https://img.shields.io/github/repo-size/semasuka/Credit-card-approval-prediction-classification)
![License](https://img.shields.io/badge/License-MIT-green)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1CfV6yEsHBjFiJbTKwY72k2g4AvszcF5R)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/semasuka/credit-card-approval-prediction-classification/main/cc_approval_pred.py)

## Authors

- [@giuliabugatti09](https://www.github.com/giuliabugatti09)

## **Sumário**


- [🔥 1. Descrição](#-1-descrição)
- [🔥 2. Tecnologias Utilizadas](#-2-tecnologias-utilizadas)
- [📊 3. Métodos de Recomendação](#-3-métodos-de-recomendação)
- [🚀 4. O Que Esse Projeto Demonstra?](#-4-o-que-esse-projeto-demonstra)
- [5. Funcionalidades](#5-funcionalidades)
- [6. Como Rodar o Projeto](#6-como-rodar-o-projeto)
  - [Pré-requisitos](#pré-requisitos)
  - [Rodando o App Localmente](#rodando-o-app-localmente)
  - [Como Usar?](#como-usar)
- [🔗 Link para o Deploy](#link-para-o-deploy)
- [7. Licença](#7-licença)

---

## 📊 **Métodos de Recomendação**  

### 🔹 **Filtragem Baseada em Conteúdo**  
- Recomenda itens **semelhantes** aos que o usuário já gostou, com base em atributos como **gênero, descrição, palavras-chave e atores**.  
- Usa técnicas como **TF-IDF, similaridade do cosseno ou embeddings**.  

### 🔹 **Filtragem Colaborativa**  
- Analisa o **comportamento de outros usuários** com gostos semelhantes para sugerir novos conteúdos.  
- Algoritmos como **kNN, SVD e Matrix Factorization**.  

### 🔹 **Modelo Híbrido**  
- **Combina** os dois métodos para um desempenho mais robusto.

---

Agora as ancoragens vão funcionar corretamente para seções como "Filtragem Baseada em Conteúdo", "Filtragem Colaborativa" e "Modelo Híbrido".


# Movie Recommendation System

## **🔥 1. Descrição**  

Os sistemas de recomendação são amplamente utilizados por plataformas como **Netflix, Amazon e Spotify** para sugerir conteúdos personalizados aos usuários.

Esse projeto tem como objetivo desenvolver um sistema de recomendação de **filmes ou livros**, baseado em diferentes abordagens, como **filtragem colaborativa, filtragem baseada em conteúdo e modelos híbridos**.  

Os dados utilizados neste estudo são provenientes do conjunto de dados do **TMDb** (The Movie Database), uma das principais fontes globais de informações sobre filmes, incluindo elenco, equipe de produção, popularidade e outros atributos relevantes.

- *movie_id* : Identificador único de cada filme na base de dados.
- *title* : Título original do filme.
- *cast* : Lista de atores principais que participaram do filme.
- *crew* : Lista da equipe de produção do filme, incluindo diretores, roteiristas, produtores, entre outros.

---

## **🔥 2. Tecnologias Utilizadas**  
✅ **Python**  
✅ **Pandas, NumPy**  
✅ **Scikit-learn** (para modelos de recomendação)  
✅ **Natural Language Processing (NLP)**  
✅ **TensorFlow/PyTorch** (para abordagens mais avançadas)  
✅ **Streamlit/Flask** (para interface web)  

---

## **📊 3. Métodos de Recomendação**  

### 🔹 **Filtragem Baseada em Conteúdo**  
- Recomenda itens **semelhantes** aos que o usuário já gostou, com base em atributos como **gênero, descrição, palavras-chave e atores**.  
- Usa técnicas como **TF-IDF, similaridade do cosseno ou embeddings**.  

### 🔹 **Filtragem Colaborativa**  
- Analisa o **comportamento de outros usuários** com gostos semelhantes para sugerir novos conteúdos.  
- Algoritmos como **kNN, SVD e Matrix Factorization**.  

### 🔹 **Modelo Híbrido**  
- **Combina** os dois métodos para um desempenho mais robusto.  

---

## **🚀 4. O Que Esse Projeto Demonstra?**  
✔️ Aplicação de **Machine Learning** e **Data Science**  
✔️ Conhecimento em **NLP e embeddings**  
✔️ Manipulação e **análise de grandes volumes de dados**  
✔️ Implementação de **sistemas inteligentes e personalizados**  

---

## **5. Funcionalidades**

- O usuário pode escolher um filme de uma lista e o sistema recomenda filmes semelhantes.
- O modelo usa a **TF-IDF** para vetorização e **sigmoid kernel** para calcular a similaridade entre os filmes.

## **6. Como Rodar o Projeto**

### **Pré-requisitos**

1. Instalar as dependências do projeto, para isso, você precisa ter o **Python 3.x** instalado.

   Clone este repositório:
   ```bash
   git clone https://github.com/giuliabugatti09/movie-recommendation-system.git
   cd movie-recommendation-system
   ```

2. Instale as bibliotecas necessárias:
   ```bash
   pip install -r requirements.txt
   ```

### **Rodando o App Localmente**

Para rodar o projeto localmente, use o comando:

```bash
streamlit run movie_recommendation.py
```

### **Como Usar?**
![banner](https://github.com/giuliabugatti09/Movie-Recommendation-System/blob/main/images/app_deploy.png)


1. Ao rodar o app, ele mostrará um campo para o usuário escolher o nome de um filme.
2. Depois de escolher o filme, clique no botão **Recomendar** e o sistema irá sugerir filmes semelhantes com base no filme selecionado.



## **Link para o Deploy**

Você pode acessar o aplicativo online através do seguinte link:

[Aplicativo de Recomendação de Filmes - Streamlit](https://movie-recommendation-system-uyvctcun8jhhtm4jkenqwa.streamlit.app/)


## **7. Licença**

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.




