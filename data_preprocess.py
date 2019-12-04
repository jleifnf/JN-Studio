import pandas as pd


def load_clean_data(cols=None):
    if cols is None:
        cols = ['title', 'year', 'budget', 'rating', 'creative', 'source', 'genre', 'time',
                'timebin', 'profit', 'sequel']

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
                                                       inflation_rate[inflation_rate['Year'] == x]['Avg-Avg']
                                                       .values[0] / 100 + 1)

    # Calculate the Profits and apply inflation
    movie_data['world_gross'] = movie_data.domestic_box_office + movie_data.international_box_office
    movie_data['profit'] = (movie_data.world_gross - movie_data.budget) * movie_data.inflation_rate / 1e6

    # Create Timebins by 10 minutes increments to look at it categorically
    movie_data['timebin'] = pd.cut(movie_data.time, bins=list(range(0, 360, 10)),
                                   labels=list(range(0, 360, 10))[0:-1])

    clean_df = movie_data[cols]
    return clean_df


def subset_df(data, col, filt):
    subset = data.loc[data[col].isin(filt)]
    return subset


def groupby_aggr(data, col, stats=None):
    if stats is None:
        stats = ['count', 'mean', 'std']
    if col == 'time':
        data['time_bins'] = pd.cut(data.time, bins=[0, 2, 17, 65, 99],
                                   labels=['Toddler/Baby', 'Child', 'Adult', 'Elderly'])
    else:
        genres_agg = data[[col, 'profit']].groupby(col).agg(stats)
    return genres_agg.sort_values(by=('profit', 'mean'), ascending=False)
