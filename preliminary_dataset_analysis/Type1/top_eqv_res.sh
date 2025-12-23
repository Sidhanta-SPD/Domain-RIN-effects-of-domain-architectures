#!bin/bash

for i in */
do
	file=${i:0:4}
	cd $file/tm-align
	grep "^ATOM" sup.pdb|awk '{if (substr($0,22,1)=="A") print}'|cut -c 18-20,22,23-26 --output-delimiter ' '|tr -s ' ' > temp1
	grep "^ATOM" sup.pdb|awk '{if (substr($0,22,1)=="B") print}'|cut -c 18-20,22,23-26 --output-delimiter ' '|tr -s ' ' > temp2
	paste -d ' ' temp1 temp2 > aligned_res
	rm temp*
	cd ../..
done
