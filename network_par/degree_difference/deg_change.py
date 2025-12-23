import os
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#import plotly.express as px
import matplotlib.patches as patches
import scipy.stats


cath=pd.read_csv('case2_4_order',sep=' ',header=None)#change here
os.chdir('case2_4')#change here for other cases
file_name,deg_change,var=[],[],[]#deg_change is list of degree change, var is var around mean
for pdb in cath.iloc[:,0]:
#for file in glob.glob('*dd'):
    file=pdb+'_dd'
    df=pd.read_csv(file,sep=' ',header=None)
    file_name.append(pdb)
    deg_change.append(df.iloc[:,8].tolist())
    #deg_change.append([abs(i) for i in df.iloc[:,8].tolist()])#for taking abs of values
    #temp=[(x-0)**2 for x in df.iloc[:,8].tolist()]#previously used to calculate variance around 0. NOT USED NOW
    #mean_deg_change=np.mean([abs(i) for i in df.iloc[:,8].tolist()])#for taking abs of values
    mean_deg_change=np.mean(df.iloc[:,8].tolist())#mean of degree changes of the file in loop
    temp=[(x-mean_deg_change)**2 for x in df.iloc[:,8].tolist()]
    #temp=[(abs(x)-mean_deg_change)**2 for x in df.iloc[:,8].tolist()]#for taking abs of values
    var.append(np.mean(temp))#variance
os.chdir('..')    
print(len(file_name),len(deg_change))
print("mean of variance:",np.mean(var))#over all pairs in that case
# GO TO @@@ FOR CHANGING MORE
"""
#fig,ax=plt.subplots(figsize=(19,10))
fig,ax=plt.subplots()
sns.boxplot(data=deg_change,showmeans=True,meanprops={'markeredgecolor':'black'})
xticklabels=[i[0:9] for i in file_name]
ax.set_xticklabels(xticklabels,rotation=90,size=8)
ax.set_ylabel('Degree changes in structural homologous domains')
plt.show()
#plt.savefig('../case2_1_dd.png',format='png',dpi=1300)
"""
#plt.bar(np.arange(0,len(file_name)),var)
#plt.show()

sns.set_style('darkgrid')
plt.fill_between(np.arange(0,len(file_name)), var,alpha=0.7,facecolor='orange',edgecolor='blue')#dodgerblue, tomato, orange
plt.xticks(np.arange(0,len(file_name)),file_name,rotation=90,size=8)
plt.hlines(np.mean(var),-1,len(file_name),color='black')#mean of all variances across that case.
plt.ylabel('Variance of degree changes')
plt.show()

"""
#adding rectangles for case3
rectangles = {
    'rect1': {'xy': (5, -0.2), 'width': 10, 'height': 13}, #CA 2.170
    'rect2': {'xy': (15, -0.2), 'width': 20, 'height': 13}, #CA 2.40
    'rect3': {'xy': (47, -0.2), 'width': 21, 'height': 13}, #CA 3.20
    'rect4': {'xy': (68, -0.2), 'width': 141, 'height': 13}, #CA 3.30
    'rect5': {'xy': (209, -0.2), 'width': 210, 'height': 13}, #CA 3.40
    'rect6': {'xy': (426, -0.2), 'width': 12, 'height': 13} #CA 3.90
}
for rect_label, rect_params in rectangles.items():
    rect = patches.Rectangle(**rect_params, linewidth=1, edgecolor='r', facecolor='none')
    plt.gca().add_patch(rect)
"""
#----------------------------------- @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#making df for deg_changes and variances of all cases. BOXPLOT
#the following df is created manually after each case run (select and run lines).
#new_df=pd.DataFrame({'file':file_name,'mean_deg_c':[np.mean(x) for x in deg_change],'var':var,'Type':'Case1'})
#new_df=new_df.append(pd.DataFrame({'file':file_name,'mean_deg_c':[np.mean(x) for x in deg_change],'var':var,'Type':'Case2'}))
#new_df=new_df.append(pd.DataFrame({'file':file_name,'mean_deg_c':[np.mean(x) for x in deg_change],'var':var,'Type':'Case3'})) #df with pair name, mean deg change and variance
#new_list=[new_df[new_df.Type=='Case1']['var'].to_list(), new_df[new_df.Type=='Case2']['var'].to_list(), new_df[new_df.Type=='Case3']['var'].to_list()] #list of lists having variances for plotting boxplots

