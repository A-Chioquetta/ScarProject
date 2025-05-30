import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.subspace_tools import generate_pxp_subspace
from models.pxp_subspace_hamiltonian import build_pxp_hamiltonian_direct_in_subspace
from models.initial_states_subspace import generate_initial_state
from utils.save_utils import save_results
from utils.plotting_utils import plot_overlap_scatter


from qutip import Qobj
import numpy as np
import matplotlib.pyplot as plt


# Parameters
N = 18
boundary = 'PBC'
initial_state = 'Z0'

# Generate subspace
subspace, basis_strings = generate_pxp_subspace(N=N, boundary=boundary)

# Hamiltonian in subspace
H_sub = build_pxp_hamiltonian_direct_in_subspace(N=N, basis_strings=basis_strings, boundary=boundary)
eigenvals, eigenstates = H_sub.eigenstates()

# Initial state in subspace
psi_sub, string = generate_initial_state(N, basis_strings, pattern=initial_state, defect_position=None)
print(f"Initial state generated: {string}")

# Compute overlaps
overlaps = np.array([np.abs(ev.dag() * psi_sub) ** 2 for ev in eigenstates])

# Filter very small overlaps for plotting
threshold = 1e-10
filtered_overlaps = np.where(overlaps > threshold, overlaps, np.nan)


# Save data
save_folder = 'results/ResultsSubspace'
os.makedirs(save_folder, exist_ok=True)

output_data = np.column_stack((eigenvals, overlaps, np.log2(overlaps)))

save_results(
    result=output_data,
    output_dir=save_folder,
    filename=f'overlap_data_N{N}_{boundary}_{initial_state}.dat',
    header="Eigenenergy Overlap Log2(Overlap)"
)

print(f"File saved to {save_folder}/overlap_data_N{N}_{boundary}_{initial_state}.dat")


# Plot
plot_overlap_scatter(
    eigenvals=eigenvals,
    log_overlaps=np.log2(filtered_overlaps),
    title=f'Log2 Overlap with eigenstates (N={N}, {boundary})',
    output_path=os.path.join(save_folder, f'overlap_plot_N{N}_{boundary}_{initial_state}.png')
)
