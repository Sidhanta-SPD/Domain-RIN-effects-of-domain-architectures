import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

file=pd.read_csv("dom_size",sep=' ',header=None)
file2=pd.read_csv("seq_aln_results",sep=' ',header=None)
file.columns=('PDB','Dom1','Dom2','coverage')
file2.columns=('PDB','id')
file=file.merge(file2,on='PDB')#merges two dataframes based on the values in 'PDB' column

x=np.arange(len(file))
file['Diff']=abs(file.Dom1-file.Dom2)
file=file.sort_values('Diff').reset_index(drop=True)

"""
plt.plot(x, file.Dom1,marker='o')
plt.plot(x, file.Dom2,marker='*')
plt.plot(x,file.Diff)
plt.legend(['Dom1','Dom2'])
plt.xticks(x,list(file.PDB),rotation=90)
plt.show()"""

#Dom sizes, dom size diff, seq id% plotting
sns.set_style('darkgrid')
plt.figure(figsize=(15,8))
fig=sns.lineplot(x=x,y=file.Dom1,marker='o',color='blue')
fig=sns.lineplot(x=x,y=file.Dom2,marker='*',markersize=10,color='red')
fig=sns.lineplot(data=file,x=x,y=file.Diff,color='green')

plt.xticks(x,list(file.PDB),rotation=90)
plt.yticks(np.arange(0,451,50))
plt.ylabel('Domain sizes')
fig.legend(['Size of Dom1','Size of Dom2','Diff. of domain size'])
fig.twinx()#s
fig=sns.lineplot(data=file,x=x,y=file.id,color='limegreen')
fig.legend(['Seq identity %'])
plt.ylabel('% Seq identity')

#the above plot is very difficult to understand. Plotting a histgram
#---Histogram of domain differences
#bins=np.arange(0,201,10)
bins=np.arange(0,271,10) #to match all axes in all Types
plt.hist(file.Diff, bins=bins, edgecolor='black')
#plt.xticks([x*10 for x in range(21)], [x*10 for x in range(21)], rotation=90)
plt.xticks([x*10 for x in range(28)],[x*10 for x in range(28)],rotation=90)
plt.yticks(np.arange(0,171,20))
plt.ylabel('Count of domain pairs',fontsize=15)
plt.xlabel('Domain size difference in protein',fontsize=15)
plt.show()

#Tm-score plotting
file3=pd.read_csv('tm-scores', sep=' ', header=None)
file3.columns=('PDB','score')
sns.lineplot(x=x, y=file3.score,marker='o')
plt.xticks(x,list(file3.PDB),rotation=90)
plt.show()

#----Seq id vs tm-score
file=file.merge(file3,on='PDB')
sns.scatterplot(x=file.id,y=file.score)
plt.xlabel('Sequence id of domain pairs')
plt.xticks(np.arange(5,55,5))
plt.ylabel('TM-scores of domain pairs')
