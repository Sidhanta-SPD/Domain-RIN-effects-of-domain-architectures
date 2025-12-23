#!/bin/bash

cd domains
for i in */
do
	file1=${i:0:4}
	file2=${i:5:4}
	echo $file1 $file2
	pdb1="/home/sidhant/Sidhanta/work/networks/dataset/madhusudan/monomers/working_dir/inputs/${file1}/${file1}_dom_1.pdb"
	pdb2="/home/sidhant/Sidhanta/work/networks/dataset/madhusudan/monomers/working_dir/inputs/${file2}/${file2}_dom_1.pdb"
	cd $i
	mkdir tm-align1
	~/softwares/tm-align/./TMalign $pdb1 $pdb2 -o sup -a > ./tm-align1/alignment
	mv sup* ./tm-align1/

	pdb3="/home/sidhant/Sidhanta/work/networks/dataset/madhusudan/monomers/working_dir/inputs/${file1}/${file1}_dom_2.pdb"
	pdb4="/home/sidhant/Sidhanta/work/networks/dataset/madhusudan/monomers/working_dir/inputs/${file2}/${file2}_dom_2.pdb"
	mkdir tm-align2
	~/softwares/tm-align/./TMalign $pdb3 $pdb4 -o sup -a > ./tm-align2/alignment
	mv sup* ./tm-align2/

	cd ..
done
