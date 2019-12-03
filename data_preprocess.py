import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_clean_data(cols=None):
    if cols is None:
        cols = ['title', 'year', 'budget', 'rating', 'creative', 'source', 'genre', 'time', 'profit', 'sequel']

    movie_data = pd.read_csv('data/MovieData.csv', )

    inflation_rate = pd.read_csv('data/inflation_rate.csv')

    # Rename the columns
    re_col = {
        'movie_name': 'title',
        'production_year': 'year',
        'production_budget': 'budget',
        'creative_type': 'creative',
        'running_time': 'time',
        }
    movie_data = movie_data.rename(columns=re_col)

    movie_data['inflation_rate'] = movie_data.year.map(lambda x:
                                                       inflation_rate[inflation_rate['Year'] == x]['Avg-Avg'].values[
                                                           0]/100+1)
    # Calculate the Profits
    movie_data['world_gross'] = movie_data.domestic_box_office + movie_data.international_box_office
    movie_data['profit'] = (movie_data.world_gross - movie_data.budget)*movie_data.inflation_rate/1e6

    clean_df = movie_data[cols]
    return clean_df


def subset_df(data, col, filt):
    subset = data.loc[data[col] == filt]
    return subset


def data_bar_graph(data, col, topn=5):
    avg_ = data.groupby(col).agg('mean').reset_index().sort_values('profit', ascending=False)
    fig, ax = plt.subplots(figsize=(7, 7))
    sns.barplot(y=col, x='profit', data=data, order=avg_[col][-topn:], color='steelblue')
    ax.set(ylabel=col.title(), xlabel='Profit ($ millions)')


def data_line_graph(data, col):
    fig, ax = plt.subplots(figsize=(7, 7))
    sns.lineplot(x='year', y='profit', hue=col, data=data, color='steelblue')
    ax.set(xlabel='Year', ylabel='Profit ($ millions)', title='{}'.format(col.title()))