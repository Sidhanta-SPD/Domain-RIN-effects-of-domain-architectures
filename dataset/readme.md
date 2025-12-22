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


