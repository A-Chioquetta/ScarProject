
from qutip import sesolve, Options
import numpy as np
from models.initial_states import get_initial_state
from models.generate_operators import generate_operators


def build_pxp_hamiltonian(N, boundary='PBC'):
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


def add_perturbation(
    H, N, W, direction='x',
    disorder=False, projected=False
):
    directions = ['x', 'y', 'z'] if direction == 'all' else [direction]

    valid_dirs = {'x', 'y', 'z'}
    if not set(directions).issubset(valid_dirs):
        raise ValueError(f"Invalid direction: {direction}")

    ops = generate_operators(N, ops_to_generate=['sx', 'sy', 'sz', 'p'])
    op_map = {'x': ops['sx'], 'y': ops['sy'], 'z': ops['sz']}
    p_list = ops['p']

    for dir in directions:
        op_list = op_map[dir]

        if disorder:
            fields = np.random.uniform(-W / 2, W / 2, size=N)
        else:
            fields = np.full(N, W)

        for n in range(N):
            if projected:
                left = p_list[(n - 1) % N]
                right = p_list[(n + 1) % N]
                term = left * op_list[n] * right
            else:
                term = op_list[n]

            H += fields[n] * term

    return H


def run_pxp_evolution_with_perturbation(
    N, state_name, boundary='PBC',
    nt=500, t_max=20., W=0.0,
    direction='x', disorder=False, projected=False
):
    ops = generate_operators(N, ops_to_generate=['sz'])
    sz_list = ops['sz']

    psi0 = get_initial_state(state_name, N)
    H = build_pxp_hamiltonian(N, boundary=boundary)

    if W != 0.0:
        H = add_perturbation(H, N, W, direction=direction, disorder=disorder, projected=projected)

    corr = 0
    for n in range(N - 1):
        corr += sz_list[n] * sz_list[n + 1]
    corr /= (N - 1)

    times = np.linspace(0, t_max, nt)

    result = sesolve(
        H, psi0, times, e_ops=[corr],
        progress_bar=True,
        options=Options(store_states=True)
    )

    states = result.states
    if len(states) == 0:
        raise RuntimeError("No states were generated during evolution.")

    overlap = [np.abs(psi0.overlap(psi_t)) ** 2 for psi_t in states]
    correlation = result.expect[0]

    return {
        'times': times,
        'overlap': overlap,
        'correlation': correlation,
        'states': states
    }
