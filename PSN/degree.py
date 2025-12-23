import pandas as pd
import os
import glob
from collections import Counter

COUNT=0
os.chdir("./edge_weights/")
for file in glob.glob("*_dom_*_w.ntf"):
    ch, res_num, res_name, deg = [], [], [], []
    COUNT+=1
    ntf_file=pd.read_csv(file,sep=' ')
    deg_dict=Counter(ntf_file.Res1_id)
    for key in deg_dict.keys():
        df=ntf_file[ntf_file.Res1_id==key]
        df.reset_index(inplace=True,drop=True)
        ch.append(df.iloc[0,0]),res_num.append(key),res_name.append(df.iloc[0,2]),deg.append(len(df))
        df2=pd.DataFrame({'Chain':ch,'Res_num':res_num,'Res_name':res_name,'Degree':deg})
        #print(df2.head())
    #df2.to_csv(file[0:10]+'.deg',sep=' ',index=False)#commented for precaution
    print(file, COUNT)
        