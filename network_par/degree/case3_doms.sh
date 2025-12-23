#!/bin/bash
#This code writes the degree file names of domain pairs in case3

rm case3_dom1 case3_dom2
for i in $(awk '{print $1}' ../../cases/case3_files/keep_dom1);
do
	pdb1=$(cut -d "_" -f 1 <<< $i)
	pdb2=$(cut -d "_" -f 2 <<< $i)
	echo ${pdb1}"_dom_1.deg" >> case3_dom1
	echo ${pdb2}"_dom_1.deg" >> case3_dom1
done

for j in $(awk '{print $1}' ../../cases/case3_files/keep_dom2);
do
	pdb1=$(cut -d "_" -f 1 <<< $j)
       	pdb2=$(cut -d "_" -f 2 <<< $i)
        echo ${pdb1}"_dom_2.deg" >> case3_dom2
        echo ${pdb2}"_dom_2.deg" >> case3_dom2
done

cat case3_dom1 case3_dom2 > case3_doms_uniqs
sort -u case3_doms_uniqs -o case3_doms_uniqs
