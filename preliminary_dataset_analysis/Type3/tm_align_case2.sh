#!/bin/bash
#performs structural superposition using TM-align.
#change parameters according to the case.

cd case2_4
for i in */
do
	file1=${i:0:4}
	file2=${i:5:4}
	echo $file1 $file2
	pdb1="/home/sidhant/Sidhanta/work/networks/dataset/madhusudan/monomers/working_dir/inputs/${file1}/${file1}_dom_2.pdb"
	pdb2="/home/sidhant/Sidhanta/work/networks/dataset/madhusudan/monomers/working_dir/inputs/${file2}/${file2}_dom_1.pdb"
	cd $i
	mkdir tm-align
	~/softwares/tm-align/./TMalign $pdb1 $pdb2 -o sup -a > ./tm-align/alignment
	mv sup* ./tm-align/
	cd ..
done
