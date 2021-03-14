import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns

# use the make_blobs dataset
from sklearn.datasets import make_blobs

X, y = make_blobs(n_samples = 100, centers = 5, random_state = 101)

#