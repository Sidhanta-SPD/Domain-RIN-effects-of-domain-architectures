#!/bin/bash
cd case3_2
echo 'Pair Preserved Changed'
for i in *dd
do
	preserved=$(grep 'Preserved' $i|wc -l)
	changed=$(grep 'Changed' $i|wc -l)

	echo ${i%_dd} $preserved $changed
done
