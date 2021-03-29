import pandas as pd
from sklearn.datasets import load_iris


data = load_iris()


def load_data(data):
    labels = data.target_names
    df = pd.DataFrame(data, columns=labels)

    return df


def preprocess(df):

    pass


print(load_data(data))
