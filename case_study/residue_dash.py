import pymol
from pymol import cmd

# Initialize PyMOL
pymol.finish_launching(['pymol', '-qc'])  # -qc for quiet and no GUI

def draw_lines_between_residue_pairs(pairs,col,val,dist_obj):
    """
    Draws lines between specified pairs of residues within the same object.

    :param pairs: List of tuples, where each tuple contains:
                  (object_name, resi1, resi2)
                  val: dash gap
                  dist_obj: object for storing the lines.
    """
    # Set global dash properties    
    cmd.set('dash_gap', val)#val=0:solid line;val=0.5: dashed
    cmd.set('dash_color', col)
    
    for i, (obj_name, resi1, resi2) in enumerate(pairs):
        # Define the selection for the two residues
        atom1 = f"{obj_name} and resi {resi1} and name CA"
        atom2 = f"{obj_name} and resi {resi2} and name CA"
        #deg_edge = f"deg_edge_{i+1}" #for saving each bond with a name
        
        # Draw the line (distance) between the specified atoms
        cmd.distance(dist_obj, atom1, atom2)
        
        # Hide the labels for the distance
        cmd.hide('labels', dist_obj)

#function to select other non-interacting residues
def other_non_interacting_res(residue_pairs):
    # Initialize a list to hold selection strings
    selection_strings = []

    # Loop through each tuple in the residue_pairs list
    for domain, res1, res2 in residue_pairs:
        # Extract the domain and residue numbers
        selection_strings.append(f"{domain} and resi {res2}")

    # Join all the selection strings with " or " (to create a combined selection)
    combined_selection = " or ".join(selection_strings)

    # Select the interacting residues
    cmd.select("interacting_res", combined_selection)

    # Invert the selection to select other non-interacting residues
    cmd.select("other_res", "not interacting_res")


# Load structure
cmd.load('sup_all_atm.pdb', 'dom1')
cmd.extract('dom2', "dom1 and chain B")



"""
# Example list of residue pairs. Blue color
residue_pairs1 = [
    ('dom1', 43, 102), ('dom1', 43, 103), ('dom1', 43, 104), ('dom1', 43, 105), ('dom1', 43, 49), ('dom1', 43, 80),
    ('dom1', 54, 56), ('dom1', 54, 74), ('dom1', 54, 77), ('dom1', 54, 84), ('dom1', 54, 85), ('dom1', 54, 89),
    ('dom1', 89, 58), ('dom1', 89, 57), ('dom1', 89, 72), ('dom1', 89, 73), ('dom1', 89, 74), ('dom1', 89, 86), ('dom1', 89, 92), ('dom1', 89, 28), ('dom1', 89, 54),
    ('dom1', 113, 5), ('dom1', 113, 30), ('dom1', 113, 116), ('dom1', 113, 118)
]

#cmd.set('dash_gap', 0)#val=0:solid line;val=0.5: dashed
#cmd.set('dash_color', 'red')
residue_pairs2 = [
    ('dom1', 43, 50), ('dom1', 43, 51), ('dom1', 43, 53), ('dom1', 43, 107), ('dom1', 43, 106), ('dom1', 43, 41),
    ('dom1', 54, 52), ('dom1', 54, 75), ('dom1', 54, 76), ('dom1', 54, 86), ('dom1', 54, 94), ('dom1', 54, 39), ('dom1', 54, 40), ('dom1', 54, 41),
    ('dom1', 89, 87), ('dom1', 89, 39), ('dom1', 89, 56),
    ('dom1', 113, 37), ('dom1', 113, 111), ('dom1', 113, 121)
    ]

#cmd.set('dash_gap', 0)#val=0:solid line;val=0.5: dashed
#cmd.set('dash_color', 'black')
residue_pairs3 = [
    ('dom1', 89, 69), ('dom1', 89, 91),
    ('dom1', 113, 3), ('dom1', 113, 33), ('dom1', 113, 115)
]

#cmd.set('dash_gap', 0.5)#val=0:solid line;val=0.5: dashed
#cmd.set('dash_color', 'blue')
residue_pairs4 = [
    ('dom1', 89, 93),
    ('dom1', 113, 34)
]#edges unique to the 2nd domain
"""

#-----------Showing all the edges
residue_pairs1=[('dom1', 43, 102), ('dom1', 43, 103), ('dom1', 43, 104), ('dom1', 43, 105), ('dom1', 43, 49), ('dom1', 43, 80),
('dom1', 54, 56), ('dom1', 54, 74), ('dom1', 54, 77), ('dom1', 54, 84), ('dom1', 54, 85), ('dom1', 54, 89),
('dom1', 89, 58), ('dom1', 89, 57), ('dom1', 89, 72), ('dom1', 89, 73), ('dom1', 89, 74), ('dom1', 89, 86), ('dom1', 89, 92), ('dom1', 89, 28), ('dom1', 89, 54),
('dom1', 113, 5), ('dom1', 113, 30), ('dom1', 113, 116), ('dom1', 113, 118),
('dom1', 43, 50), ('dom1', 43, 51), ('dom1', 43, 53), ('dom1', 43, 107), ('dom1', 43, 106), ('dom1', 43, 41),
('dom1', 54, 52), ('dom1', 54, 75), ('dom1', 54, 76), ('dom1', 54, 86), ('dom1', 54, 94), ('dom1', 54, 39), ('dom1', 54, 40), ('dom1', 54, 41),
('dom1', 89, 87), ('dom1', 89, 39), ('dom1', 89, 56),
('dom1', 113, 37), ('dom1', 113, 111), ('dom1', 113, 121),
('dom1', 89, 69), ('dom1', 89, 91),
('dom1', 113, 3), ('dom1', 113, 33), ('dom1', 113, 115),
]

residue_pairs2=[('dom2',174,187),('dom2',174,188),('dom2',174,190),('dom2',174,230),('dom2',174,229),('dom2',174,172),
               ('dom2',191,189),('dom2',191,200),('dom2',191,201),('dom2',191,211),('dom2',191,217),('dom2',191,170),('dom2',191,171),('dom2',191,172),
               ('dom2',214,212),('dom2',214,170),('dom2',214,193),('dom2',214,216),
               ('dom2',236,166),('dom2',236,168),('dom2',236,234),('dom2',236,242),
    ]

# Draw lines between the specified residue pairs
#draw_lines_between_residue_pairs(residue_pairs4,'blue',0.3,'obj4')
draw_lines_between_residue_pairs(residue_pairs1,'blue',0,'obj1')
draw_lines_between_residue_pairs(residue_pairs2,'red',0,'obj2')
#draw_lines_between_residue_pairs(residue_pairs3,'black',0,'obj3')
#then manually chang the colors of distance objects

other_non_interacting_res(residue_pairs1+residue_pairs2)

cmd.set('dash_color','blue','obj1')
cmd.set('dash_color','red','obj2')
cmd.select('high_deg1','dom1 and resi 43+54+89+113')
cmd.select('high_deg2','dom2 and resi 174+191+214+236')
#manually exlclude high_deg1 and 2 from selection other_res in pymol

# Save the session
session_file = 'session2.pse'  # Name of the session file
cmd.save(session_file)

# Terminate PyMOL session
pymol.cmd.quit()
