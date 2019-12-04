import matplotlib.pyplot as plt
import seaborn as sns
from data_preprocess import subset_df, groupby_aggr

sns.set(style='white', context='talk', )


def data_bar_graph(data, col, topn=5, savefig=False):
    if savefig:
        c = 'w'
    else:
        c = 'k'

    avg_ = data.groupby(col).agg('mean').reset_index().sort_values('profit', ascending=False)
    fig, ax = plt.subplots(figsize=(7, 7))
    sns.barplot(y=col, x='profit', data=data, order=avg_[col][0:topn], color='steelblue', errcolor=c, capsize=0.1)
    sns.despine()
    ax.set_ylabel(col.title(), color=c)
    ax.set_xlabel('Profit ($ millions)', color=c)
    ax.tick_params(axis='both', colors=c, labelcolor=c)
    ax.spines['left'].set_color(c)
    ax.spines['bottom'].set_color(c)
    fig.savefig('figs/{}-bars.png'.format(col), transparent=True, dpi=150, bbox_inches='tight')


def data_line_graph(data, col, savefig=False):
    if savefig:
        c = 'w'
    else:
        c = 'k'

    fig, ax = plt.subplots(figsize=(7, 7))
    groupby_agg = groupby_aggr(data, col).reset_index()
    subset = subset_df(data, col, groupby_agg[col][0:5])
    sns.lineplot(x='year', y='profit', hue=col, data=subset, ci=None, color='steelblue')
    sns.despine()
    ax.set_xlabel('Year', color=c)
    ax.set_ylabel('Profit ($ millions)', color=c)
    ax.tick_params(axis='both', colors=c, labelcolor=c)
    ax.legend(loc='top left', bbox_to_anchor=(0, 1.1), borderaxespad=0)
    ax.spines['left'].set_color(c)
    ax.spines['bottom'].set_color(c)
    fig.savefig('figs/{}-lines.png'.format(col), transparent=True, dpi=150, bbox_inches='tight')


def data_scatter(data, savefig=False):
    fig, ax = plt.subplots(figsize=(16, 9))
    if savefig:
        ax.set_facecolor('#0066CC')
    sns.scatterplot(x='budget', y='profit',
                    hue='genre', size='profit',
                    sizes=(100, 400),
                    data=data.loc[data['profit'] > 250], ax=ax)
    ax.set_xlabel('Budget in $ millions')
    ax.set_ylabel('Profit in $ millions')
    sns.despine()
    ax.legend(loc='right', bbox_to_anchor=(1.4, 0.5), borderaxespad=0)
    fig.savefig('figs/budget_vs_profit-scatter.png', bbox_inches='tight', dpi=150)


def data_distribution(data, savefig=False):
    if savefig:
        c = 'w'
    else:
        c = 'k'
    fig, ax = plt.subplots(figsize=(10, 7))
    sns.set(style='white')
    ax = sns.distplot(data.time.dropna(), bins=50, color='steelblue')
    sns.distplot(data.iloc[0:int(data.shape[0] * 0.1)]['time'], bins=25, color='darkblue', ax=ax)
    ax.set(xlim=(50, 200), xlabel='Time (minutes)', ylabel='Ratio of movies')
    sns.despine()
    ax.set_xlabel('Time (minutes)', color=c)
    ax.set_ylabel('Ratio of movies', color=c)
    ax.tick_params(axis='both', colors=c, labelcolor=c)
    ax.spines['left'].set_color(c)
    ax.spines['bottom'].set_color(c)
    fig.savefig('figs/runtime-distribution.png', transparent=True, bbox_inches='tight', dpi=150)
