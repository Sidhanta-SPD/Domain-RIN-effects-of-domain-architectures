awk 'NR>1 {print}' nox_outputs | awk '{
if ($2 >=70)
print $0,"obl";
else if ($3 >=70)
print $0, "non_obl";
}'
