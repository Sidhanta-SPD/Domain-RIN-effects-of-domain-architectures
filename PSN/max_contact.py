import glob
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
#import numpy as np
import os

amino_acids = ["GLY", "ALA", "VAL", "LEU", "ILE", "MET", "CYS", "PHE", "PRO", "SER", "THR", "TYR", "TRP", "ASN", "GLN", "ASP", "GLU", "HIS", "LYS", "ARG"]
max_vals={keys:0 for keys in [(i+'_'+j) for i in amino_acids for j in amino_acids]}

COUNT=0
#for ntf in glob.glob("./ntf_files/????.ntf"):
for ntf in glob.glob("./ntf_files/????_dom_?.ntf"):
    file=open(ntf,'r')
    lines=file.readlines()
    for i in max_vals.keys():
        counter_list=[0]
        for line in lines[1:]:
            ch, res1, resn1, res2, resn2, n_ij = line.strip().split(' ')
            res_pair=resn1+'_'+resn2
            if i==res_pair:
                counter_list.append(int(n_ij))
        if max_vals[i]<max(counter_list):
            max_vals[i]=max(counter_list)
    COUNT+=1     
    print(ntf,COUNT)
    file.close()
    
max_vals={'GLY_GLY': 13, 'GLY_ALA': 17, 'GLY_VAL': 20, 'GLY_LEU': 22, 'GLY_ILE': 21, 'GLY_MET': 23, 'GLY_CYS': 16, 'GLY_PHE': 32, 'GLY_PRO': 17, 'GLY_SER': 22, 'GLY_THR': 20, 'GLY_TYR': 34, 'GLY_TRP': 41, 'GLY_ASN': 25, 'GLY_GLN': 23, 'GLY_ASP': 23, 'GLY_GLU': 27, 'GLY_HIS': 33, 'GLY_LYS': 16, 'GLY_ARG': 22, 'ALA_GLY': 17, 'ALA_ALA': 16, 'ALA_VAL': 18, 'ALA_LEU': 22, 'ALA_ILE': 20, 'ALA_MET': 19, 'ALA_CYS': 16, 'ALA_PHE': 27, 'ALA_PRO': 16, 'ALA_SER': 19, 'ALA_THR': 19, 'ALA_TYR': 29, 'ALA_TRP': 29, 'ALA_ASN': 21, 'ALA_GLN': 21, 'ALA_ASP': 23, 'ALA_GLU': 25, 'ALA_HIS': 32, 'ALA_LYS': 23, 'ALA_ARG': 24, 'VAL_GLY': 20, 'VAL_ALA': 18, 'VAL_VAL': 21, 'VAL_LEU': 22, 'VAL_ILE': 23, 'VAL_MET': 22, 'VAL_CYS': 17, 'VAL_PHE': 28, 'VAL_PRO': 17, 'VAL_SER': 20, 'VAL_THR': 23, 'VAL_TYR': 37, 'VAL_TRP': 34, 'VAL_ASN': 25, 'VAL_GLN': 23, 'VAL_ASP': 26, 'VAL_GLU': 26, 'VAL_HIS': 25, 'VAL_LYS': 21, 'VAL_ARG': 26, 'LEU_GLY': 22, 'LEU_ALA': 22, 'LEU_VAL': 22, 'LEU_LEU': 24, 'LEU_ILE': 25, 'LEU_MET': 21, 'LEU_CYS': 22, 'LEU_PHE': 28, 'LEU_PRO': 25, 'LEU_SER': 21, 'LEU_THR': 24, 'LEU_TYR': 31, 'LEU_TRP': 39, 'LEU_ASN': 24, 'LEU_GLN': 22, 'LEU_ASP': 27, 'LEU_GLU': 27, 'LEU_HIS': 26, 'LEU_LYS': 21, 'LEU_ARG': 30, 'ILE_GLY': 21, 'ILE_ALA': 20, 'ILE_VAL': 23, 'ILE_LEU': 25, 'ILE_ILE': 26, 'ILE_MET': 24, 'ILE_CYS': 21, 'ILE_PHE': 31, 'ILE_PRO': 17, 'ILE_SER': 26, 'ILE_THR': 22, 'ILE_TYR': 34, 'ILE_TRP': 31, 'ILE_ASN': 28, 'ILE_GLN': 26, 'ILE_ASP': 26, 'ILE_GLU': 23, 'ILE_HIS': 25, 'ILE_LYS': 22, 'ILE_ARG': 26, 'MET_GLY': 23, 'MET_ALA': 19, 'MET_VAL': 22, 'MET_LEU': 21, 'MET_ILE': 24, 'MET_MET': 18, 'MET_CYS': 22, 'MET_PHE': 25, 'MET_PRO': 18, 'MET_SER': 23, 'MET_THR': 24, 'MET_TYR': 32, 'MET_TRP': 36, 'MET_ASN': 22, 'MET_GLN': 23, 'MET_ASP': 24, 'MET_GLU': 30, 'MET_HIS': 35, 'MET_LYS': 25, 'MET_ARG': 38, 'CYS_GLY': 16, 'CYS_ALA': 16, 'CYS_VAL': 17, 'CYS_LEU': 22, 'CYS_ILE': 21, 'CYS_MET': 22, 'CYS_CYS': 16, 'CYS_PHE': 25, 'CYS_PRO': 15, 'CYS_SER': 18, 'CYS_THR': 18, 'CYS_TYR': 29, 'CYS_TRP': 25, 'CYS_ASN': 21, 'CYS_GLN': 18, 'CYS_ASP': 22, 'CYS_GLU': 19, 'CYS_HIS': 22, 'CYS_LYS': 18, 'CYS_ARG': 19, 'PHE_GLY': 32, 'PHE_ALA': 27, 'PHE_VAL': 28, 'PHE_LEU': 28, 'PHE_ILE': 31, 'PHE_MET': 25, 'PHE_CYS': 25, 'PHE_PHE': 34, 'PHE_PRO': 30, 'PHE_SER': 26, 'PHE_THR': 28, 'PHE_TYR': 40, 'PHE_TRP': 46, 'PHE_ASN': 34, 'PHE_GLN': 32, 'PHE_ASP': 27, 'PHE_GLU': 35, 'PHE_HIS': 42, 'PHE_LYS': 31, 'PHE_ARG': 40, 'PRO_GLY': 17, 'PRO_ALA': 16, 'PRO_VAL': 17, 'PRO_LEU': 25, 'PRO_ILE': 17, 'PRO_MET': 18, 'PRO_CYS': 15, 'PRO_PHE': 30, 'PRO_PRO': 15, 'PRO_SER': 21, 'PRO_THR': 18, 'PRO_TYR': 33, 'PRO_TRP': 38, 'PRO_ASN': 26, 'PRO_GLN': 22, 'PRO_ASP': 23, 'PRO_GLU': 26, 'PRO_HIS': 28, 'PRO_LYS': 21, 'PRO_ARG': 29, 'SER_GLY': 22, 'SER_ALA': 19, 'SER_VAL': 20, 'SER_LEU': 21, 'SER_ILE': 26, 'SER_MET': 23, 'SER_CYS': 18, 'SER_PHE': 26, 'SER_PRO': 21, 'SER_SER': 22, 'SER_THR': 24, 'SER_TYR': 31, 'SER_TRP': 32, 'SER_ASN': 24, 'SER_GLN': 28, 'SER_ASP': 29, 'SER_GLU': 27, 'SER_HIS': 26, 'SER_LYS': 22, 'SER_ARG': 28, 'THR_GLY': 20, 'THR_ALA': 19, 'THR_VAL': 23, 'THR_LEU': 24, 'THR_ILE': 22, 'THR_MET': 24, 'THR_CYS': 18, 'THR_PHE': 28, 'THR_PRO': 18, 'THR_SER': 24, 'THR_THR': 26, 'THR_TYR': 31, 'THR_TRP': 36, 'THR_ASN': 35, 'THR_GLN': 31, 'THR_ASP': 29, 'THR_GLU': 33, 'THR_HIS': 30, 'THR_LYS': 26, 'THR_ARG': 30, 'TYR_GLY': 34, 'TYR_ALA': 29, 'TYR_VAL': 37, 'TYR_LEU': 31, 'TYR_ILE': 34, 'TYR_MET': 32, 'TYR_CYS': 29, 'TYR_PHE': 40, 'TYR_PRO': 33, 'TYR_SER': 31, 'TYR_THR': 31, 'TYR_TYR': 39, 'TYR_TRP': 48, 'TYR_ASN': 39, 'TYR_GLN': 37, 'TYR_ASP': 38, 'TYR_GLU': 34, 'TYR_HIS': 48, 'TYR_LYS': 36, 'TYR_ARG': 40, 'TRP_GLY': 41, 'TRP_ALA': 29, 'TRP_VAL': 34, 'TRP_LEU': 39, 'TRP_ILE': 31, 'TRP_MET': 36, 'TRP_CYS': 25, 'TRP_PHE': 46, 'TRP_PRO': 38, 'TRP_SER': 32, 'TRP_THR': 36, 'TRP_TYR': 48, 'TRP_TRP': 48, 'TRP_ASN': 41, 'TRP_GLN': 39, 'TRP_ASP': 39, 'TRP_GLU': 44, 'TRP_HIS': 50, 'TRP_LYS': 39, 'TRP_ARG': 47, 'ASN_GLY': 25, 'ASN_ALA': 21, 'ASN_VAL': 25, 'ASN_LEU': 24, 'ASN_ILE': 28, 'ASN_MET': 22, 'ASN_CYS': 21, 'ASN_PHE': 34, 'ASN_PRO': 26, 'ASN_SER': 24, 'ASN_THR': 35, 'ASN_TYR': 39, 'ASN_TRP': 41, 'ASN_ASN': 30, 'ASN_GLN': 31, 'ASN_ASP': 29, 'ASN_GLU': 38, 'ASN_HIS': 33, 'ASN_LYS': 27, 'ASN_ARG': 34, 'GLN_GLY': 23, 'GLN_ALA': 21, 'GLN_VAL': 23, 'GLN_LEU': 22, 'GLN_ILE': 26, 'GLN_MET': 23, 'GLN_CYS': 18, 'GLN_PHE': 32, 'GLN_PRO': 22, 'GLN_SER': 28, 'GLN_THR': 31, 'GLN_TYR': 37, 'GLN_TRP': 39, 'GLN_ASN': 31, 'GLN_GLN': 29, 'GLN_ASP': 30, 'GLN_GLU': 26, 'GLN_HIS': 29, 'GLN_LYS': 32, 'GLN_ARG': 35, 'ASP_GLY': 23, 'ASP_ALA': 23, 'ASP_VAL': 26, 'ASP_LEU': 27, 'ASP_ILE': 26, 'ASP_MET': 24, 'ASP_CYS': 22, 'ASP_PHE': 27, 'ASP_PRO': 23, 'ASP_SER': 29, 'ASP_THR': 29, 'ASP_TYR': 38, 'ASP_TRP': 39, 'ASP_ASN': 29, 'ASP_GLN': 30, 'ASP_ASP': 30, 'ASP_GLU': 32, 'ASP_HIS': 35, 'ASP_LYS': 32, 'ASP_ARG': 32, 'GLU_GLY': 27, 'GLU_ALA': 25, 'GLU_VAL': 26, 'GLU_LEU': 27, 'GLU_ILE': 23, 'GLU_MET': 30, 'GLU_CYS': 19, 'GLU_PHE': 35, 'GLU_PRO': 26, 'GLU_SER': 27, 'GLU_THR': 33, 'GLU_TYR': 34, 'GLU_TRP': 44, 'GLU_ASN': 38, 'GLU_GLN': 26, 'GLU_ASP': 32, 'GLU_GLU': 30, 'GLU_HIS': 33, 'GLU_LYS': 32, 'GLU_ARG': 36, 'HIS_GLY': 33, 'HIS_ALA': 32, 'HIS_VAL': 25, 'HIS_LEU': 26, 'HIS_ILE': 25, 'HIS_MET': 35, 'HIS_CYS': 22, 'HIS_PHE': 42, 'HIS_PRO': 28, 'HIS_SER': 26, 'HIS_THR': 30, 'HIS_TYR': 48, 'HIS_TRP': 50, 'HIS_ASN': 33, 'HIS_GLN': 29, 'HIS_ASP': 35, 'HIS_GLU': 33, 'HIS_HIS': 35, 'HIS_LYS': 35, 'HIS_ARG': 38, 'LYS_GLY': 16, 'LYS_ALA': 23, 'LYS_VAL': 21, 'LYS_LEU': 21, 'LYS_ILE': 22, 'LYS_MET': 25, 'LYS_CYS': 18, 'LYS_PHE': 31, 'LYS_PRO': 21, 'LYS_SER': 22, 'LYS_THR': 26, 'LYS_TYR': 36, 'LYS_TRP': 39, 'LYS_ASN': 27, 'LYS_GLN': 32, 'LYS_ASP': 32, 'LYS_GLU': 32, 'LYS_HIS': 35, 'LYS_LYS': 24, 'LYS_ARG': 31, 'ARG_GLY': 22, 'ARG_ALA': 24, 'ARG_VAL': 26, 'ARG_LEU': 30, 'ARG_ILE': 26, 'ARG_MET': 38, 'ARG_CYS': 19, 'ARG_PHE': 40, 'ARG_PRO': 29, 'ARG_SER': 28, 'ARG_THR': 30, 'ARG_TYR': 40, 'ARG_TRP': 47, 'ARG_ASN': 34, 'ARG_GLN': 35, 'ARG_ASP': 32, 'ARG_GLU': 36, 'ARG_HIS': 38, 'ARG_LYS': 31, 'ARG_ARG': 35}

