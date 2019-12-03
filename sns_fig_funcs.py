import matplotlib.pyplot as plt
import seaborn as sns


def data_bar_graph(data, col, topn=5):
    avg_ = data.groupby(col).agg('mean').reset_index().sort_values('profit', ascending=False)
    fig, ax = plt.subplots(figsize=(7, 7))
    sns.barplot(y=col, x='profit', data=data, order=avg_[col][0:topn], color='steelblue')
    ax.set(ylabel=col.title(), xlabel='Profit ($ millions)')
    fig.savefig('figs/{}-bars.png'.format(col))


def data_line_graph(data, col):
    fig, ax = plt.subplots(figsize=(7, 7))
    sns.lineplot(x='year', y='profit', hue=col, data=data, color='steelblue')
    ax.set(xlabel='Year', ylabel='Profit ($ millions)', title='{}'.format(col.title()))
    fig.savefig('figs/{}-lines.png'.format(col))
