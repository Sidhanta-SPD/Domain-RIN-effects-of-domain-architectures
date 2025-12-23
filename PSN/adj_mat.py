import pandas as pd
import os
import glob
import sys

#input is *_w.ntf for case3
#input is *_dom_?_w.ntf for others
input_file=sys.argv[1]
#os.chdir('edge_weights')
#input_file='4gv2_dom_1_w.ntf'
file=pd.read_csv(input_file,sep=' ')
names_row=file.Chain.astype(str)+'_'+file.Res1_id.astype(str)+'_'+file.Resname1.astype(str)
#names_row=file.Chain1.astype(str)+'_'+file.Res1_id.astype(str)+'_'+file.Resname1.astype(str)#for case3
matrix_df=pd.DataFrame(0,index=list(names_row.unique()),columns=list(names_row.unique()))#adjacency matrix
for i in matrix_df.index:
    for j in matrix_df.columns:
        a=i.split('_')[1]
        b=j.split('_')[1]
        if not file[(file.Res1_id==int(a)) & (file.Res2_id==int(b))].empty:
        #if not file[(file.Res1_id==int(a)) & (file.Res2_id==int(b)) & (file.Chain1==i.split('_')[0]) & (file.Chain2==j.split('_')[0])].empty:#for case3
            c=file[(file.Res1_id==int(a)) & (file.Res2_id==int(b))].iloc[0,6]
            #c=file[(file.Res1_id==int(a)) & (file.Res2_id==int(b)) & (file.Chain1==i.split('_')[0]) & (file.Chain2==j.split('_')[0])].iloc[0,7]#for case3
            matrix_df.loc[i,j]=c
            #print(matrix_df)
#matrix_df.to_csv(input_file[0:10]+'.adj_mat',sep=' ') #commented for precaution
#matrix_df.to_csv(input_file[0:4]+'.adj_mat',sep=' ')#for case3

#degree matrix
file1=pd.read_csv(input_file[0:10]+'.deg',sep=' ')
#file1=pd.read_csv(input_file[0:4]+'.deg',sep=' ')#for case3
names_row_deg=file1.Chain.astype(str)+'_'+file1.Res_num.astype(str)+'_'+file1.Res_name.astype(str)
matrix_df1=pd.DataFrame(0,index=list(names_row_deg.unique()),columns=list(names_row_deg.unique()))#degree matrix
for i in matrix_df1.index:
    x=i.split('_')[0]
    y=i.split('_')[1]
    matrix_df1.loc[i,i]=file1[(file1.Chain==x) & (file1.Res_num==int(y))].iloc[0,3]
#matrix_df1.to_csv(input_file[0:10]+'.deg_mat',sep=' ') #commented for precaution
#matrix_df1.to_csv(input_file[0:4]+'.deg_mat',sep=' ')#for case3

