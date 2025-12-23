import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

file=pd.read_csv("dom_size_case2",sep=' ',header=None)
file2=pd.read_csv("seq_aln_results_case2",sep=' ',header=None)
file3=pd.read_csv('tm-scores_case2', sep=' ', header=None)
file3.columns=('PDB','score')
file.columns=('PDB','Dom1','Dom2','coverage')
file2.columns=('PDB','id')
#file=pd.merge(file, file2,on='PDB')#merges two dataframes based on the values in 'PDB' column
file['id']=0 # creating new column filled with 0
file['score']=0
for i in range(len(file)):
    for j in range(len(file2)):
        if file.iloc[i,0]==file2.iloc[j,0]:
            file.iloc[i,4]=file2.iloc[j,1]
        if file.iloc[i,0]==file3.iloc[j,0]:
            file.iloc[i,5]=file3.iloc[j,1]

x=np.arange(len(file))
file['Diff']=abs(file.Dom1-file.Dom2)
file=file.sort_values('Diff').reset_index(drop=True)

file['max_dom']=[max(file.Dom1[i],file.Dom2[i]) for i in range(len(file))]#The size of bigger domain
"""
plt.plot(x, file.Dom1,marker='o')
plt.plot(x, file.Dom2,marker='*')
plt.plot(x,file.Diff)
plt.legend(['Dom1','Dom2'])
plt.xticks(x,list(file.PDB),rotation=90)
plt.show()"""

"""
#Dom sizes, dom size diff, seq id% plotting
#sns.set_style('darkgrid')
plt.figure(figsize=(20,8))
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
"""
#domain size plot
sns.scatterplot(x=file.Diff,y=file.max_dom,color='blue')
plt.ylabel('Size of bigger domain')
plt.xlabel('Difference between domain sizes')
plt.show()

#histogram of domain diff
bins=np.arange(0,271,10)
plt.hist(file.Diff, bins=bins, edgecolor='black')
plt.xticks([x*10 for x in range(28)], [x*10 for x in range(28)], rotation=90)
plt.yticks(np.arange(0,171,20))
plt.ylabel('Count of domain pairs',fontsize=15)
plt.xlabel('Domain size difference in protein',fontsize=15)
plt.show()
#plt.savefig('dom_size2.png',format='png',dpi=300)

#Tm-score plotting
file3=file3.sort_values('score').reset_index(drop=True)
sns.lineplot(x=x, y=file3.score,marker='o')
plt.xticks(x,list(file3.PDB),rotation=90)
plt.show()

#coverage plot
plt.bar(x,file.coverage,color='black')
plt.axhline(y=0.5,color='red')
plt.ylabel('Proportion of coverage')
plt.xlabel('# of pairs')
plt.show()

#seq id %
sns.lineplot(x,file.id,color='limegreen')
plt.xlabel('# of pairs')
plt.ylabel('%id of sequence of domains')
plt.show()

#----Seq id vs tm-score
sns.scatterplot(x=file.id,y=file.score)
plt.xlabel('Sequence id of domain pairs')
plt.xticks(np.arange(5,55,5))
plt.ylabel('TM-scores of domain pairs')