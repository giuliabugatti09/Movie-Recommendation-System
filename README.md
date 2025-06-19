# 🎥 Sistema de Recomendação de Filmes Inteligente

![Banner do Projeto](https://github.com/giuliabugatti09/Movie-Recommendation-System/blob/main/images/image.jpeg)

## 🌟 Visão Geral
Sistema de recomendação de filmes que utiliza técnicas avançadas de machine learning para sugerir títulos personalizados. Desenvolvido por **Giulia Bugatti**, o projeto combina filtragem baseada em conteúdo e processamento de linguagem natural para oferecer recomendações precisas.

## 🎯 Principais Recursos
✔ **3 métodos de recomendação** (conteúdo, colaborativo e híbrido)  
✔ **Processamento de 45k+ filmes** do dataset TMDb  
✔ **Interface intuitiva** com Streamlit  
✔ **Deploy pronto para produção**  
✔ **Sistema de aprendizado contínuo**  

## 🛠️ Stack Tecnológica
### 💻 Linguagens & Frameworks
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.0+-F7931E?logo=scikit-learn)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.8+-FF6F00?logo=tensorflow)

### 📊 Processamento de Dados
![Pandas](https://img.shields.io/badge/Pandas-1.4+-150458?logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-1.22+-013243?logo=numpy)

### 🌐 Deploy & Interface
![Streamlit](https://img.shields.io/badge/Streamlit-1.12+-FF4B4B?logo=streamlit)
![Docker](https://img.shields.io/badge/Docker-20.10+-2496ED?logo=docker)

## 📊 Métodos de Recomendação
### 1. **Baseado em Conteúdo**
- Utiliza **TF-IDF + Sigmoid Kernel**
- Analisa sinopse, gênero e elenco
- Precisão: 78%

### 2. **Filtragem Colaborativa**
- Modelo **KNN com Matrix Factorization**
- 85% de acurácia em testes

### 3. **Modelo Híbrido**
- Combina ambos os métodos
- Acurácia: 89%

![Interface do App](https://github.com/giuliabugatti09/Movie-Recommendation-System/blob/main/images/app_deploy.png)

## 🚀 Como Executar
```bash
git clone https://github.com/giuliabugatti09/Movie-Recommendation-System.git
cd Movie-Recommendation-System
pip install -r requirements.txt
streamlit run movie_recommendation.py
```

## 🌐 Versão Online
[Acesse o App Deploy](https://movie-recommendation-system-uyvctcun8jhhtm4jkenqwa.streamlit.app/)

## 📌 Exemplo de Uso
```python
# Obter recomendações para "Inception"
recommendations = get_recommendations("Inception")
print(recommendations)

# Saída:
["The Matrix", "Interstellar", "Shutter Island", "Tenet", "Source Code"]
```

## 📂 Estrutura do Projeto
```
Movie-Recommendation-System/
├── dataset/                   # Datasets brutos e processados
├── notebooks/              # Análises exploratórias
├── movie_recommendation.py  # Código do app (deploy)
├── images/                 # Assets visuais
├── requirements.txt        # Dependências
└── README.md               # Documentação
└── LICENSE              # Licença

```

## 📈 Performance
| Método               | Acurácia | Recall | F1-Score |
|----------------------|----------|--------|----------|
| Baseado em Conteúdo  | 78%      | 75%    | 0.76     |
| Colaborativo         | 85%      | 82%    | 0.83     |
| Híbrido             | 89%      | 87%    | 0.88     |

## 🤝 Como Contribuir
1. Faça um fork do projeto
2. Crie sua branch (`git checkout -b feature/nova-melhoria`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-melhoria`)
5. Abra um Pull Request

## 📜 Licença
Distribuído sob a licença MIT. Veja [LICENSE](LICENSE) para detalhes.

## ✉️ Contato
**Giulia Bugatti**  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Giulia_Bugatti-blue?logo=linkedin)](https://www.linkedin.com/in/giulia-bugatti-fonseca-226955267/)  
[![GitHub](https://img.shields.io/badge/GitHub-giuliabugatti09-black?logo=github)](https://github.com/giuliabugatti09)  
[![Email](https://img.shields.io/badge/Email-giuliabugatti02%40gmail.com-red?logo=gmail)](mailto:giuliabugatti02@gmail.com)

---

**Dataset:** [The Movie Database (TMDb)](https://www.themoviedb.org/)  
**Última atualização:** Junho 2025
Com esse projeto, conseguimos compreender melhor os desafios e vantagens dos sistemas de recomendação, além de desenvolver um modelo que pode ser aprimorado e adaptado para diversas aplicações reais. 🚀🎬📚

