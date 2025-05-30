import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.rydberg_hamiltonian import run_rydberg_evolution
from utils.save_utils import save_results

import numpy as np



if __name__ == "__main__":
    # Parameters
    N = 18
    state_name = 'Z2'
    boundary = 'PBC'
    nt = 500
    t_max = 20.0
    V = 10.0
    Omega = 2.0

    # Run simulation
    result = run_rydberg_evolution(
        N=N,
        state_name=state_name,
        boundary=boundary,
        nt=nt,
        t_max=t_max,
        V=V,
        Omega=Omega
    )

    # Save results
    output_dir = f"results/ResultsEvolution/Rydberg_{N}sites_{boundary}"
    filename = f"evolution_{N}sites_{state_name}_{boundary}_W{Omega}.dat"
    header = "time correlation fidelity"

    save_results(
        result={
        'times': result['times'],
        'correlation': result['correlation'],
        'overlap': result['fidelity']
    },
        output_dir=output_dir,
        filename=filename,
        header=header,
        W=Omega
    )
