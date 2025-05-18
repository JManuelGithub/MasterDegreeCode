import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_absolute_error, r2_score

def plot_graph(plot_df):
    plot_df = plot_df[['unique_id','ds','y','GRU']]
    loss: float = mean_absolute_error(plot_df['y'], plot_df['GRU'])
    r2: float = r2_score(plot_df['y'], plot_df['GRU'])
    year: float = plot_df['GRU'].sum()/plot_df['y'].sum()*100
    pearson: float = plot_df['y'].corr(plot_df['GRU'])
    pn = plot_df['unique_id'].unique()[0]


    plt.figure(figsize=(10,3))
    sns.lineplot(data=plot_df)
    #plt.plot(plot_df['ds'], plot_df['y'], c='black', label='y')
    #plt.plot(plot_df['ds'], plot_df['GRU'], c='blue', label='GRU')
    #plt.legend()
    #plt.grid()
    
    plt.title(f'Results for: {pn}; MAE:{loss:.0f}; R2:{r2:.2f}; YoY:{year:.2f}%; Pearson: {pearson:.2f}')
    #plt.show()


def plot_corr (plot_df,by='Month'):
    plot_df = plot_df[['unique_id','ds','y','GRU']]
    maxi=plot_df.y.max() if plot_df.y.max()>plot_df.GRU.max() else plot_df.GRU.max()
    mini=-1000
    fig = plt.figure(figsize=(9,3), layout='constrained')#
    
    ax1 = plt.subplot(131)
    #ax1.hist(plot_df.y)
    ax1.set_xlim(mini, maxi*1.1)
    ax1.grid()
    ax1.set_title("Distribution")
    sns.histplot(plot_df,ax=ax1)
    
    ax2 = plt.subplot(132)
    #ax2.scatter(plot_df.GRU, plot_df.y, c='blue')
    ax2.axis('scaled')
    ax2.set_xlabel('y')
    ax2.set_ylabel('GRU')
    ax2.set_xlim(mini,maxi*1.1)
    ax2.set_ylim(mini,maxi*1.1)
    
    ax2.grid()
    ax2.set_title("Correlation")
    sns.scatterplot(data=plot_df,x='y',y='GRU',ax=ax2)
    
    ax3 = plt.subplot(133)
    
    #ax3.hist(plot_df.GRU)
    ax3.set_xlim(mini, maxi*1.1)
    ax3.grid()
    ax3.set_title("Boxplot")
    sns.boxplot(plot_df,ax=ax3)



def plot_test(p, by='Month'):
    #assert train['unique_id'].nunique() == p['unique_id'].nunique(), 'unique_id numbers must match between train and valid sets'
    for pn in p['unique_id'].unique():
        plot_df = p[p['unique_id']==pn]
        plot_graph(plot_df)
        plot_corr(plot_df,by=by)

def plot_df(p, by='Year'):
    '''
        input p: dataframe to plot
        output none, just plotting
    '''
    for pn in p['unique_id'].unique():
        plot_df = p[p['unique_id']==pn]
        fig = plt.figure(figsize=(9,6), layout='tight')
        ax1 = fig.add_subplot(2, 1, 1)
        
        ax1.grid()
        ax1.set_title(plot_df['unique_id'].unique()[0])
        sns.lineplot(data=plot_df[['ds','y']],x= 'ds', y='y', ax=ax1)

        ax2 = fig.add_subplot(2, 3, 4)
        df = plot_df[[by,'y']]
        data=[]
        for _ in df[by].unique():
            d=df[df[by]==_]['y']
            data.append(d)
        sns.boxplot(plot_df,x= 'Year', y='y', ax=ax2)

        ax3 = fig.add_subplot(2, 3, 5)
        sns.histplot(plot_df,x = 'y',ax=ax3)