amino_acids1=amino_acids.reverse()
# Initialize an empty DataFrame
#amino_acids = sorted(set(key.split('_')[0] for key in max_vals.keys()))
matrix_df = pd.DataFrame(index=amino_acids, columns=amino_acids1)

# Populate the DataFrame
for key, value in max_vals.items():
    aa1, aa2 = key.split('_')
    matrix_df.at[aa1, aa2] = value

# Fill diagonal if needed (if 'ALA_ALA', 'ARG_ARG', etc. are not in the dictionary)
for aa in amino_acids:
    if pd.isnull(matrix_df.at[aa, aa]):
        matrix_df.at[aa, aa] = 0  # or some other default value if needed

#matrix_df
matrix_df = matrix_df.apply(pd.to_numeric, errors='coerce')
matrix_df = matrix_df.fillna(0)

#Plotting
#hm=sns.heatmap(matrix_df,annot=True,cmap='coolwarm',fmt='g')
#plt.show()

#---------------------Edge weight normalization
os.chdir('./ntf_files/')
#Weighing edges by max contacts. I_ij=n_ij/N_ij
for ntf1 in glob.glob("????.ntf"):
    pdb=ntf1.split('.')[0]
    file1=open(pdb+'_w.ntf','w')
    file1.writelines('Chain Res1_id Resname1 Res2_id Resname2 n_ij I_ij\n')
    file=open(ntf1,'r')
    lines=file.readlines()
    for line in lines[1:]:
        ch, res1, resn1, res2, resn2, n_ij = line.strip().split(' ')
        weight=int(n_ij)/matrix_df.at[resn1,resn2]
        line=line.strip()+' '+str(weight)+'\n'
        #file1.writelines(line)# commented for precaution
        #move the _w.ntf files to ../edge_weights
os.chdir('..')

    
    