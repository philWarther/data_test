import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import DataFrame, Series

datafile = '/home/phil/python/data_sim/test_data.csv'

def rel_data(file,delimiter=','):
    
    dframe = pd.read_csv(file,sep=delimiter)

    rel_count = pd.crosstab(dframe.Reviewer,dframe.Rating)

    rel_pct = pd.crosstab(dframe.Reviewer,dframe.Rating, margins=True)
    rel_pct['Relevance Rate'] = rel_pct['Relevant']/rel_pct['All']

    avg = rel_pct['Relevance Rate']['All']
    
    plt.close
    
    fig, (ax1,ax2) = plt.subplots(2,1)
    rel_count.plot.bar(rot=0,ax=ax1)
    ax1.set_title('Relevance Count')

    rel_pct['Relevance Rate'].plot.bar(rot=0,alpha=.7,ax=ax2)
    ax2.set_title('Relevance Rate')
    plt.axhline(avg,linewidth=5,color='r',alpha=.3)
    
    plt.subplots_adjust(hspace=.6)
    plt.show(block=False)
    return
    
rel_data(datafile,delimiter='\t')