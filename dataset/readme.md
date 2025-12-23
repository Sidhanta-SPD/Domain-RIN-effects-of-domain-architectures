# Dataset creation

**Original dataset taken from Interface library of Dr Madhusudhan's group at IISER Pune, India. Please refer the [article](https://doi.org/10.1002/pro.4406) for more details and dataset**  

`grep 'domain-domain' interface_library.tsv | awk '{print $1}' > pdb_ids_doms`  
**pdb_ids_doms** --- the pdb ids of domain-domain interfaces.  
**all** --- all rcsb custom reports were merged for extracting monomeric PDB ids.  
**remove_empty.py** --- some entries are monomer as well as multimer. Such entries are removed. Those which don't have Uniprot id also removed.  
**all_filtered** --- extracted monomeric entries. Output of *remove_empty.py*  
**pisces_input** --- only pdb ids from all_filtered. Used for reducing redundancy.  
**nr_pdbs** --- non-redundent pdb ids  
**nr_pdbs_cath** --- cath domain boundaries of non-redundant PDBs. *Supplementary*  
**two_domains_cath** --- cath domain boundary details of proteins with two domains. Considered 2nd column of CATH domain boundary file.  
**chop_domains.py** --- py to process cath domain boundaries into domains and chop them.  

**Syntax**: `python3 chop_domains.py two_domains_cath`  

**chopped_domains** --- all nr pdbs and its domain boundaries. Output of the *chop_domains.py* on *nr_pdbs_cath*. PDBs having -ve residues have errors in the boundary. *Supplementary*  
**chopped_two_domains1** --- nr pdbs having two domains and its boundaries. Output of *chop_domains py*. PDBs having -ve residues are modified to 1 so that the domain starts from 1. Mostly no errors. 3SUU is manually edited and is a special case.  
**download_two_domains** --- two domain pdbs to download for this study.  
**download_pdb.sh** --- shell script to download pdbs.  
**temp** --- list of pdbs which has -ve residues. *Supplementary*  

`for i in $(ls ????.pdb);do a=${i:0:4}_dom_2.pdb; if [ ! -f $a ];then echo $a;fi;done| cut -c1-4 > temp`  

**processing.sh** --- shell script to process outputs of noxclass in different directories.  
**nox_outputs** --- outputs of noxclass classifications. Obl,n_obl, bio, n_bio percentages. Obl: Permanent; n_obl:Transient.  
**filter.awk** --- awk to filter on 70 percentatge and label.  
**nox_results_no_mut** --- two domain proteins with intra-chain domain interaction classification.  

`awk '{print $1}' nox_results_no_mut > no_results_pdbs_no_mut`  
`grep -f nox_results_pdbs_no_mut ../../CATH/cath-domain-list-v4_3_0.txt > nox_domain_details`  
`cat nox_domain_details|tr -s ' '|cut -d ' ' -f 1-6 > nox_domain_details_f_no_mut`  

**nox_domain_details_f_no_mut** --- formatted CATHS details of no mutation pdbs. wc 294*2=588.  

**Check insertion code**
`for i in $(awk 'NR>1 {print $1}' nox_domain_details2);do echo $i;cd inputs/$i;grep "^ATOM" $i.pdb| cut -c 27|uniq;cd ../..;done`  

**insertion_code_pdbs** --- pdbs which has insertion codes.Removed. wc 6.  
**dataset.sh** --- shell script to create nox_domain_details2. A pretty format.    
**nox_domain_details2** --- pdb id, cath ids and ddi status of all structures with zero mutation. wc 288 (removed pdb insertions). Obl: permanent; non_obl: transient. THIS IS THE FINAL FILE.  

