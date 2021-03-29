from .script import data_stats
from sklearn.datasets import load_iris


data = load_iris()

def test_columns():
    df =data_stats(data)
    assert len(df.columns) == 6