import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.subspace_tools import generate_pxp_subspace, embed_subspace_state_to_full
from models.pxp_subspace_hamiltonian import build_pxp_hamiltonian_direct_in_subspace
from utils.compute_entropy import compute_entropy
from utils.save_utils import save_results
from utils.plotting_utils import plot_entropy_vs_energy

from qutip import Qobj

import numpy as np
import os

# Parameters
N = 10
boundary = 'PBC'

# Generate subspace
subspace, basis_strings = generate_pxp_subspace(N=N, boundary=boundary)

# Hamiltonian in subspace
H_sub = build_pxp_hamiltonian_direct_in_subspace(N=N, basis_strings=basis_strings, boundary=boundary)
eigenvals, eigenstates = H_sub.eigenstates()


eigenstates_full = [
    embed_subspace_state_to_full(state, basis_strings=basis_strings, N=N)
    for state in eigenstates
]

# Compute entropy for each eigenstate
entropies = [compute_entropy(Qobj(state), N) for state in eigenstates_full]

# Save results
save_folder = 'results/ResultsSubspace/Entropy'
os.makedirs(save_folder, exist_ok=True)

output_data = np.column_stack((eigenvals, entropies))
save_results(
    result=output_data,
    output_dir=save_folder,
    filename=f'entropy_eigenstates_subspace_N{N}_{boundary}.dat',
    header="eigenenergy entropy_log2"
)

# Plot
plot_entropy_vs_energy(
    eigenenergies=eigenvals,
    entropies=entropies,
    title=f'Entropy of eigenstates in subspace (N={N}, {boundary})',
    output_path=os.path.join(save_folder, f'entropy_plot_subspace_N{N}_{boundary}.png')
)
