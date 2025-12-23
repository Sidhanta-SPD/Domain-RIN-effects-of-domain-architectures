#!/bin/bash

cd domains
awk 'NR>1 {print $1, $4}' ../../case3_pairs.txt | while read -r i j
do
	echo $i"_"$j
	mkdir $i"_"$j
	cd $i"_"$j
	pdb_tofasta /home/sidhant/Sidhanta/work/networks/dataset/madhusudan/monomers/working_dir/inputs/$i/${i}_dom_1.pdb >> ${i}_${j}"_dom1.fa"
	pdb_tofasta /home/sidhant/Sidhanta/work/networks/dataset/madhusudan/monomers/working_dir/inputs/$j/${j}_dom_1.pdb >> ${i}_${j}"_dom1.fa"
	sed -i "0,/PDB/{s/PDB/$i/}" ${i}_${j}"_dom1.fa" #0th line to the occurence of pattern
	sed -i "2,/PDB/{s/PDB/$j/}" ${i}_${j}"_dom1.fa" #2nd line to occurence of pattern
	muscle -in ${i}_${j}"_dom1.fa" -clwstrictout ${i}_${j}"_dom1.aln"
	clustalw2 -infile=${i}_${j}"_dom1.aln" -tree -pim
	
	#dom2 pairs of the PDBs
	pdb_tofasta /home/sidhant/Sidhanta/work/networks/dataset/madhusudan/monomers/working_dir/inputs/$i/${i}_dom_2.pdb >> ${i}_${j}"_dom2.fa"
        pdb_tofasta /home/sidhant/Sidhanta/work/networks/dataset/madhusudan/monomers/working_dir/inputs/$j/${j}_dom_2.pdb >> ${i}_${j}"_dom2.fa"
        sed -i "0,/PDB/{s/PDB/$i/}" ${i}_${j}"_dom2.fa" #0th line to the occurence of pattern
        sed -i "2,/PDB/{s/PDB/$j/}" ${i}_${j}"_dom2.fa" #2nd line to occurence of pattern
        muscle -in ${i}_${j}"_dom2.fa" -clwstrictout ${i}_${j}"_dom2.aln"
        clustalw2 -infile=${i}_${j}"_dom2.aln" -tree -pim

	cd ..
done
