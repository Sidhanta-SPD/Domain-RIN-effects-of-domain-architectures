#!/bin/bash
#$1=*aligned_res
#$2=*dom_1.deg
#$3=*dom_2.deg
#usage: paralle -j 40 < something.job

cat $1|while read -r i j k l m n
do
	awk 'NR>1 {print}' $2|while read -r i1 j1 k1 l1
	do
		awk 'NR>1 {print}' $3|while read -r i2 j2 k2 l2
		do
			if [[ $i == $k1 ]] && [[ $k == $j1 ]] && [[ $l == $k2 ]] && [[ $n == $j2 ]]
			#added chain match criteria for previous case3. Now, the following line is not needed.	
			#if [[ $i == $k1 ]] && [[ $k == $j1 ]] && [[ $l == $k2 ]] && [[ $n == $j2 ]] && [[ $j == $i1 ]] && [[ $m == $i2 ]]
			then
				echo $i $j $k $l $m $n $l1 $l2 $(($l1-$l2))
			fi
		done
	done
done
