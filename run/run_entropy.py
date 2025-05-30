import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.initial_states import get_initial_state
from models.pxp_perturbation import build_pxp_hamiltonian, add_perturbation
from utils.compute_entropy import compute_entropy
from utils.save_utils import save_results
from utils.plotting_utils import plot_fidelity_and_correlation
from qutip import sesolve
import numpy as np



# Parameters
N = 16
initial_state = 'Z2'
boundary = 'PBC'
t_max = 20
nt = 500
times = np.linspace(0, t_max, nt)

# Including perturbation: perturbation =True
perturbation = False
W_perturbation = 0.01
direction = 'all'
disorder = False
projected = True


# Output folder
output_folder = 'results/ResultsEntropy'
os.makedirs(output_folder, exist_ok=True)

# Initial state
psi0 = get_initial_state(initial_state, N)

# Hamiltonian
H = build_pxp_hamiltonian(N, boundary=boundary)

# Add perturbation
if perturbation:
    W = W_perturbation
    H = add_perturbation(H, N, W, direction=direction, disorder=disorder, projected=projected)
elif not perturbation:
    W = 0

# Time evolution
result = sesolve(H, psi0, times, [])

# Compute entropies over time
entropies = [compute_entropy(state, N) for state in result.states]

# Plot
plot_fidelity_and_correlation(
    times=times,
    fidelity=entropies,
    correlation=None,
    title=f'Entanglement entropy over time (N={N}, {boundary})',
    output_path=os.path.join(output_folder, f'entropy_N{N}_{boundary}_{initial_state}_W{W}.png')
)

# Save data
save_results(
    result=(times, entropies),
    output_dir=output_folder,
    filename=f'entropy_N{N}_{boundary}_{initial_state}_W{W}.csv',
    header="time entropy_log2"
)
