from script import load_data
from sklearn.datasets import load_iris


data = load_iris()


def test_columns():
    df = load_data(data)
    assert len(df.columns) == 3


def test_column_names():
    df = load_data(data)
    column_names = list(df.columns)
    assert column_names == ["setosa", "versicolor", "virginica"]
