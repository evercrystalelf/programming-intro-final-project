import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import pandas as pd

df=pd.read_csv('patients.csv')
women_under_65df=df[(df['age']<65)&(df['sex']=='F')]
women_over_65df=df[(df['age']>=65)&(df['sex']=='F')]
men_under_65df=df[(df['age']<65)&(df['sex']=='M')]
men_over_65df=df[(df['age']>=65)&(df['sex']=='M')]

dfss={'All':df,
      'Women Under 65':women_under_65df,
      'Women Over 65':women_over_65df,
      'Men Under 65':men_under_65df,
      'Men Over 65':men_over_65df}

def print_stats(dffs, string):
    return(' Min: %d\n Max: %d\n Average: %f\nQuartiles:\n%s \n'% (dffs[string].min(), dffs[string].max(), dffs[string].mean(), dffs[string].quantile([.25, .5, .75, 1]).to_string())    )

def counts(string): #for GUI
    return '%s \n' % df.groupby(string)['id'].count().to_string()

def graphsea(string):
    fig, axs = plt.subplots(ncols=4, sharey=True)
    sns.boxplot(x=women_under_65df[string], ax=axs[0], orient='v').set(xlabel='women_under_65', ylabel=string)
    sns.boxplot(x=women_over_65df[string], ax=axs[1], orient='v').set(xlabel='women_over_65', ylabel='')
    sns.boxplot(x=men_under_65df[string], ax=axs[2], orient='v').set(xlabel='men_under_65', ylabel='')
    sns.boxplot(x=men_over_65df[string], ax=axs[3], orient='v').set(xlabel='men_over_65', ylabel='')
    return fig
