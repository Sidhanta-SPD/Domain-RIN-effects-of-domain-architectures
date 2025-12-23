# Preliminary analysis of the dataset  


**dom_supfam.py** --- py for understaning types of superfamilies and their frequency in the dataset.  


## Type1
**seq_aln_case1.sh** --- shell script to align sequences (atom records) of domains in pdbs using muscle and find seq id using clustalw2.  
**seq_aln_result.sh** --- shell script to extract the seq id % from the pim matrix  
**seq_aln_results** --- output of the *seq_aln_results.sh*  
**tm-align.sh** --- shell script to perform tm-alignment domain structural alignment  
**dom_size.sh** --- shell script to find domain lengths from tm-align alignment file. Also finds the coverage of alignment w.r.t to the smallest domain.  
**dom_size.py** --- py to plot  
**tm-score.sh** --- shell script to find tm-scores. Normalized tm-scores by the avg length of both domains.  
**tm-scores** --- output of *tm-score.sh*
**remove** --- pdbs with TM-score <= 0.5 and coverage <= 0.5 and unique pdbs out of them.  
**keep** --- pdbs to compare and study.wc 89-43=46.  
**top_eqv_res.sh** --- shell script to find topologically equivalent residues from sup.pdb. Generates file aligned_res in tm-align folder.  


## Type2  
**seq_aln_doms.sh** --- pair dir creation and sequence alignment of domain pairs. pdb_pdb_dom?.* file format.  
**tm_align_doms.sh** --- tm-align of domain pairs  
**seq_aln_results_doms.sh** --- sh to get seq id %. Pdb_pdb id_of_1st_dom_pair id_of_2nd_dom_pair  
**seq_aln_results_doms** --- output of *seq_aln_results_doms.sh*. wc 471  
**dom_size_doms.sh** --- sh to get dom size and coverage  
**tm-score_doms.sh** --- tm scores of domains pairs alignment.  
**tm-score_doms** --- output of *tm-score_doms.sh*. pdb_pair tm-score1 tm-score2 format. wc 471  
**remove_dom1** --- remove entries for N-teminal domain pair. All coverages are better than 0.5. Wc 57  
**remove_dom2** --- reomove entries for C-terminal domain pair. All coverages are better than 0.5. Wc 51  

`awk '$2<=0.5 {print}' tm-score_doms > remove`  
`awk '$4<=0.5 {print}' dom_size? >> remove`  

**keep_dom1** --- entries of N-terminal domain pairs for study. wc 414  
**keep_dom2** --- entries of C-terminal domain pairs for study. wc 420  
**re-assign_doms.py** --- TM-align renames the proteins for comparison. This py changes ch IDs for domains using data from chopped_two_domains1. Input is aligned_res  
**dom_size_case3.py** --- plotting related py  


## Type3
*All codes are similar to Type2*  
**dom_size_case2** --- domain length, alignment length and length coverage  
**tm-scores_case2** --- tm score of the alignment  
__keep*__ --- pdbs to work with. TM>0.5 and coverage>0.5. wc 139+25+52+54  


