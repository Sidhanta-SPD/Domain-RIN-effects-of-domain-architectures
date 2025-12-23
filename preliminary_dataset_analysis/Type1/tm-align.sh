#!/bin/bash

for i in */
do
	file=${i:0:4}
	file1="/home/sidhant/Sidhanta/work/networks/dataset/madhusudan/monomers/working_dir/inputs/${file}/${file}_dom_1.pdb"
	file2="/home/sidhant/Sidhanta/work/networks/dataset/madhusudan/monomers/working_dir/inputs/${file}/${file}_dom_2.pdb"
	cd $i
	mkdir tm-align
	~/softwares/tm-align/./TMalign $file1 $file2 -o sup -a > ./tm-align/alignment
	mv sup* ./tm-align/
	cd ..
done
