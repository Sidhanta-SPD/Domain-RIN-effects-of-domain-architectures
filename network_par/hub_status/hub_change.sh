#!/bin/bash
cd ../deg_change/case3/dom2

for i in *dd
do
	awk '$7>=11 || $8>=11 {if ($7>=11 && $8>=11) {$9="Preserved"} else {$9="Changed"} print}' $i > ../../../hub_change/case3_2/$i
done
