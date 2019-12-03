import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_clean_data(cols=None):
    if cols is None:
        cols = ['title', 'year', 'budget', 'rating', 'creative', 'source', 'genre', 'time', 'profit', 'sequel']

    # Load the movie_data.csv
    movie_data = pd.read_csv('data/MovieData.csv', )

    # Rename the columns
    re_col = {
        'movie_name': 'title',
        'production_year': 'year',
        'production_budget': 'budget',
        'creative_type': 'creative',
        'running_time': 'time',
        }
    movie_data = movie_data.rename(columns=re_col)

    # Calculate the Profits
    movie_data['world_gross'] = movie_data.domestic_box_office + movie_data.international_box_office
    movie_data['profit'] = movie_data.world_gross - movie_data.budget

    clean_df = movie_data[cols]
    return clean_df


def subset_df(data, col, filt):
    subset = data.loc[data[col] == filt]
    return subset


def data_bar_graph(data, col, topn=5):
    avg_ = data.groupby(col).agg('mean').reset_index().sort_values('profit')
    fig, ax = plt.subplots(figsize=(7, 7))
    sns.barplot(y=col, x='profit', data=data, order=avg_[col][-topn:], color='steelblue')
    ax.set(ylabel=col.title(), xlabel='Profit')


def data_line_graph(data):
    fig, ax = plt.subplots(figsize=(7, 7))
    sns.lineplot(x='year', y='profit', data=data, color='steelblue')
    ax.set(xlabel='Year', ylabel='Profit', )