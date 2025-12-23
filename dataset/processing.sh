#!/bin/bash
#This script extracts the percentages

cd inputs
for i in *;
do
	cd $i/NOXclass/python_scripts/
	obl=$(grep -A1 'Obligate' nox_out_${i} | awk 'NR==2 {print $2}')
	n_obl=$(grep  -A1 'Non-obligate' nox_out_${i} | awk 'NR==2 {print $3}')
	bio=$(grep  -A1 'Biological' nox_out_${i} | awk 'NR==2 {print $2}')
	n_bio=$(grep  -A1 'Non-biological' nox_out_${i} | awk 'NR==2 {print $3}')
	echo $i $obl $n_obl $bio $n_bio
	cd ../../../
done

