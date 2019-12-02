import pandas as pd


def load_clean_data(cols=None):
    if cols is None:
        cols = ['title', 'year', 'budget', 'rating', 'creative', 'source', 'genre', 'time', 'profit']

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

load_clean_data()