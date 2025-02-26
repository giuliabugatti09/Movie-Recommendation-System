pip install -r requirement.txt

from IPython.display import display
import pandas as pd
import numpy as np

# Links corretos para os arquivos CSV
credits_csv = "https://raw.githubusercontent.com/giuliabugatti09/Movie-Recommendation-System/main/tmdb_5000_credits.csv"
movies_url = "https://raw.githubusercontent.com/giuliabugatti09/Movie-Recommendation-System/main/tmdb_5000_movies.csv"

# Lendo os arquivos corretamente
credits = pd.read_csv(credits_csv, encoding='utf-8', on_bad_lines='skip')
movies = pd.read_csv(movies_url, encoding='utf-8')

# Visualizando as primeiras linhas em formato de tabela
print("Tabela Credits:")
display(credits.head()) #Mostra a tabela credits
print("\nTabela Movies:")
display(movies.head()) # Mostra a tabela movies

print("Credits:",credits.shape)
print("Movies Dataframe:",movies.shape)

credits_column_renamed = credits.rename(index=str, columns={"movie_id": "id"})
movies_merge = movies.merge(credits_column_renamed, on='id')
display(movies_merge.head())

movies_cleaned = movies_merge.drop(columns=['homepage', 'title_x', 'title_y', 'status','production_countries'])

display(movies_cleaned.head())
display(movies_cleaned.info())
display(movies_cleaned.head(1)['overview'])
# fill in the np.nan values with empty string
movies_cleaned['overview'] = movies_cleaned['overview'].fillna('')

tfv = TfidfVectorizer(min_df=3,  max_features=None,
            strip_accents='unicode', analyzer='word',token_pattern=r'\w{1,}',
            ngram_range=(1, 3),
            stop_words = 'english')

# Fitting the TF-IDF on the 'overview' text
tfv_matrix = tfv.fit_transform(movies_cleaned['overview'])
print(tfv_matrix)
print(tfv_matrix.shape)
from sklearn.metrics.pairwise import sigmoid_kernel

# Compute the sigmoid kernel
sig = sigmoid_kernel(tfv_matrix, tfv_matrix)
print(sig[0])
# Reverse mapping of indices and movie titles
indices = pd.Series(movies_cleaned.index, index=movies_cleaned['original_title']).drop_duplicates()
print(indices)
print(indices['Newlyweds'])

# Determine the valid range of indices by the shape of the matrix
max_index = sig.shape[0] -1
# Print the maximum index value
print(f"The maximum index is: {max_index}")
# Verify if the value is inside the matrix, if not, print the maximum value available
if max_index > 0:
    print(sig[max_index])
else:
    print(f"The matrix is empty or does not have valid indexes")

print(list(enumerate(sig[indices['Newlyweds']])))
print(sorted(list(enumerate(sig[indices['Newlyweds']])), key=lambda x: x[1], reverse=True))
def give_recomendations(title, sig=sig):
    # Get the index corresponding to original_title
    idx = indices[title]

    # Get the pairwsie similarity scores
    sig_scores = list(enumerate(sig[idx]))

    # Sort the movies
    sig_scores = sorted(sig_scores, key=lambda x: x[1], reverse=True)

    # Scores of the 10 most similar movies
    sig_scores = sig_scores[1:11]

    # Movie indices
    movie_indices = [i[0] for i in sig_scores]

    # Top 10 most similar movies
    return movies_cleaned['original_title'].iloc[movie_indices]
    print(give_recomendations('Avatar'))
