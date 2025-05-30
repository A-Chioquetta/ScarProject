
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.subspace_tools import generate_pxp_subspace, project_operator_to_subspace, embed_subspace_state_to_full
from models.pxp_subspace_hamiltonian import build_pxp_hamiltonian_direct_in_subspace
from models.generate_operators import generate_operators
from utils.compute_entropy import compute_entropy
from utils.save_utils import save_results
from utils.plotting_utils import plot_entropy_vs_energy

from qutip import Qobj
import numpy as np

# Parameters
N = 14
boundary = 'PBC'
direction = 'all'   # 'x', 'y', 'z', or 'all'
W = 0.5            # Perturbation strength

# Generate subspace
subspace, basis_strings = generate_pxp_subspace(N=N, boundary=boundary)

# Build PXP Hamiltonian in subspace
H_sub = build_pxp_hamiltonian_direct_in_subspace(N=N, basis_strings=basis_strings, boundary=boundary)

# Add perturbation projected into subspace
if W!=0.0:
    ops_full = generate_operators(N, ops_to_generate=['sx', 'sy', 'sz'])
    op_map = {'x': ops_full['sx'], 'y': ops_full['sy'], 'z': ops_full['sz']}
    directions = ['x', 'y', 'z'] if direction == 'all' else [direction]
    fields = fields = np.random.uniform(-W / 2, W / 2, size=N)

    for dir in directions:
        for n in range(N):
            op = op_map[dir][n]
            op_proj = project_operator_to_subspace(op, basis_strings)
            H_sub += fields[n] * op_proj
        print(dir)
            

# Diagonalize Hamiltonian
eigenvals, eigenstates_sub = H_sub.eigenstates()


# Embed to full space
entropies = []

for state in eigenstates_sub:
    full_state = embed_subspace_state_to_full(state, basis_strings, N)
    entropy = compute_entropy(Qobj(full_state), N)
    entropies.append(entropy)
    


# Save results
save_folder = 'results/ResultsSubspace/Entropy'
os.makedirs(save_folder, exist_ok=True)

output_data = np.column_stack((eigenvals, entropies))
filename = f'entropy_eigenstates_subspace_perturbed_N{N}_{boundary}_W{W}.dat'
header = "eigenenergy entropy_log2"

save_results(
    result=output_data,
    output_dir=save_folder,
    filename=filename,
    header=header
)

# Plot
plot_entropy_vs_energy(
    eigenenergies=eigenvals,
    entropies=entropies,
    title=f'Entropy (perturbed subspace) - N={N}, {boundary}, W={W}',
    output_path=os.path.join(save_folder, f'entropy_plot_subspace_perturbed_N{N}_{boundary}_W{W}.png')
)
