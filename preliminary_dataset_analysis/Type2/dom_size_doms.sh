#!/bin/bash
rm dom_size_dom1
rm dom_size_dom2

cd domains
for i in */
do
	cd $i
	file=${i:0:9}
	cd tm-align1
	l_1=$(grep "Length" alignment | cut -d ':' -f 2|tr -s ' '|cut -d ' ' -f 2|awk 'NR==1 {print}')
	l_2=$(grep "Length" alignment | cut -d ':' -f 2|tr -s ' ' |cut -d ' ' -f 2|awk 'NR==2 {print}')
	aln_len=$(grep "^Aligned length=" alignment | tr -s ' ' | cut -d ' ' -f 3|cut -d ',' -f 1)
	min=$((l_1 < l_2 ? l_1 : l_2)) #to get the min value
	cov=$(awk "BEGIN {print $aln_len/$min}") #division using awk
	echo $file $l_1 $l_2 $cov >> ../../../dom_size_dom1
	
	cd ../tm-align2
	l_1=$(grep "Length" alignment | cut -d ':' -f 2|tr -s ' '|cut -d ' ' -f 2|awk 'NR==1 {print}')
        l_2=$(grep "Length" alignment | cut -d ':' -f 2|tr -s ' ' |cut -d ' ' -f 2|awk 'NR==2 {print}')
        aln_len=$(grep "^Aligned length=" alignment | tr -s ' ' | cut -d ' ' -f 3|cut -d ',' -f 1)
        min=$((l_1 < l_2 ? l_1 : l_2)) #to get the min value
        cov=$(awk "BEGIN {print $aln_len/$min}") #division using awk
        echo $file $l_1 $l_2 $cov >> ../../../dom_size_dom2

	cd ../..
done
