import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
from scipy.stats import spearmanr
import scipy.stats

file=pd.read_csv('case1_counts', sep=' ')

#preserved_bar=[(file.iloc[i,1]/(file.iloc[i,2]+file.iloc[i,1]))*100 for i in range(len(file))]
#changed_bar=[(file.iloc[i,2]/(file.iloc[i,2]+file.iloc[i,1]))*100 for i in range(len(file))]

"""
#plotting stacked bar plots of preserved and changed hub. Change 5th line for each case.
plt.bar(file.Pair,preserved_bar,color='blue')
plt.bar(file.Pair,changed_bar,bottom=preserved_bar,color='deepskyblue')
plt.yticks(range(0,102,10))
plt.xticks(rotation=90)
plt.ylabel('Percentages')
#plt.legend(['Preserved','Changed'])
plt.show()
"""

#scatterplot
file2=pd.read_csv('case2_1_counts',sep=' ')
file3=pd.read_csv('case2_2_counts',sep=' ')
file4=pd.read_csv('case2_3_counts',sep=' ')
file5=pd.read_csv('case2_4_counts',sep=' ')
file6=pd.read_csv('case3_1_counts',sep=' ')
file7=pd.read_csv('case3_2_counts',sep=' ')

file['Hue']="Case1"
file2['Hue']="Case2"
file3['Hue']="Case2"
file4['Hue']="Case2"
file5['Hue']="Case2"
file6['Hue']="Case3"
file7['Hue']="Case3"

"""
#--------PLOTTING CASE2 SUBCASES IN 4TH QUADRANT
file2['Hue']="Case2_1"
file3['Hue']="Case2_2"
file4['Hue']="Case2_3"
file5['Hue']="Case2_4"
"""

#percentage of preserved and changed in one plot with hue.
final_file=pd.concat([file,file2,file3,file4,file5,file6,file7],ignore_index=True)
#Preserved=[(final_file.iloc[i,1]/(final_file.iloc[i,2]+final_file.iloc[i,1]))*100 for i in range(len(final_file))]#comment these to get absolute values
#Changed=[(final_file.iloc[i,2]/(final_file.iloc[i,2]+final_file.iloc[i,1]))*100 for i in range(len(final_file))]#comment these to get absolute values
#final_file.Preserved=Preserved#comment these to get absolute values
#final_file.Changed=Changed#comment these to get absolute values
sns.set_style('darkgrid')
sns.scatterplot(data=final_file,x=final_file.Preserved,y=final_file.Changed,hue=final_file.Hue,palette=['blue','limegreen','red'],alpha=0.6)
plt.xticks(range(0,102,10))
plt.yticks(range(0,122,10))
#style=final_file.Hue
"""
#plotting each case, percentage of preserved and chagned in scatter plot
plt.subplot(2,2,1)
some_file=final_file[final_file.Hue=='Case1']
#sns.scatterplot(data=some_file,x=some_file.Preserved,y=some_file.Changed,color='blue')
sns.regplot(x=some_file.Preserved,y=some_file.Changed,scatter_kws={'color':'blue','edgecolor':'black','linewidth':0.4,'alpha':0.9},line_kws={'color':'blue'},robust=True,label="Case1")
plt.xticks(range(0,102,10))
plt.yticks(range(0,122,10))
plt.xlabel('No. of conserved hubs')
plt.ylabel('No. of non-conserved hubs')
plt.title('Case1')
plt.subplot(2,2,2)
some_file=final_file[final_file.Hue=='Case2']
#sns.scatterplot(data=some_file,x=some_file.Preserved,y=some_file.Changed,color='limegreen')
sns.regplot(x=some_file.Preserved,y=some_file.Changed,scatter_kws={'color':'limegreen','edgecolor':'black','linewidth':0.4,'alpha':0.9},line_kws={'color':'limegreen'},robust=True,label="Case2")
plt.xticks(range(0,102,10))
plt.yticks(range(0,122,10))
plt.xlabel('No. of conserved hubs')
plt.ylabel('No. of non-conserved hubs')
plt.title('Case2')
plt.subplot(2,2,3)
some_file=final_file[final_file.Hue=='Case3']
#if I remove the outlier '3rx7_1ut9', the slope doesn't change much. Keeping the original.
#sns.scatterplot(data=some_file,x=some_file.Preserved,y=some_file.Changed,color='red')
sns.regplot(x=some_file.Preserved,y=some_file.Changed,scatter_kws={'color':'red','edgecolor':'black','linewidth':0.4,'alpha':0.9},line_kws={'color':'red'},robust=True,label="Case3")
plt.xticks(range(0,102,10))
plt.yticks(range(0,122,10))
plt.xlabel('No. of conserved hubs')
plt.ylabel('No. of non-conserved hubs')
plt.title('Case3')
plt.subplot(2,2,4)
#sns.scatterplot(data=final_file,x=final_file.Preserved,y=final_file.Changed,hue=final_file.Hue,palette=['blue','limegreen','red'],alpha=0.6)
sns.regplot(x=final_file.Preserved,y=final_file.Changed,scatter_kws={'color':'orange','edgecolor':'black','linewidth':0.4,'alpha':0.9},line_kws={'color':'orange'},robust=True,label="All cases")
#some_file=pd.concat([file2,file5,file4,file3],ignore_index=True)#case2 subcases in 4th quadrant
#sns.scatterplot(data=some_file,x=some_file.Preserved,y=some_file.Changed,hue=some_file.Hue,palette=['blue','black','yellow','red'],alpha=0.8)#case2 subcases in 4th quadrant
plt.xticks(range(0,102,10))
plt.yticks(range(0,122,10))
plt.xlabel('No. of conserved hubs')
plt.ylabel('No. of non-conserved hubs')
plt.title('All cases')
#plt.title('Subcases of Case2') #case2 subcases in 4th quadrant
plt.show()
"""

#plotting all split violin plot.
file11=pd.DataFrame({'value':file.Preserved,'Hub':"Conserved",'case':"Case1"})
file11=file11.append(pd.DataFrame({'value':file.Changed,'Hub':"Non-conserved",'case':"Case1"}),ignore_index=True)
for i in [file2,file3,file4,file5,file6,file7]:
    file11=file11.append(pd.DataFrame({'value':i.Preserved,'Hub':"Conserved",'case':i.iloc[0,3]}),ignore_index=True)
    file11=file11.append(pd.DataFrame({'value':i.Changed,'Hub':"Non-conserved",'case':i.iloc[0,3]}),ignore_index=True)
print(file11)
palette={'Conserved':'cornflowerblue','Non-conserved':'limegreen'}
sns.violinplot(data=file11,x='case',y='value',hue='Hub',split=True,inner='box',palette=palette,linecolor='black')
plt.xlabel('')
plt.legend(loc='upper left')
plt.ylabel('Number of hubs')
plt.show()


#-------PLOTTING ALN-LEN VS #CHANGED
file22=pd.read_csv('hub_tm',sep=' ')
sns.scatterplot(data=file22,y=file22.Changed,x=file22.Aln_len,hue=file22.Hue,palette=['red','limegreen','blue'])
plt.xticks(range(0,max(file22.Aln_len)+2,50))
plt.ylabel('# of non-conserved hubs')
