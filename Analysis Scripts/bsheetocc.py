import numpy as np
import MDAnalysis as mda

def calculate_beta_sheet_occupancy(pdb_file):
    """
    Calculates the percentage of residues falling into the 
    beta-sheet region of the Ramachandran plot.
    """
    # Load the structure
    u = mda.Universe(pdb_file)
    
    phi_angles = []
    psi_angles = []
    
    # Iterate through residues to extract dihedrals
    for res in u.residues:
        try:
            phi = res.phi_selection()
            psi = res.psi_selection()
            
            if phi is not None and psi is not None:
                phi_angles.append(phi.dihedral.value())
                psi_angles.append(psi.dihedral.value())
        except Exception:
            continue
    
    phi_vals = np.array(phi_angles)
    psi_vals = np.array(psi_angles)
    

    beta_mask = (phi_vals >= -180) & (phi_vals <= -90) & \
                (psi_vals >= 90) & (psi_vals <= 180)
    
    beta_count = np.sum(beta_mask)
    total_residues = len(phi_vals)
    
    occupancy_pct = (beta_count / total_residues) * 100
    
    return occupancy_pct

structures = {
    'Arctic_Set': '/path/to/arctic_structure.pdb',
    'WT_Set': '/path/to/wt_structure.pdb',
}

for name, path in structures.items():
    pct = calculate_beta_sheet_occupancy(path)
    print(f"{name} Beta-Sheet Occupancy: {pct:.10f}%")