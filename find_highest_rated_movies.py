import numpy as np
import pandas as pd
import pickle
import matrix_factorization_utilities

# Load user ratings
raw_dataset_df = pd.read_csv('movie_ratings_data_set.csv')

# Convert the running list of user ratings into a matrix
ratings_df = pd.pivot_table(raw_dataset_df, index='user_id', columns='movie_id', aggfunc=np.max)

# Normalize the ratings (center them around their mean)
normalized_ratings, means = matrix_factorization_utilities.normalize_ratings(ratings_df.as_matrix())




movies_df = pd.read_csv('movies.csv', index_col='movie_id')


print("Movies we will recommend:")

movies_df['rating'] = means
movies_df = movies_df.sort_values(by=['rating'], ascending=False)

print(movies_df[['title', 'genre', 'rating']].head(5))