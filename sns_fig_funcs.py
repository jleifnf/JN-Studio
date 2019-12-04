import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='white', context='talk', )


def data_bar_graph(data, col, topn=5,savefig=True):
    if savefig:
        c = 'w'
    else:
        c= 'k'
        
    avg_ = data.groupby(col).agg('mean').reset_index().sort_values('profit', ascending=False)
    fig, ax = plt.subplots(figsize=(7, 7))
    sns.barplot(y=col, x='profit', data=data, order=avg_[col][0:topn], color='steelblue', errcolor=c,capsize=0.1)
    sns.despine()
    ax.set_ylabel(col.title(), color=c) 
    ax.set_xlabel('Profit ($ millions)', color=c)
    ax.tick_params(axis='both', colors=c, labelcolor=c)
    ax.spines['left'].set_color(c)
    ax.spines['bottom'].set_color(c)
    fig.savefig('figs/{}-bars.png'.format(col), transparent=True, dpi=150, bbox_inches='tight')


def data_line_graph(data, col, savefig=True):
    if savefig:
        c = 'w'
    else:
        c= 'k'
        
    fig, ax = plt.subplots(figsize=(7, 7))
    sns.lineplot(x='year', y='profit', hue=col, data=data, color='steelblue')
    sns.despine()
    ax.set_xlabel('Year', color=c) 
    ax.set_ylabel('Profit ($ millions)', color=c)
    ax.tick_params(axis='both', colors=c, labelcolor=c)
    ax.spines['left'].set_color(c)
    ax.spines['bottom'].set_color(c)
    fig.savefig('figs/{}-lines.png'.format(col), transparent=True, dpi=150, bbox_inches='tight')
    
def data_scatter(data, savefig=True):
    if savefig:
        c = 'w'
    else:
        c= 'k'
    fig, ax = plt.subplots(figsize=(15, 12))
    ax = sns.scatterplot(x='budget', y='profit',
                     hue='source', size='profit',
                     sizes=(100, 400),
                     data=data.loc[data['profit'] > 250])
    ax.set_xlabel('Budget in $ millions', color=c)
    ax.set_ylabel('Profit in $ millions', color=c)
    #ax.xticks(movie_data['budget'] > 1e6, rotation=90)
    fig.savefig('figs/budget_vs_profit-scatter.png', transparent=True, dpi=150, bbox_inches='tight')
                 
                 
                 
                 
                 
