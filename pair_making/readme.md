# creation of pairs for comparisons.  

**grouping.py** --- py to pull pdbs satisfying the rules. Extract the pdb entries from *../dataset/nox_domain_details2* to match the rules of each type.  

### Naming conventions. Old namings are founds in codes while current namings are found in article.  

|Old naming  |	Current naming |  
|------------|----------------|    
| Case3 | Type2 |  
| Case2 | Type3 |  
| Case1 | Type1 |  

**Type subtyping is mentioned as case2_1, case2_2, etc. accroding to rules.**  
**pairing.py** ---py to pair up culled pdbs according to CATH domain ids. In this study till 'H' is compared.  
__*pairs.txt__ --- pair of pdbs to compare written in each line. Format: header of each file.  
**case1** --- pairs for type1 class (current naming)  
 
**Command for looking into peculiar pairs**  
`awk '{split($2,a,"."); split($5,b,"."); if (a[1]==b[1]) && a[2]==b[2] && a[3]==b[3] && a[4]==b[4]) print $0}' case2_1_pairs.txt`
