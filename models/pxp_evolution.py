from qutip import sesolve, Options, Qobj
import numpy as np
from models.initial_states import get_initial_state
from models.generate_operators import generate_operators


def build_pxp_hamiltonian(N, boundary='PBC'):
    """
    Construct the PXP Hamiltonian for a spin-1/2 chain.

    Parameters
    ----------
    N : int
        Number of spins.
    boundary : str
        'PBC' for periodic boundary conditions or 'OBC' for open.

    Returns
    -------
    qutip.Qobj
        The PXP Hamiltonian.
    """
    ops = generate_operators(N, ops_to_generate=['sx', 'p'])
    sx_list = ops['sx']
    p_list = ops['p']

    H = 0
    for n in range(N - 2):
        H += p_list[n] * sx_list[n + 1] * p_list[n + 2]

    if boundary.lower() == 'pbc':
        H += p_list[N - 2] * sx_list[N - 1] * p_list[0]
        H += p_list[N - 1] * sx_list[0] * p_list[1]

    elif boundary.lower() == 'obc':
        H += sx_list[0] * p_list[1]
        H += p_list[N - 2] * sx_list[N - 1]

    else:
        raise ValueError("Boundary condition must be 'PBC' or 'OBC'.")

    return H


def run_pxp_evolution(N, state_name, boundary='PBC', nt=500, t_max=20.):
    """
    Run time evolution under the PXP Hamiltonian.

    Parameters
    ----------
    N : int
        Number of spins.
    state_name : str
        Initial state name (e.g. 'Z2', 'Z2_flip_up').
    boundary : str
        Boundary conditions ('PBC' or 'OBC').
    nt : int
        Number of time steps.
    t_max : float
        Maximum evolution time.

    Returns
    -------
    dict
        Contains 'times', 'overlap', 'correlation', and 'states'.
    """
    # Operators
    ops = generate_operators(N, ops_to_generate=['sz'])
    sz_list = ops['sz']

    # Initial state
    psi0 = get_initial_state(state_name, N)

    # Hamiltonian
    H = build_pxp_hamiltonian(N, boundary=boundary)

    # Observable: average nearest-neighbor correlation
    corr = 0
    for n in range(N - 1):
        corr += sz_list[n] * sz_list[n + 1]
    corr /= (N - 1)

    # Time grid
    times = np.linspace(0, t_max, nt)

    # Time evolution
    result = sesolve(
    H, psi0, times, e_ops=[corr], 
    progress_bar=True,
    options=Options(store_states=True)
)
    states = result.states

    # Fidelity overlap with initial state
    overlap = [np.abs(psi0.overlap(psi_t)) ** 2 for psi_t in states]

    # Expectation value of the correlation
    correlation = result.expect[0]

    return {
        'times': times,
        'overlap': overlap,
        'correlation': correlation,
        'states': states
    }
