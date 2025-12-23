import pandas as pd
from Bio.PDB import *
import sys


parser=PDBParser()
#file=parser.get_structure('3p2w', '3p2w_dom_1.pdb')
input_pdb=sys.argv[1]
file=parser.get_structure(input_pdb[0:4],input_pdb)
residues=list(list(file[0])[0].get_residues())#all residues

#residues=file.get_residues()
#residues=Selection.unfold_entities(file,'R')
#list(file[0])[0][100]#100th residue of the chain or
#file[0]["A"][100]
#residue.get_id()
#residue.get_full_id()
#residue.get_resname()
#residue.get_list()
#residue.get_unpacked_list()
#atoms=list(file[0]["A"][100].get_atoms())
#atoms[0]get_id()
#atoms[0].get_name()
#for more help http://biopython.org/DIST/docs/tutorial/Tutorial.html#:~:text=An%20Atom%20object%20has%20the%20following%20additional%20methods%3A
#atom.get_serial_number()

#Bio.PDB package takes care of MO and alt locations. By default it takes highest occupancy
#````````````
chain_id=[]#chain id
res_no1=[]#residue number
resname1=[]#residue name
res_no2=[]
resname2=[]
n_ij=[]#The number of atom pairs which are closer than 4.5A in non-adjacent residues
for resi1 in residues:
    for resi2 in residues:
        if resi1.get_id()[0][0]=='H' or resi2.get_id()[0][0]=='H' or resi1.get_id()[0]=='W' or resi2.get_id()[0]=='W':#removing hetero residues or water
            continue
        else:
            res1_id=resi1.get_id()[1]
            res2_id=resi2.get_id()[1]
            if res1_id == res2_id or abs(res1_id-res2_id)==1:#not pairing same residue and adjacent residues
                continue
            else:
                #res1_atoms=resi1.get_list()#list of atoms in a list
                #res2_atoms=resi2.get_list()
                res1_atoms=[k for k in resi1.get_list() if k.get_name()[0]!='H']#considering non-hydrogen atoms
                res2_atoms=[k for k in resi2.get_list() if k.get_name()[0]!='H']
                dists=[i-j for i in res1_atoms for j in res2_atoms]#taking distances of all atom pairs
                n_ij.append(len([x for x in dists if x<=4.5]))
                chain_id.append(resi1.get_full_id()[2])
                
                res_no1.append(res1_id)
                resname1.append(resi1.get_resname())
                
                res_no2.append(res2_id)
                resname2.append(resi2.get_resname())
            
df=pd.DataFrame({'Chain':chain_id,'Res1_id':res_no1,'Resname1':resname1,'Res2_id':res_no2,'Resname2':resname2,'n_ij':n_ij})
#print(df)
df=df[df.n_ij!=0]#taking only connected residues
#df.to_csv(input_pdb[0:10]+'.ntf',sep=' ',index=False)#commented for precaution
