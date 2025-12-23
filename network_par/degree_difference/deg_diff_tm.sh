#!/bin/bash
#usage: bash deg_diff_tm.sh >> var_tm

echo "Pair Var TM RMSD Hue" #only for first run

cd case3/dom1 #change
for pair in $(cat ../../keep_dom1); #change
do
	alignment="/home/sidhant/Sidhanta/work/networks/cases/case3_files/domains/${pair}/tm-align1/alignment" #change
	var=$(awk '{sumsq+=$9*$9; sum+=$9} END{print sumsq/NR-(sum/NR)^2}' ${pair}_dd)
	rmsd=$(grep 'RMSD=' ${alignment} |tr -s ' '| cut -d ' ' -f 5|cut -d ',' -f 1)
	tm=$(grep "TM-score=" ${alignment} | grep "chains =" | cut -d ' ' -f 2)
	echo $pair $var $tm $rmsd "Case3" #change
done

cd ../dom2
for pair in $(cat ../../keep_dom2); #change
do
	alignment="/home/sidhant/Sidhanta/work/networks/cases/case3_files/domains/${pair}/tm-align2/alignment" #change
	var=$(awk '{sumsq+=$9*$9; sum+=$9} END{print sumsq/NR-(sum/NR)^2}' ${pair}_dd)
	rmsd=$(grep 'RMSD=' ${alignment} |tr -s ' '| cut -d ' ' -f 5|cut -d ',' -f 1)
	tm=$(grep "TM-score=" ${alignment} | grep "chains =" | cut -d ' ' -f 2)
	echo $pair $var $tm $rmsd "Case3" #change
done

cd ../../case2_1
for pair in $(cat ../case2_1_order); #change
do
	alignment="/home/sidhant/Sidhanta/work/networks/cases/case2_files/case2_1/${pair}/tm-align/alignment" #change
	var=$(awk '{sumsq+=$9*$9; sum+=$9} END{print sumsq/NR-(sum/NR)^2}' ${pair}_dd)
	rmsd=$(grep 'RMSD=' ${alignment} |tr -s ' '| cut -d ' ' -f 5|cut -d ',' -f 1)
	tm=$(grep "TM-score=" ${alignment} | grep "chains =" | cut -d ' ' -f 2)
	echo $pair $var $tm $rmsd "Case2" #change
done

cd ../case2_2
for pair in $(cat ../case2_2_order); #change
do
	alignment="/home/sidhant/Sidhanta/work/networks/cases/case2_files/case2_2/${pair}/tm-align/alignment" #change
	var=$(awk '{sumsq+=$9*$9; sum+=$9} END{print sumsq/NR-(sum/NR)^2}' ${pair}_dd)
	rmsd=$(grep 'RMSD=' ${alignment} |tr -s ' '| cut -d ' ' -f 5|cut -d ',' -f 1)
	tm=$(grep "TM-score=" ${alignment} | grep "chains =" | cut -d ' ' -f 2)
	echo $pair $var $tm $rmsd "Case2" #change
done

cd ../case2_3
for pair in $(cat ../case2_3_order); #change
do
	alignment="/home/sidhant/Sidhanta/work/networks/cases/case2_files/case2_3/${pair}/tm-align/alignment" #change
	var=$(awk '{sumsq+=$9*$9; sum+=$9} END{print sumsq/NR-(sum/NR)^2}' ${pair}_dd)
	rmsd=$(grep 'RMSD=' ${alignment} |tr -s ' '| cut -d ' ' -f 5|cut -d ',' -f 1)
	tm=$(grep "TM-score=" ${alignment} | grep "chains =" | cut -d ' ' -f 2)
	echo $pair $var $tm $rmsd "Case2" #change
done

cd ../case2_4
for pair in $(cat ../case2_4_order); #change
do
	alignment="/home/sidhant/Sidhanta/work/networks/cases/case2_files/case2_4/${pair}/tm-align/alignment" #change
	var=$(awk '{sumsq+=$9*$9; sum+=$9} END{print sumsq/NR-(sum/NR)^2}' ${pair}_dd)
	rmsd=$(grep 'RMSD=' ${alignment} |tr -s ' '| cut -d ' ' -f 5|cut -d ',' -f 1)
	tm=$(grep "TM-score=" ${alignment} | grep "chains =" | cut -d ' ' -f 2)
	echo $pair $var $tm $rmsd "Case2" #change
done

cd ../case1
for pair in $(cat ../case1_order); #change
do
	alignment="/home/sidhant/Sidhanta/work/networks/cases/case1_files/${pair}/tm-align/alignment" #change
	var=$(awk '{sumsq+=$9*$9; sum+=$9} END{print sumsq/NR-(sum/NR)^2}' ${pair}_dd)
	rmsd=$(grep 'RMSD=' ${alignment} |tr -s ' '| cut -d ' ' -f 5|cut -d ',' -f 1)
	tm=$(grep "TM-score=" ${alignment} | grep "chains =" | cut -d ' ' -f 2)
	echo $pair $var $tm $rmsd "Case1" #change1
done
