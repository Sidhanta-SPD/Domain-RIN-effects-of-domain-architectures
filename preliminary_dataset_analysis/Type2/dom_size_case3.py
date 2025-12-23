import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

file=pd.read_csv("dom_size_dom1",sep=' ',header=None)
file4=pd.read_csv("dom_size_dom2",sep=' ',header=None)
file2=pd.read_csv("seq_aln_results_doms",sep=' ',header=None)
file3=pd.read_csv('tm-score_doms', sep=' ', header=None)
file3.columns=('PDB','score1','score2')
file.columns=('PDB','Dom1','Dom2','coverage')
file4.columns=('PDB','Dom1','Dom2','coverage')
file2.columns=('PDB','id1','id2')
#file=pd.merge(file, file2,on='PDB')#merges two dataframes based on the values in 'PDB' column


x=np.arange(len(file))
file['Diff']=abs(file.Dom1-file.Dom2)
file4['Diff']=abs(file4.Dom1-file4.Dom2)
file=file.sort_values('Diff').reset_index(drop=True)
file4=file4.sort_values('Diff').reset_index(drop=True)

file['max_dom']=[max(file.Dom1[i],file.Dom2[i]) for i in range(len(file))]#The size of bigger domain
file4['max_dom']=[max(file4.Dom1[i],file4.Dom2[i]) for i in range(len(file4))]

sns.set_style('darkgrid')

#domain size plot
sns.scatterplot(x=file.Diff,y=file.max_dom,color='blue',label='1st domain pair')
sns.scatterplot(x=file4.Diff,y=file4.max_dom,color='red',label='2nd domain pair')
plt.ylabel('Size of bigger domain')
plt.xlabel('Difference between domain sizes')
plt.legend()
plt.show()

#Histogram plots
#bins=np.arange(0,211,10)
bins=np.arange(0,271,10) #to match all axes in all Types
plt.hist([file.Diff,file4.Diff],bins=bins,edgecolor='black')
plt.xticks([x*10 for x in range(28)],[x*10 for x in range(28)],rotation=90)
plt.yticks(np.arange(0,171,20))
plt.legend(['1st domain pair','2nd domain pair'])
plt.xlabel('Domain size differences',fontsize=15)
plt.ylabel('Count of domain pairs',fontsize=15)

#Tm-score plotting
file3=file3.sort_values('score1').reset_index(drop=True)
sns.lineplot(x=x, y=file3.score1,marker='o',label='1st domain pair')
sns.lineplot(x=x,y=file3.score2,marker='*',label='2nd domain pair')
plt.xticks(x,list(file3.PDB),rotation=90)
plt.ylabel('TM-scores')
plt.legend()
plt.show()

#coverage plot
plt.bar(x,file.coverage,color='black')
plt.bar(x,file4.coverage,color='black')
plt.axhline(y=0.5,color='red')
plt.ylabel('Proportion of coverage')
plt.xlabel('# of pairs')
plt.show()

#seq id %
sns.lineplot(x,file2.id1,color='limegreen',label='%id of 1st domain pair')
sns.lineplot(x,file2.id2,color='skyblue',label='%id of 2nd domains pair')
plt.xlabel('# of pairs')
plt.ylabel('%id of sequence of domains')
plt.legend()
plt.show()

#seq-id vs tm-score
file3=file3.merge(file2,on='PDB')
sns.scatterplot(x=file3.id1,y=file3.score1,label='1st domain pair',alpha=0.7)
sns.scatterplot(x=file3.id2,y=file3.score2, label='2nd domain pair',alpha=0.7)
plt.xlabel('Seq id of domain pairs')
plt.ylabel('TM-score of domain pairs')

#------------------------------------------------------------------------------
#proteins
file10=pd.read_csv("prot_size",sep=' ',header=None)
file11=pd.read_csv("seq_aln_results_prots",sep=' ',header=None)
file12=pd.read_csv("tm-score_prots", sep=' ', header=None)

file10.columns=('PDB','Prot1','Prot2','coverage')
file11.columns=('PDB','id1')
file12.columns=('PDB','score1')

x=np.arange(len(file10))
file10['Diff']=abs(file10.Prot1-file10.Prot2)
file10['max_prot']=[max(file10.Prot1[i],file10.Prot2[i]) for i in range(len(file10))]#The size of bigger domain

#domain size plot
sns.scatterplot(x=file10.Diff,y=file10.max_prot,color='blue')
plt.ylabel('Size of bigger protein')
plt.xlabel('Difference between protein sizes')
plt.show()

#protein size histogram
bins=np.arange(0,311,10)
plt.hist(file10.Diff,bins=bins,edgecolor='black')
plt.xticks([x*10 for x in range(32)],[x*10 for x in range(32)],rotation=90)
plt.xlabel('Protein size difference')
plt.ylabel('Count of protein pairs')

#Tm-score plotting
file12=file12.sort_values('score1').reset_index(drop=True)
sns.lineplot(x=x, y=file12.score1,marker='o')
plt.xticks(x,list(file3.PDB),rotation=90)
plt.ylabel('TM-scores')
#plt.legend()
plt.show()

#coverage plot
plt.bar(x,file10.coverage,color='black')
plt.axhline(y=0.5,color='red')
plt.ylabel('Proportion of coverage')
plt.xlabel('# of pairs')
plt.show()

#seq id %
sns.lineplot(x,file11.id1,color='orange')
plt.xlabel('# of pairs')
plt.ylabel('%id of sequence of proteins')
#plt.legend()
plt.show()

#seq-id vs tm-score of proteins
file12=file12.merge(file11,on='PDB')
sns.scatterplot(x=file12.id1, y=file12.score1)
plt.xlabel('Sequence id of protein pairs')
plt.ylabel('TM-scores of protein pairs')