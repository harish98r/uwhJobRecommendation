import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

text = ['java Paris London Newyork Newyork Newyork']

text2 = ['java Paris London Newyork Newyork Newyork', 'java Paris London Newyork Newyork Newyork', 'Paris Paris London Newyork Newyork', 'Paris London Newyork']

cv = CountVectorizer()
count_matrix = cv.fit_transform(text)

count_matrix_2 = cv.fit_transform(text2)

similarity_scores = cosine_similarity(count_matrix, count_matrix_2)

print(similarity_scores)
