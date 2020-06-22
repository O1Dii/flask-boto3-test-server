import pandas as pd


def df_sum(df):
    df['3'] = df['1'] + df['2']

    return df
