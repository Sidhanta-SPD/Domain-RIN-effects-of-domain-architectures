#!/bin/bash
#performs sequence alignment for pairs
#change parameters accordingly

cd case2_4
awk 'NR>1 {print $1, $4}' ../../case2_4_pairs.txt | while read -r i j
do
	echo $i"_"$j
	mkdir $i"_"$j
	cd $i"_"$j
	pdb_tofasta /home/sidhant/Sidhanta/work/networks/dataset/madhusudan/monomers/working_dir/inputs/$i/${i}_dom_2.pdb >> ${i}_${j}.fa
	pdb_tofasta /home/sidhant/Sidhanta/work/networks/dataset/madhusudan/monomers/working_dir/inputs/$j/${j}_dom_1.pdb >> ${i}_${j}.fa
	sed -i "0,/PDB/{s/PDB/$i/}" ${i}_${j}.fa #0th line to the occurence of pattern
	sed -i "2,/PDB/{s/PDB/$j/}" ${i}_${j}.fa #2nd line to occurence of pattern
	muscle -in ${i}_${j}.fa -clwstrictout ${i}_${j}.aln
	clustalw2 -infile=${i}_${j}.aln -tree -pim
	cd ..
done
