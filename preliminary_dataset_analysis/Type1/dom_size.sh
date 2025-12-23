#!/bin/bash

for i in */
do
	file=${i:0:4}
	cd $file/tm-align
	l_1=$(grep "Length" alignment | cut -d ':' -f 2| tr -s ' ' | cut -d ' ' -f 2|awk 'NR==1 {print}')
	l_2=$(grep "Length" alignment | cut -d ':' -f 2| tr -s ' ' | cut -d ' ' -f 2|awk 'NR==2 {print}')
	aln_len=$(grep "^Aligned length=" alignment | tr -s ' ' | cut -d ' ' -f 3|cut -d ',' -f 1)
	min=$((l_1 < l_2 ? l_1 : l_2)) #to get the min value
	cov=$(awk "BEGIN {print $aln_len/$min}") #division using awk
	echo $file $l_1 $l_2 $cov
	cd ../..
done
