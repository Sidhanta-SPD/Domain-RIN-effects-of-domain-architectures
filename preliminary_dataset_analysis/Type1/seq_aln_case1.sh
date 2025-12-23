#!/bin/bash

#cd case1_files
for i in $(awk 'NR>1{print substr($1,1,4)}' ../case1)
do
	echo $i
	mkdir $i
	cd $i
	#pdb_tofasta /home/sidhant/Sidhanta/work/networks/dataset/madhusudan/monomers/working_dir/inputs/$i/${i}_dom_1.pdb >> ${i}.fa
	#pdb_tofasta /home/sidhant/Sidhanta/work/networks/dataset/madhusudan/monomers/working_dir/inputs/$i/${i}_dom_2.pdb >> ${i}.fa
	muscle -in ${i}.fa -clwstrictout ${i}.aln
	clustalw2 -infile=${i}.aln -tree -pim
	cd ..
done
