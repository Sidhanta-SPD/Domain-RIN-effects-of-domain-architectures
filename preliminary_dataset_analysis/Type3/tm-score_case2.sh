#!/bin/bash

for i in case2*/
do
	cd $i
	for j in */
	do
		file=${j:0:9}
		cd $file/tm-align
		tm=$(grep "TM-score=" alignment | grep "chains =" | cut -d ' ' -f 2)
		echo $file $tm
		cd ../..
	done
	cd ..
done
