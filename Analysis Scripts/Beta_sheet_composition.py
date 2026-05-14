import pandas as pd
from scipy import stats
import numpy as np
from scipy.stats import f_oneway, kruskal

def dssp_blah():
    filename = '/Users/kushalpatil/Desktop/studious-waffle/03_md/dat/secondary_structure.dat'

    try:
        df = pd.read_csv(filename, sep='\s+', comment='@', header=None)
        df = df[~df[0].astype(str).str.startswith('#')]
        
        structure_col = df.iloc[:, -1] 

        df['Helix_Count'] = structure_col.str.count('H')
        df['Sheet_Count'] = structure_col.str.count('E')
        
        df['Frame_Index'] = df.index 

        print("Secondary structure mapped successfully!")


        native_candidates = df[(df['Helix_Count'] > df['Helix_Count'].median()) & (df['Sheet_Count'] == 0)]
        

        toxic_candidates = df[df['Sheet_Count'] > 0].sort_values(by='Sheet_Count', ascending=False)

        def get_diverse_frames(subset, label):
            if subset.empty:
                return f"No {label} frames found."
            indices = np.linspace(0, len(subset) - 1, 3).astype(int)
            return subset.iloc[indices]['Frame_Index'].tolist()

        print(f"\nTarget Alpha-Helix Frames (Indices): {get_diverse_frames(native_candidates, 'Helix')}")
        print(f"Target Beta-Sheet Frames (Indices): {get_diverse_frames(toxic_candidates, 'Sheet')}")

    except Exception as e:
        print(f"An error occurred: {e}")

def cohen_d(t_stat1):
    # Data from your VQE analysis
    t_stat = "blah"  # Replace with t-stat
    n_arctic = 3
    n_wt = 3

    # Calculate Cohen's d
    cohens_d = t_stat * np.sqrt((1/n_arctic) + (1/n_wt))

    print(f"Cohen's d: {cohens_d:.4f}")

    # Interpretation logic
    if cohens_d > 0.8:
        print("Interpretation: Large Effect Size")
    elif cohens_d > 0.5:
        print("Interpretation: Medium Effect Size")
    else:
        print("Interpretation: Small Effect Size")
def delta_e():
    delta_E_UCCSD = [0.01983, -0.00861, -0.0486]  
    delta_E_TwoLocal = [-0.161, -0.338, 0.0772]  
    delta_E_EfficientSU2 = [-0.11]  
    delta_E_B3LYP = [0.02, 0.03, 0.01]
    delta_E_CASCI = [0.04, 0.02, 0.01]

    h_stat, p_value = kruskal(delta_E_UCCSD, delta_E_TwoLocal,
                          delta_E_EfficientSU2, delta_E_B3LYP, delta_E_CASCI)

    print(f"p-value: {p_value}")
#dssp_blah()
#t_stat = t_test_analysis()
#cohen_d(t_stat)
#delta_e()
