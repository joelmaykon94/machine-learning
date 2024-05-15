import pandas as pd
from sklearn.preprocessing import LabelEncoder


class ClearBitcoinTwitter:
    def __init__(self):
        """"""

    def clean_rows_values_invalids(self, df):
        df = df.drop(df.index[64943])
        df = df.drop(df.index[137067])
        df = df.drop(df.index[180573])
        df = df.drop(df.index[693191])
        df = df.drop(df.index[697393])
        return df

    def remove_dates_invalids(self, df):
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        return df.dropna(subset=['date'])

    def format_date(self, df):
        df['date'] = pd.to_datetime(df['date'])
        return df['date'].dt.tz_localize(
            'UTC').dt.strftime('%m-%d-%Y')

    def part_column_two(self, df, collum, first, second):
        df = df.assign(**{
            first: df[collum].str.split().str[0],
            second: df[collum].str.split().str[-1]
        })
        return df

    def convert_text_to_number(self, df, collumn):
        label_encoder = LabelEncoder()
        label = label_encoder.fit_transform(df[collumn])
        df[collumn] = label
        return df

    def create_day_month_year(self, df, collumn_date):
        df[collumn_date] = pd.to_datetime(df[collumn_date])
        df['day'] = df[collumn_date].dt.day
        df['month'] = df[collumn_date].dt.month
        df['year'] = df[collumn_date].dt.year
        return df

    def insert_values_at_collumns(self, df, collumn):
        frequence = df[collumn].value_counts().iloc[0]
        df[collumn].fillna(frequence)
        df[collumn].isnull().sum()
        return df

    def view_data_empty(self, df):
        df.describe()
        df.info()
        df.isnull().sum()
        return df

    def remove_rows_with_collumns_empty(self, df):
        df = df.dropna(axis=0, inplace=True)
        return df

    def remove_collumns(self, df, collumns):
        return df.drop(collumns, axis=1)


class ClearBitcoinHistory:
    def format_date(self, df):
        df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')
        df['Date'] = df['Date'].dt.tz_localize('UTC').dt.strftime('%Y-%m-%d')
        return df

    def format_value_price_to_number(self, df):
        df['Price'] = df['Price'].replace(
            {'(\\D)': ''}, regex=True).replace(',', '').astype(float)
        return df


"""
dataset_bitcoin_twitter['text'] = dataset_bitcoin_twitter['text'].str.lower()

# Vectorization using Bag of Words
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(dataset_bitcoin_twitter['text'])

# Convert to DataFrame
df_text_features = pd.DataFrame(
    X.toarray(), columns=vectorizer.get_feature_names_out())

# Concatenate original DataFrame with text features
dataset_bitcoin_twitter = pd.concat(
    [dataset_bitcoin_twitter, df_text_features], axis=1)


list_collumns = ["user_name", "user_created",
                 "source", "is_retweet", "user_verified", "text"]
dataset_bitcoin_twitter = clearTwitter.remove_collumns(
    dataset_bitcoin_twitter, list_collumns)
# clearTwitter.view_data_empty(dataset_bitcoin_twitter)
clearTwitter.remove_rows_with_collumns_empty(dataset_bitcoin_twitter)
# clearTwitter.view_data_empty(dataset_bitcoin_twitter)
dataset_bitcoin_twitter
"""