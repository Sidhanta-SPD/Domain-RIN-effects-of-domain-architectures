import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import numpy as np
from scipy.stats import percentileofscore

#updated on 20-8-24. case3 now contain domain pairs

case1=pd.read_csv('degree_case1',header=None)
case2=pd.read_csv('degree_case2',header=None)
case3=pd.read_csv('degree_case3',header=None)
#new_all_deg=pd.read_csv('degree_case1_2',header=None)
all_deg=pd.read_csv('degree_all',header=None)#degrees of all nodes from unique domains in all cases.
case1.columns=['degree']
case2.columns=['degree']
case3.columns=['degree']
#new_all_deg.columns=['degree']
all_deg.columns=['degree']

#all_deg=case1.append(case2)
#all_deg=all_deg.append(case3)
#new_all_deg=new_all_deg.append(case3)

"""
sns.kdeplot(case1.degree,shade=True,label='case1')
sns.kdeplot(case2.degree,shade=True,label='case2')
sns.kdeplot(case3.degree,shade=True,label='case3')
sns.kdeplot(all_deg.degree,shade=True,label='All')
plt.xticks(range(0,21))
plt.xlabel('Degree')
plt.ylabel('Density')
plt.legend()
plt.show()
"""

#barplots
case1_dict=dict(Counter(case1.degree))
case2_dict=dict(Counter(case2.degree))
case3_dict=dict(Counter(case3.degree))
#all_dict=dict(Counter(new_all_deg.degree))
all_dict=dict(Counter(all_deg.degree))

width=0.2
plt.bar([i-(width/2)*3 for i in case1_dict.keys()],case1_dict.values(),width=width,color='lightskyblue',label='case1')
plt.bar([i-(width/2) for i in case2_dict.keys()],case2_dict.values(),width=width,color='red',label='case2')
#plt.bar(case2_dict.keys(),case2_dict.values(),width=0.25,color='red')
plt.bar([i+(width/2) for i in case3_dict.keys()],case3_dict.values(),width=width,color='limegreen',label='case3')
plt.bar([i+(width/2)*3 for i in all_dict.keys()],all_dict.values(),width=width,color='blue',label='all cases')
plt.xticks(np.arange(1,20,1))

sns.lineplot(x=[i-(width/2)*3 for i in case1_dict.keys()],y=case1_dict.values(),color='lightskyblue')
sns.lineplot(x=[i-(width/2) for i in case2_dict.keys()],y=case2_dict.values(),color='red')
sns.lineplot(x=[i+(width/2) for i in case3_dict.keys()],y=case3_dict.values(),color='limegreen')
sns.lineplot(x=[i+(width/2)*3 for i in all_dict.keys()],y=all_dict.values(),color='blue')

plt.xlabel('Degree')
plt.ylabel('Number of residues')


#percentile
#np.percentile(new_all_deg.degree,90)#11
np.percentile(all_deg.degree,90)
np.percentile(case3.degree, 90)#12

p_1=[percentileofscore(case1.degree, i) for i in np.arange(1,max(case1_dict.keys())+1)]
p_2=[percentileofscore(case2.degree, i) for i in np.arange(1,max(case2_dict.keys())+1)]
p_3=[percentileofscore(case3.degree, i) for i in np.arange(1,max(case3_dict.keys())+1)]
#p_all=[percentileofscore(new_all_deg.degree, i) for i in np.arange(1,max(all_dict.keys())+1)]
p_all=[percentileofscore(all_deg.degree, i) for i in np.arange(1,max(all_dict.keys())+1)]
plt.twinx()
plt.plot(np.arange(1,max(case1_dict.keys())+1),p_1,color='lightskyblue',linestyle='-.')
plt.plot(np.arange(1,max(case2_dict.keys())+1),p_2,color='red',linestyle='-.')
plt.plot(np.arange(1,max(case3_dict.keys())+1),p_3,color='limegreen',linestyle='-.')
plt.plot(np.arange(1,max(all_dict.keys())+1),p_all,color='blue',linestyle='-.')
plt.yticks(np.arange(0,101,10))
plt.ylabel('Percentile')

plt.hlines(percentileofscore(case1.degree,11),11, max(case3.degree),linestyles='dashed',color='lightskyblue')#max line is set to case3 max to extend the line till end
plt.vlines(11, 0, percentileofscore(case1.degree,11),linestyles='dashed') #11 can be replaced with np.percentile(case1.degree,90)

plt.hlines(percentileofscore(case2.degree,11),11,max(case3.degree),linestyles='dashed',color='red')#max line is set to case3 max to extend the line till end
plt.vlines(11, 0, percentileofscore(case2.degree,11),linestyles='dashed')

plt.hlines(percentileofscore(case3.degree,11),11,max(case3.degree),linestyles='dashed',color='limegreen')#case3 90th percentile has changed to 11 from 12 after considering domain pairs.
plt.vlines(11, 0, percentileofscore(case3.degree,11),linestyles='dashed')

#plt.hlines(percentileofscore(new_all_deg.degree,11),11,max(new_all_deg.degree),linestyles='dashed',color='blue')
plt.hlines(percentileofscore(all_deg.degree,11),11,max(all_deg.degree),linestyles='dashed',color='blue')
#plt.vlines(11, 0, percentileofscore(new_all_deg.degree,11),linestyles='dashed')
plt.vlines(11, 0, percentileofscore(all_deg.degree,11),linestyles='dashed')
plt.show()
