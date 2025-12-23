#!/bin/bash
#this script takes noxclass outputs which doesn't have mutations and lists the domain ids, along with ddi status
#USAGE: bash dataset.sh > nox_domain_details2

echo "PDB CATH1 CATH2 DDI"
cat nox_results_pdbs_no_mut| while read pdb
do
	dom1="${pdb}.01"
	dom2="${pdb}.02"
	cath1=$(grep $dom1 nox_domain_details_f_no_mut|cut -d ' ' -f 2,3,4,5,6|tr ' ' '.')
	cath2=$(grep $dom2 nox_domain_details_f_no_mut|cut -d ' ' -f 2,3,4,5,6|tr ' ' '.')
	interaction=$(grep $pdb nox_results_no_mut|cut -d ' ' -f 6)
	echo $pdb $cath1 $cath2 $interaction
done
