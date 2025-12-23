import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file=pd.read_csv('all_bet',sep=' ')

sns.boxplot(data=file,x=file.MAE, hue=file.case,showmeans=True)
plt.xlabel('Betweenness Mean Absolute Error(MAE)')
