#!/bin/bash
for i in case2*/
do
	cd $i
	for j in */
	do
		file=${j:0:9}
		cd $file
		seq_id=$(awk 'NR>6 {print}' ${file}.pim|tr -s ' '|cut -d ' ' -f 4|awk 'NR==2 {print}')
		echo $file $seq_id
		cd ..
	done
	cd ..
done
