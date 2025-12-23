#!/bin/bash

rm case2_doms
rm case2_doms_uniqs
awk 'NR>1 {print $1, $4}' ../../cases/case2_1_pairs.txt| while read -r i j
do
	echo ${i}"_dom_1.deg" >> case2_doms
	echo ${j}"_dom_1.deg" >> case2_doms
done
awk 'NR>1 {print $1, $4}' ../../cases/case2_2_pairs.txt| while read -r i j
do
	echo ${i}"_dom_2.deg" >> case2_doms
	echo ${j}"_dom_2.deg" >> case2_doms
done
awk 'NR>1 {print $1, $4}' ../../cases/case2_3_pairs.txt|while read -r i j
do
	echo ${i}"_dom_1.deg" >> case2_doms
	echo ${j}"_dom_2.deg" >> case2_doms
done
awk 'NR>1 {print $1, $4}' ../../cases/case2_4_pairs.txt|while read -r i j
do
	echo ${i}"_dom_2.deg" >> case2_doms
	echo ${j}"_dom_1.deg" >> case2_doms
done
sort -u case2_doms > case2_doms_uniqs
