import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.pxp_perturbation import build_pxp_hamiltonian, add_perturbation
from utils.compute_entropy import compute_entropy
from utils.save_utils import save_results
from utils.plotting_utils import plot_entropy_vs_energy

import numpy as np
import os

# Parameters
N = 10
boundary = 'PBC'

# Including perturbation: perturbation =True
perturbation = False
W_perturbation = 0.01
direction = 'all'
disorder = False
projected = True

# Output
output_dir = 'results/ResultsEntropy'
os.makedirs(output_dir, exist_ok=True)

# Build Hamiltonian and diagonalize
H = build_pxp_hamiltonian(N=N, boundary=boundary)
# Add perturbation
if perturbation:
    W = W_perturbation
    H = add_perturbation(H, N, W, direction=direction, disorder=disorder, projected=projected)
elif not perturbation:
    W = 0

eigenvals, eigenstates = H.eigenstates()

# Compute entropy for each eigenstate
entropies = [compute_entropy(state, N) for state in eigenstates]

# Save results
data = np.column_stack((eigenvals, entropies))
filename = f'entropy_eigenstates_N{N}_{boundary}_W{W}.dat'
header = "eigenenergy entropy_log2"
save_results(result=data, output_dir=output_dir, filename=filename, header=header)

# Plot using utility function
plot_entropy_vs_energy(
    eigenenergies=eigenvals,
    entropies=entropies,
    title=f'Entanglement Entropy of Eigenstates (N={N}, {boundary})',
    output_path=os.path.join(output_dir, f'entropy_eigenstates_N{N}_{boundary}_W{W}.png')
)
