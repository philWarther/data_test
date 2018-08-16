def relevance_data(file):
    import matplotlib.pyplot as plt
    import seaborn as sns
    from pandas import DataFrame, Series
    import pandas as pd
    
    dframe = pd.read_csv(file,sep='\t')

    rel_count = pd.crosstab(dframe.Reviewer,dframe.Rating)

    rel_pct = pd.crosstab(dframe.Reviewer,dframe.Rating, margins=True)
    rel_pct['Relevance Rate'] = rel_pct['Relevant']/rel_pct['All']

    avg = rel_pct['Relevance Rate']['All']

    fig, (ax1,ax2) = plt.subplots(2,1)
    rel_count.plot.bar(rot=0,ax=ax1)
    ax1.set_title('Relevance Count')

    rel_pct['Relevance Rate'].plot.bar(rot=0,alpha=.7,ax=ax2)
    ax2.set_title('Relevance Rate')
    plt.axhline(avg,linewidth=5,color='r')

    plt.show(block=False)
    
    print('Relevance Data')
    print(rel_pct)
    return 