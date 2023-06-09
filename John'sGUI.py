import csv
import numpy as np
import pandas as pd


empty_list=[]
women_under_65=[]
women_over_65=[]
men_under_65=[]
men_over_65=[]

df=pd.read_csv('patient_with_cardio_case.csv')
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
import tkinter as tk
root = tk.Tk()
root.wm_title("Supersquad")
w=tk.Label(root, text="Counts and Statistics")
w.pack()

tkvar = tk.StringVar(root)
choices = {'Disease at Admission','state','visittype','Comorbidities'}
tkvar.set('state')

a=tk.Label(root, text="Choose a attribute to count:")
a.pack()

popupMenu = tk.OptionMenu(root, tkvar, *choices)
#y=tk.Label(popupMenu, text="Features")
#y.pack()
popupMenu.pack()

b=tk.Label(root, text="Choose a grouping and a lab test for Discriptive Statistics:")
b.pack()

def print1(*args):
    T.delete(1.0, tk.END)
    T.insert(tk.END, counts(tkvar.get()) )   
tkvar.trace('w', print1)

tkvar1 = tk.StringVar(root)
tkvar2 = tk.StringVar(root)
# Dictionary with options
choices1 = {'All',
      'Women Under 65',
      'Women Over 65',
      'Men Under 65',
      'Men Over 65'}
choices2 = {'Triglycerides','HDL','LDL','Total Cholesterol','CRP'}
tkvar1.set('All') # set the default option
tkvar2.set('HDL')

popupMenu1 = tk.OptionMenu(root, tkvar1, *choices1,)
#tk.Label(root, text="Choose a Group for Statistics")
popupMenu1.pack()

popupMenu2 = tk.OptionMenu(root, tkvar2, *choices2,)
#tk.Label(root, text="Choose a Test for Statistics")
popupMenu2.pack()

T = tk.Text(root, height=10, width=50)
T.pack()
def holder(*args):
    holder=tkvar1.get()
def print2(*args):
    T.delete(1.0, tk.END)
    T.insert(tk.END, print_stats(dfss[tkvar1.get()], tkvar2.get()) )   
tkvar1.trace('w', holder)
tkvar2.trace('w', print2)

tk.mainloop()
