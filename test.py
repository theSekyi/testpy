from script import data_stats
from sklearn.datasets import load_iris


data = load_iris()

def test_columns():
    df = data_stats(data)
    assert len(df.columns) == 3

def test_column_names():
    df = data_stats(data)
    column_names = list(df.columns)
    assert column_names == ["setosa", "versicolor", "virginica"]

