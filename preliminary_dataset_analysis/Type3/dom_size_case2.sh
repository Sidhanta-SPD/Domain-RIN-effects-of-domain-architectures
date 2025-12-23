#!/bin/bash
#this calculates dom size differences and alignment coverage

for i in case2*/
do
	cd $i
	for j in */
	do
		file=${j:0:9}
		cd $file/tm-align
		l_1=$(grep "Length" alignment | cut -d ':' -f 2|tr -s ' '|cut -d ' ' -f 2|awk 'NR==1 {print}')
		l_2=$(grep "Length" alignment | cut -d ':' -f 2| tr -s ' ' | cut -d ' ' -f 2|awk 'NR==2 {print}')
		aln_len=$(grep "^Aligned length=" alignment | tr -s ' ' | cut -d ' ' -f 3|cut -d ',' -f 1)
		min=$((l_1 < l_2 ? l_1 : l_2)) #to get the min value
		cov=$(awk "BEGIN {print $aln_len/$min}") #division using awk
		echo $file $l_1 $l_2 $cov
		cd ../..
	done
	cd ..
done
