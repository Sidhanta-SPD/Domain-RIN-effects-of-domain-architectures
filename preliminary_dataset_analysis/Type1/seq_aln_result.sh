#!/bin/bash

for i in */
do
	file=${i:0:4}
	cd $file
	seq_id=$(awk 'NR>6 {print}' ${file}.pim|tr -s ' '|cut -d ' ' -f 4|awk 'NR==2 {print}')
	echo $file $seq_id
	cd ..
done
