
from qutip import sesolve, Options
import numpy as np
from models.generate_operators import generate_operators
from models.initial_states import get_initial_state


def build_pxp_sw_hamiltonian(N, W, V=10.0, boundary='PBC'):
    """
    Build the PXP Hamiltonian with Schrieffer-Wolff second order correction.
    """
    ops = generate_operators(N)
    sx_list = ops['sx']
    p_list = ops['p']
    sp_list = ops['sp']
    sm_list = ops['sm']

    Omega = np.random.uniform(W * 0.97, W * 1.03, N)

    H = 0

    for n in range(N - 2):
        H += (Omega[n] / 2) * p_list[n] * sx_list[n + 1] * p_list[n + 2]

    if boundary.lower() == 'pbc':
        H += (Omega[N - 2] / 2) * p_list[N - 2] * sx_list[N - 1] * p_list[0]
        H += (Omega[N - 1] / 2) * p_list[N - 1] * sx_list[0] * p_list[1]
    elif boundary.lower() == 'obc':
        H += (Omega[0] / 2) * sx_list[0] * p_list[1]
        H += (Omega[N - 1] / 2) * p_list[N - 2] * sx_list[N - 1]

    for n in range(N - 3):
        factor = (Omega[n + 1] * (Omega[n] + Omega[n + 2])) / (8 * V)
        H += factor * p_list[n] * sp_list[n + 1] * sm_list[n + 2] * p_list[n + 3]
        H += factor * p_list[n] * sm_list[n + 1] * sp_list[n + 2] * p_list[n + 3]

    boundary_terms = [
        (N - 3, N - 2, N - 1, 0),
        (N - 2, N - 1, 0, 1),
        (N - 1, 0, 1, 2)
    ]
    for i, j, k, l in boundary_terms:
        factor = (Omega[i] * (Omega[j] + Omega[k])) / (8 * V)
        H += factor * p_list[i] * sp_list[j] * sm_list[k] * p_list[l]
        H += factor * p_list[i] * sm_list[j] * sp_list[k] * p_list[l]

    return H


def run_pxp_evolution_with_sw(N, state_name, W, V=10.0, boundary='PBC',
                               t_max=20.0, nt=500):
    """
    Run time evolution for the PXP + SW Hamiltonian.
    """
    ops = generate_operators(N)
    sz_list = ops['sz']

    psi0 = get_initial_state(state_name, N)

    H = build_pxp_sw_hamiltonian(N, W, V=V, boundary=boundary)

    corr = sum([sz_list[i] * sz_list[i + 1] for i in range(N - 1)]) / (N - 1)
    if boundary.lower() == 'pbc':
        corr += sz_list[N - 1] * sz_list[0] / (N - 1)

    times = np.linspace(0, t_max, nt)

    options = Options(store_states=True, method='adams')

    result = sesolve(H, psi0, times, [corr], options=options)

    fidelity = [np.abs(psi0.overlap(state)) ** 2 for state in result.states]

    return {
        'times': times,
        'correlation': np.array(result.expect[0]),
        'fidelity': np.array(fidelity),
        'states': result.states
    }
