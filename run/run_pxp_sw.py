
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.pxp_sw_evolution import run_pxp_evolution_with_sw
from utils.save_utils import save_results
import numpy as np



if __name__ == "__main__":
    # Parameters
    N = 8
    state_name = 'Z2'
    boundary = 'PBC'
    nt = 500
    t_max = 20.0
    V = 10.0
    W = 1.0

    # Run simulation
    result = run_pxp_evolution_with_sw(
        N=N,
        state_name=state_name,
        boundary=boundary,
        W=W,
        V=V,
        nt=nt,
        t_max=t_max
    )

    # Save results
    output_dir = f"results/ResultsEvolution/PXPSW_{N}sites_{boundary}"
    filename = f"evolution_{N}sites_{state_name}_{boundary}_W{W}.dat"
    header = "time correlation fidelity"

    save_results(
        result={
        'times': result['times'],
        'correlation': result['correlation'],
        'overlap': result['overlap']
    },
        output_dir=output_dir,
        filename=filename,
        header=header
    )
