#!/bin/bash

cd domains
for i in */
do
	file=${i:0:9}
	cd $file
	seq_id1=$(awk 'NR>6 {print}' ${file}"_dom1.pim"|tr -s ' '|cut -d ' ' -f 4|awk 'NR==2 {print}')
	seq_id2=$(awk 'NR>6 {print}' ${file}"_dom2.pim"|tr -s ' '|cut -d ' ' -f 4|awk 'NR==2 {print}')
	echo $file $seq_id1 $seq_id2
	cd ..
done
