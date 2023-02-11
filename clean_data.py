import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("FedData/2014-12.csv")
for name in df.columns:
    if(df[name].isna().sum() > 0):
        df = pd.drop(columns=[name])
        print(name)


def tranform1(series):
    return series

def transform2(series):
    