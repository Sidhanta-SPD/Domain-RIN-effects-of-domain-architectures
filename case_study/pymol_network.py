import pandas as pd

# Load the adjacency matrix
adj_matrix_file = "./2fbo_dom_2.adj_mat"
pdb_file = "./sasa/2fbo_dom_2.pdb"
output_script_file = "dom2_network.pml"
obj_name='dom2'

# Read the adjacency matrix as a DataFrame
adj_matrix = pd.read_csv(adj_matrix_file, delim_whitespace=True, index_col=0)

# Create a PyMOL script to visualize the matrix
with open(output_script_file, 'w') as script:
    # Start the PyMOL script
    script.write("from pymol import cmd\n")
    script.write(f"cmd.load('{pdb_file}', '{obj_name}')\n")

    # Iterate through the adjacency matrix and create lines and spheres for non-zero entries
    for col in adj_matrix.columns:
        chain1, resi1, resn1 = col.split("_")
        
        for index, value in adj_matrix[col].items():
            if value != 0:
                chain2, resi2, resn2 = index.split("_")

                # Draw a line between the two residues
                line_name = f"line_{chain1}_{resi1}_{chain2}_{resi2}"
                script.write(
                    f"cmd.distance('{line_name}', "
                    f"'/{obj_name}///{resi1}/CA', "
                    f"'/{obj_name}///{resi2}/CA')\n"
                )
                script.write("cmd.group('all_distances', '{}')\n".format(line_name))
        
    # Finalize the script
    script.write("cmd.hide('lines', '{obj_name}')\n")
    script.write("cmd.hide('labels')\n")
    script.write("cmd.show('cartoon', '{obj_name}')\n")
    script.write("cmd.set('dash_gap', 0)\n")
    script.write("cmd.set('dash_width', 0.5)\n")
    script.write("cmd.set('dash_color', 'black')\n")

# Provide the path of the generated PyMOL script
output_script_file
