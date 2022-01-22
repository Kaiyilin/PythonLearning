"""Classifying movie reviews:
a binary classification example

dataset: IMDB dataset
"""

import ssl
import tensorflow as tf
from tensorflow.keras.datasets import imdb

# The argument num_words=10000 means you’ll only keep the top 10,000 most frequently occurring words in the training data
ssl._create_default_https_context = ssl._create_unverified_context
(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)

print(f"1st training data: {train_data[0]}")

print(f"1st training label: {train_labels[0]}")