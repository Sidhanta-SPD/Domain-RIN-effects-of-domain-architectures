#!/bin/bash

for i in */
do
	file=${i:0:4}
	cd ${file}/tm-align
	tm=$(grep "TM-score=" alignment | grep "chains =" | cut -d ' ' -f 2)
	echo $file $tm
	cd ../..
done
