# Initialize dictionaries to store domain IDs for PDBs
pdb_to_cath1 = {}
pdb_to_cath2 = {}
cath1Full={}
cath2Full={}

# Read the input file
with open("case3", "r") as file:
    lines = file.readlines()

# Process each line and populate the dictionaries
for line in lines[1:]:  # Skip the header line
    pdb, cath1, cath2, ddi = line.strip().split()
    real_cath1 = '.'.join(cath1.split('.')[0:4])
    real_cath2 = '.'.join(cath2.split('.')[0:4])
    
    cath1Full[pdb]=cath1
    cath2Full[pdb]=cath2
    pdb_to_cath1[pdb] = real_cath1
    pdb_to_cath2[pdb] = real_cath2

# Initialize a set to store unique pairs of PDBs

unique_pairs = set()
#change the conditions based on case.

# Find pairs of PDBs based on your criteria
for pdb1 in pdb_to_cath1:
    for pdb2 in pdb_to_cath1:
        #if pdb1 != pdb2 and pdb_to_cath1[pdb1] == pdb_to_cath1[pdb2] and pdb_to_cath2[pdb1] != pdb_to_cath2[pdb2]:#case 2_1
        #if pdb1 != pdb2 and pdb_to_cath1[pdb1] != pdb_to_cath1[pdb2] and pdb_to_cath2[pdb1] == pdb_to_cath2[pdb2]:#case 2_2
        #if pdb1 != pdb2 and pdb_to_cath1[pdb1] == pdb_to_cath2[pdb2] and pdb_to_cath2[pdb1] != pdb_to_cath1[pdb2]:#case 2_3
        #if pdb1 != pdb2 and pdb_to_cath1[pdb1] != pdb_to_cath2[pdb2] and pdb_to_cath2[pdb1] == pdb_to_cath1[pdb2]:#case 2_4
        if pdb1 != pdb2 and pdb_to_cath1[pdb1] == pdb_to_cath1[pdb2] and pdb_to_cath2[pdb1] == pdb_to_cath2[pdb2]:#case 3
            pair = (pdb1, pdb2)
            if pair not in unique_pairs and (pair[1], pair[0]) not in unique_pairs:
                unique_pairs.add(pair)

"""
# Write the output to a new file. Change file name accordingly
with open("case3_pairs.txt", "w") as file:
    file.write("PDB1 CATH1 CATH2 PDB2 CATH1 CATH2\n")
    for pdb1, pdb2 in unique_pairs:
        file.write(f"{pdb1} {cath1Full[pdb1]} {cath2Full[pdb1]} {pdb2} {cath1Full[pdb2]} {cath2Full[pdb2]}\n")
"""