#sns.stripplot(new_list,linewidth=0.5,jitter=0.2,palette=['blue','limegreen','red'])
#plt.xticks((0,1,2),['Case1','Case2','Case3'])
#sns.boxplot(new_list,showmeans=True,color='white',meanprops={'markerfacecolor':'yellow','markeredgecolor':'black','markersize':8})
#plt.ylabel('Variance of degree change')
#plt.savefig('all_deg_change_var.png',format='png',dpi=300)
#sns.violinplot(new_list,density_norm='count',common_norm=True,palette=['blue','limegreen','red'])
#sns.swarmplot(new_list,color='white',alpha=0.4)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#degree variance vs TM-score
var_tm=pd.read_csv('var_tm',sep=' ',)
tm_list=[var_tm[var_tm.Hue=='Case1']['TM'].to_list(), var_tm[var_tm.Hue=='Case2']['TM'].to_list(), var_tm[var_tm.Hue=='Case3']['TM'].to_list()]
var_list=[var_tm[var_tm.Hue=='Case1']['Var'].to_list(), var_tm[var_tm.Hue=='Case2']['Var'].to_list(), var_tm[var_tm.Hue=='Case3']['Var'].to_list()]
#list of lists for each case for boxplots. var_list is same as new_list.

fig = plt.figure(figsize=(16, 10), dpi= 80)
grid = plt.GridSpec(4, 4,height_ratios=[3, 3, 3, 2], width_ratios=[3, 3, 3, 1], hspace=0.5, wspace=0.3)
ax_main = fig.add_subplot(grid[:-1, :-1])
ax_right = fig.add_subplot(grid[:-1, -1], xticklabels=[])#removed yticklabels=[] to have a different y-axis for this.
ax_bottom = fig.add_subplot(grid[-1, 0:-1], xticklabels=[], yticklabels=[])

#sns.lmplot(x="Var", y="TM", hue="Hue", data=var_tm,palette=['red','limegreen','blue'],robust=True,scatter_kws={"edgecolor":'black','linewidth':0.4,'alpha':0.9})#ci=None to remove the confidence interval.
#lmplot doesn't have axis property. Using regplot and plotting manually for Hue.
#sns.scatterplot(data=var_tm,x=var_tm.Var,y=var_tm.TM,hue=var_tm.Hue,palette=['red','limegreen','blue'],edgecolor='black',ax=ax_main)
sns.regplot(x=var_list[0],y=tm_list[0],scatter_kws={'color':'blue','edgecolor':'black','linewidth':0.4,'alpha':0.9},line_kws={'color':'blue'},robust=True,label="Case1",ax=ax_main)
sns.regplot(x=var_list[1],y=tm_list[1],scatter_kws={'color':'limegreen','edgecolor':'black','linewidth':0.4,'alpha':0.9},line_kws={'color':'limegreen'},robust=True,label="Case2",ax=ax_main)
sns.regplot(x=var_list[2],y=tm_list[2],scatter_kws={'color':'red','edgecolor':'black','linewidth':0.4,'alpha':0.9},line_kws={'color':'red'},robust=True,label="Case3",ax=ax_main)
ax_main.legend(prop={'size': 20})
sns.boxplot(tm_list, ax=ax_right, orient="v",palette=['blue','limegreen','red'],width=0.5)
sns.boxplot(var_list, ax=ax_bottom, orient="h",palette=['blue','limegreen','red'],width=0.5)
ax_main.set_xlabel('Variance of degree changes',fontweight='bold')
ax_main.set_ylabel('TM scores',fontweight='bold')
#plt.savefig('var_tm.png',format='png',dpi=300)


#``````Correlation test
scipy.stats.spearmanr(tm_list[0],var_list[0])
