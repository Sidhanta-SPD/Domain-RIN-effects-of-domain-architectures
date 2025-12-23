#!/bin/bash

cd domains
for i in */
do
	cd $i
	file=${i:0:9}
	cd tm-align1
	tm1=$(grep "TM-score=" alignment | grep "chains =" | cut -d ' ' -f 2)
	cd ../tm-align2
	tm2=$(grep "TM-score=" alignment | grep "chains =" | cut -d ' ' -f 2)
	echo $file $tm1 $tm2
	cd ../..
done
