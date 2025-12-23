import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import networkx as nx
import multiprocessing as mp

"""
Change the aln_loc case wise
change the write filename
change the inputs in multiprocessing setup
run normally
"""

def find_var(pair, case, net_loc, ch1, ch2, dom1, dom2):
    #aln_loc='/home/sidhant/Sidhanta/work/networks/cases/'+case[0:5]+'_files/'+case+'/'+pair+'/tm-align/aligned_res' #case2
    #aln_loc='/home/sidhant/Sidhanta/work/networks/cases/'+case[0:5]+'_files/'+pair+'/tm-align/aligned_res' #case1
    aln_loc='/home/sidhant/Sidhanta/work/networks/cases/'+case[0:5]+'_files/domains/'+pair+'/tm-align2/aligned_res' #case3
    pdb1=pair.split("_")[0]
    if case != 'case1':
        pdb2=pair.split("_")[1]
    else:
        pdb2=pdb1
    adj_mat1=pd.read_csv(net_loc+pdb1+dom1+'.adj_mat',sep=' ',index_col=0)
    adj_mat2=pd.read_csv(net_loc+pdb2+dom2+'.adj_mat',sep=' ',index_col=0)
    G1=nx.from_pandas_adjacency(adj_mat1)
    G2=nx.from_pandas_adjacency(adj_mat2)
    aligned_res=pd.read_csv(aln_loc,sep=' ',header=None,names=("resn1","ch1","res1","resn2","ch2","res2"))
    aligned_res["RES1"] = aligned_res[["res1", "resn1"]].apply(lambda x: ch1+"_".join(x.astype(str)), axis =1)
    aligned_res["RES2"] = aligned_res[["res2", "resn2"]].apply(lambda x: ch2+"_".join(x.astype(str)), axis =1)
    aligned_res=aligned_res.drop(columns=["ch1","res1", "resn1","ch2","res2", "resn2"])
    aligned_res["bet1"]=[round(nx.betweenness_centrality(G1)[aligned_res["RES1"][i]],3) if aligned_res["RES1"][i] in adj_mat1.columns else np.nan for i in range(len(aligned_res))]
    aligned_res["bet2"]=[round(nx.betweenness_centrality(G2)[aligned_res["RES2"][i]],3) 
                         if aligned_res["RES2"][i] in adj_mat2.columns
                         else np.nan
                         for i in range(len(aligned_res))]
    aligned_res.dropna(subset=["bet1","bet2"], inplace=True)
    aligned_res.reset_index(drop=True, inplace=True)
    
    #var=np.var(aligned_res.bet1-aligned_res.bet2)
    mae=np.mean(aligned_res.bet1-aligned_res.bet2)
    with open('bet3_2','a') as filehandle:
        filehandle.writelines(f"{pair} {round(mae,3)} {case} {case[0:5]}\n")
    #print(f"{pair} {round(var,3)} {case} {case[0:5]}")

# Multiprocessing setup
if __name__ == "__main__":
    # Set up the variables
    case, input_file = 'case3_2', 'keep_dom2'
    ch1, ch2 = "B_", "B_"
    dom1, dom2 = '_dom_2', '_dom_2'
    net_loc = '/home/sidhant/Sidhanta/work/networks/PSN/edge_weights/'

    # Read the pairs from the input file
    pairs = [line.strip('\n') for line in open(input_file, 'r')]

    # Set the number of processes you want to use
    #num_processes = mp.cpu_count()  # or you can manually set a number like 4 or 8
    num_processes=6
    # Create a multiprocessing pool
    with mp.Pool(processes=num_processes) as pool:
        # Map the function to the pairs
        pool.starmap(find_var, [(pair, case, net_loc, ch1, ch2, dom1, dom2) for pair in pairs])