# calculation of some network parameters  

## Degree  
**case2_doms.sh** --- sh to get the domains in case2. All the case2 and unique pdbs.  
**degree_dist.py** --- py to plot the degree distributions  
**case3_doms.sh** --- sh to write the 1st and 2nd domain pairs. Latest one to compare domain pairs instead of protein pairss.  


## difference in degrees  
__*job__ --- job files for parallel run. Type2 jobs are also split into dom1 and dom2 like the subclasses of Type3.  
**file_transfer.sh** --- sh to transfer files from different locations to folders here.  
**deg_diff.sh** --- sh to match aligned residue pair and corresponding degree file and write *dd file. Refer job file for input. Changed a bit for type2.  
**deg_change.py** --- py to generate plot for degree differences    
**stats.py** --- py to check statistical significance of variances of types.  
**deg_diff_tm.sh** --- sh to print variance of deg differences and their TM-score, RMSD.  
**var_tm** --- output of *deg_diff_tm.sh*. Contains Pair, variance of degree changes, TM-score, RMSD and Hue. LATEST. TO BE USED.  


## Hub status  
**hub_change.sh** --- sh to read /deg_change/case*/*_dd files and modify them for hub change by writing 'Preserved' or 'Changed'.  
**preserved_count.sh** --- sh to count number of preserved and changed pairs in a structure pair.  
**plotting.py** --- py to plot the hub changes  
**import_tm.sh** --- sh to print #changed hubs and import tm aln len.  
**hub_tm** --- pair, #changed, aln_len and hue  


## Betweenness  
**betweenness.py** --- multiprocessing enabled py to create bet* files  
**plot_bet.py** --- py to plot  
