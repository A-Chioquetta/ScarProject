import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.pxp_evolution import run_pxp_evolution
from utils.save_utils import save_results

import numpy as np


if __name__ == "__main__":
    # === Parameters ===
    N = 8                      # Number of sites
    state_name = 'Z2' # Initial state ('Z2', 'Z2_flip_up', 'Z3', etc.)
    boundary = 'PBC'             # 'PBC' or 'OBC'
    nt = 500                     # Number of time steps
    t_max = 20.0                 # Maximum evolution time

    # === Run evolution ===
    result = run_pxp_evolution(
        N=N,
        state_name=state_name,
        boundary=boundary,
        nt=nt,
        t_max=t_max
    )

    # === Save results ===
    output_dir = f"results/ResultsEvolution/PXP_{N}sites_{boundary}"
    filename = f"evolution_{N}sites_{state_name}_{boundary}.dat"
    header = "time correlation overlap_with_initial"

    save_results(
        result=(result['times'], result['correlation'], result['overlap']),
        output_dir=output_dir,
        filename=filename,
        header=header
    )
