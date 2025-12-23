import pandas as pd

data=pd.read_csv('nox_domain_details2',sep=' ')
#print(data)

def cath_id(input_str):#function to extract CATH id from CATHS id
    id='.'.join(input_str.split('.')[0:4])
    return(id)

#>>>>>>>>>>>>>>>>>>>CASE 1>>>>>>>>>>>>>
#cases where dom1 and dom2 in a protein are homologous
temp=[]
for i in range(len(data)):
    if cath_id(data.iloc[i,1]) == cath_id(data.iloc[i,2]):
        temp.append(i)
        
df=data.iloc[temp,:]
df.reset_index(inplace=True, drop=True)
#df.to_csv('case1',sep=' ',index=False)

#>>>>>>>>>>>>>>>>>CASE 3>>>>>>>>>>>>>>>>>>
#conditions: protein1 with domains A-B vs protein2 with domains A'-B' 
temp=[]
for i in range(len(data)):
    if i in temp:
        continue
    else:
        for j in range(len(data)):
            if i!=j and cath_id(data.iloc[i,1]) == cath_id(data.iloc[j,1]) and cath_id(data.iloc[i,2]) == cath_id(data.iloc[j,2]):
                temp.append(j)
                if i not in temp:
                    temp.append(i)
df1=data.iloc[temp,:]
df1.reset_index(inplace=True, drop=True)
#df1.to_csv('case3',sep=' ',index=False)

#>>>>>>>>>>>>>>>>CASE 2_1>>>>>>>>>>>>>>>>>>>
#conditions: for two proteins, cath of dom1 is same but dom2 is not
"""
temp=[]
for i in range(len(data)):
    if i in temp:
        continue
    else:
        for j in range(len(data)):
            if i!=j and cath_id(data.iloc[i,1]) == cath_id(data.iloc[j,1]) and cath_id(data.iloc[i,2]) != cath_id(data.iloc[j,2]):
                #temp.append(j)
                if i not in temp and j not in temp:#in this case, it will miss other matched j of i as there is 'and'. Using 'or' will duplicate i.
                    temp.append(i)
                    temp.append(j)
        #print(temp)
df2=data.iloc[temp,:]
df2.reset_index(inplace=True, drop=True)
#df2.to_csv('case2_1',sep=' ',index=False)
"""

#conditions: for two proteins, cath of dom1 is same but dom2 is not. A-B and A'-C
temp=[]
for i in range(len(data)):
    if i in temp:
        continue
    else:
        for j in range(len(data)):
            if i!=j and cath_id(data.iloc[i,1]) == cath_id(data.iloc[j,1]) and cath_id(data.iloc[i,2]) != cath_id(data.iloc[j,2]):
                temp.append(j)
                if i not in temp:
                    temp.append(i)
        #print(temp)
df2=data.iloc[temp,:]
df2.reset_index(inplace=True, drop=True)
#df2.to_csv('case2_1',sep=' ',index=False)

#>>>>>>>>>>>>>>>>CASE 2_2>>>>>>>>>>>>>>>>>>>
#conditions: for two proteins, cath of dom2 is same but dom1 is not. A-B and C-B'
temp=[]
for i in range(len(data)):
    if i in temp:
        continue
    else:
        for j in range(len(data)):
            if i!=j and cath_id(data.iloc[i,1]) != cath_id(data.iloc[j,1]) and cath_id(data.iloc[i,2]) == cath_id(data.iloc[j,2]):
                temp.append(j)
                if i not in temp:
                    temp.append(i)
                    
df3=data.iloc[temp,:]
df3.reset_index(inplace=True, drop=True)
#df3.to_csv('case2_2',sep=' ',index=False)

#>>>>>>>>>>>>>CASE 2_3>>>>>>>>>>>>>
#conditions: for two proteins, cath of dom1 is same to cath of dom2 in 2nd protein. CASE: A-B and C-A'
temp=[]
for i in range(len(data)):
    if i in temp:
        continue
    else:
        for j in range(len(data)):
            if i!=j and cath_id(data.iloc[i,1]) == cath_id(data.iloc[j,2]) and cath_id(data.iloc[i,2]) != cath_id(data.iloc[j,1]):
                temp.append(j)
                if i not in temp:
                    temp.append(i)
                    
df4=data.iloc[temp,:]
df4.reset_index(inplace=True, drop=True)
#df4.to_csv('case2_3',sep=' ',index=False)

#>>>>>>>>>>>>>>CASE 2_4>>>>>>>>>>>>>>>>
#conditions: for two proteins, cath of dom2 of a protein is similar to dom1 of another protein. CASE: A-B and B'-C
temp=[]
for i in range(len(data)):
    if i in temp:
        continue
    else:
        for j in range(len(data)):
            if i!=j and cath_id(data.iloc[i,1]) != cath_id(data.iloc[j,2]) and cath_id(data.iloc[i,2]) == cath_id(data.iloc[j,1]):
                temp.append(j)
                if i not in temp:
                    temp.append(i)
                    
df5=data.iloc[temp,:]
df5.reset_index(inplace=True, drop=True)
#df5.to_csv('case2_4',sep=' ',index=False)