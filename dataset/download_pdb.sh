#!/bin/sh

while read p;
do
	echo "by Sid"
	echo "$p"
	wget "https://files.rcsb.org/download/$p" -O $p
done < download_two_domains
#list is the list of pdb files
