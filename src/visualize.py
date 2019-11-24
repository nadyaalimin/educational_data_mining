import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_compare_dist(df, discrete_var, continuous_var):
    
    title = discrete_var
    label = df[discrete_var].unique()
    
    sns.distplot(df[df[discrete_var]==label[0]][continuous_var], hist=False, label=label[0])
    sns.distplot(df[df[discrete_var]==label[1]][continuous_var], hist=False, label=label[1])
    
    plt.title(title) 
    plt.legend()
    
    
def plot_compare_categorical(data, feature, target, top_n=10, rotation=0):
    
    df = data.copy()
    df_cnt = df.groupby([feature])[target] \
                     .value_counts(normalize=True) \
                     .rename('percentage') \
                     .reset_index() 
    
    df_cnt = df_cnt.loc[df_cnt[target]==1,:]
    df_cnt = df_cnt.sort_values(by="percentage", ascending=False).head(top_n).reset_index(drop=True)
    
    ax = sns.barplot(x=feature, y="percentage", hue=target, data=df_cnt, order=df_cnt[feature])
    ax.set_xticklabels(ax.get_xticklabels(), rotation=rotation)