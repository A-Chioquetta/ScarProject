import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.pxp_perturbation import run_pxp_evolution_with_perturbation
from utils.save_utils import save_results

import numpy as np



if __name__ == "__main__":
    # Parameters
    N = 18
    state_name = 'Z2'
    boundary = 'PBC'
    nt = 500
    t_max = 20.0
    W_max = 0.1
    direction = 'all'       # 'x', 'y', 'z' or 'all'
    disorder = True        # True for random disorder, False for homogeneous
    projected = False       # True for projected perturbation

    W_values = np.arange(0.0, W_max + 0.01, 0.01)

    for W in W_values:
        print(f"Running for W = {W:.3f}")
        # Run simulation
        result = run_pxp_evolution_with_perturbation(
            N=N,
            state_name=state_name,
            boundary=boundary,
            nt=nt,
            t_max=t_max,
            W=W,
            direction=direction,
            disorder=disorder,
            projected=projected
        )
        # Save results
        proj_str = 'projected' if projected else 'unprojected'
        disorder_str = 'disorder' if disorder else 'homogeneous'

        output_dir = f"results/ResultsEvolution/PXP_{N}sites_{boundary}_{direction}_{disorder_str}_{proj_str}"
        filename = f"evolution_{N}sites_{state_name}_{boundary}_W{W:.3f}.dat"
        header = "time correlation overlap_with_initial"
        save_results(
        result={
        'times': result['times'],
        'correlation': result['correlation'],
        'overlap': result['overlap']
    },
        output_dir=output_dir, 
        filename=filename,
        header=header,
        W=W
    )

   

