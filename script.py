import pandas as pd


from sklearn.datasets import load_iris


data = load_iris()












def data_stats(data):
    labels = data.target_names
    df = pd.DataFrame(data, columns=labels)








    return df





















print(data_stats(data))
