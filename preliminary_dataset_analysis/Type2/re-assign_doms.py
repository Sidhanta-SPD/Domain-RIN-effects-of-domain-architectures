import pandas as pd
import os
import glob
#This py re-assigns domain chain ids in the *aligned_res file.

os.chdir('proteins')
for folder in glob.glob('*/'):
    print(folder)
    os.chdir(folder+'tm-align')
    input_file="aligned_res"
    file=pd.read_csv(input_file,sep=' ',header=None)
    #print(file)
    pdb1=folder[0:4]#first pdb
    pdb2=folder[5:9]#second pdb
    
    pdb1_range=os.popen('grep -A2 '+pdb1+' ../../../chopped_two_domains1|sed -n "3p"').read()#dom2 for pdb1
    pdb2_range=os.popen('grep -A2 '+pdb2+' ../../../chopped_two_domains1|sed -n "2p"').read()#dom1 for pdb2
    ranges1=pdb1_range.strip().split(': ')[1].split(',')
    ranges2=pdb2_range.strip().split(': ')[1].split(',')
    
    for i in range(len(file)):
        for j in ranges1:
            if file.iloc[i,2]>=int(j.split(':')[0]) and file.iloc[i,2]<=int(j.split(':')[1]):
                file.iloc[i,1]='B'
        for k in ranges2:
            if file.iloc[i,5]>=int(k.split(':')[0]) and file.iloc[i,5]<=int(k.split(':')[1]):
                file.iloc[i,4]='A'
    file.to_csv(folder[0:9]+'_aligned_res',sep=' ',index=False,header=False)
    os.chdir('../..')