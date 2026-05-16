import pandas as pd
from scipy import stats
import numpy as np
from scipy.stats import f_oneway, kruskal

def delta_e():
    delta_E_UCCSD = [0.01983, -0.00861, -0.0486]  
    delta_E_TwoLocal = [-0.161, -0.338, 0.0772]  
    delta_E_EfficientSU2 = [-0.11]  
    delta_E_B3LYP = [0.02, -0.01, -0.05]  
    delta_E_CASCI = [0.01, 0.03, 0.04]

    h_stat, p_value = kruskal(delta_E_UCCSD, delta_E_TwoLocal,
                          delta_E_EfficientSU2, delta_E_B3LYP, delta_E_CASCI)

    print(f"p-value: {p_value}")
    print(f"H-statistic: {h_stat}")
delta_e()
