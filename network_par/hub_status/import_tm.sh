#!/bin/bash
#echo "Pair Changed Aln_len Hue" #for the first run only
sed -n '2,$p' case1_counts|while read -r pair pres chang; #change
do
	alignment="/home/sidhant/Sidhanta/work/networks/cases/case1_files/${pair}/tm-align/alignment" #change
	aln_len=$(grep "^Aligned length=" ${alignment} | tr -s ' ' | cut -d ' ' -f 3|cut -d ',' -f 1)


	echo $pair $chang $aln_len "Case1" #change
done
