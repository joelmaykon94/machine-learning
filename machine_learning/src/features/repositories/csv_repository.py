import pandas as pd

def get_data_bitcoin_twitter():
  return pd.read_csv('../data/raw/Bitcoin_tweets.csv', nrows=500)