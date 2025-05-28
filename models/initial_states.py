from qutip import tensor, qeye, fock, sigmax
import numpy as np


# Local states
UP = fock(2, 0)
DOWN = fock(2, 1)


def build_flip_operators(N):
    """
    Create local sigma_x operators for each site in the chain.

    Parameters
    ----------
    N : int
        Number of spins in the chain.

    Returns
    -------
    list of qutip.Qobj
        List of sigma_x operators acting on each site.
    """
    sx = sigmax()
    si = qeye(2)
    sx_list = []

    for n in range(N):
        op_list = [si] * N
        op_list[n] = sx
        sx_list.append(tensor(op_list))

    return sx_list


def get_initial_state(state_name, N):
    """
    Generate initial states for the spin chain.

    Parameters
    ----------
    state_name : str
        Name of the initial state. Available options are:
        - 'Z0'                 : all spins down
        - 'Z2'                 : |Z2> = up down up down ...
        - 'Z2_flip_down'       : flip an up -> down (keeps the constrained subspace)
        - 'Z2_flip_up'         : flip a down -> up (breaks the constrained subspace)
        - 'Z3'                 : |Z3> = up down down up down down ...
        - 'Z3_flip_down'       : flip a down -> up (creates up-up, breaks the subspace)
        - 'Z3_flip_up'         : flip an up -> down (does not create up-up, stays in the subspace)
    N : int
        Number of spins in the chain.

    Returns
    -------
    qutip.Qobj
        The full initial state in the Hilbert space.
    """
    if N < 2:
        raise ValueError("N must be greater than 1.")

    sx_list = build_flip_operators(N)

    if state_name == 'Z0':
        state = tensor([DOWN] * N)

    elif state_name == 'Z2':
        state = tensor([
            UP if i % 2 == 0 else DOWN
            for i in range(N)
        ])

    elif state_name == 'Z2_flip_down':
        # Flip an UP -> DOWN (does not break the constrained subspace)
        base = get_initial_state('Z2', N)
        up_sites = [i for i in range(N) if i % 2 == 0]
        defect_site = up_sites[len(up_sites) // 2]  # central UP
        state = sx_list[defect_site] * base

    elif state_name == 'Z2_flip_up':
        # Flip a DOWN -> UP (creates up-up, breaks the constrained subspace)
        base = get_initial_state('Z2', N)
        down_sites = [i for i in range(N) if i % 2 == 1]
        defect_site = down_sites[len(down_sites) // 2]  # central DOWN
        state = sx_list[defect_site] * base

    elif state_name == 'Z3':
        pattern = []
        while len(pattern) < N:
            pattern += [UP, DOWN, DOWN]
        state = tensor(pattern[:N])

    elif state_name == 'Z3_flip_up':
        # Flip a DOWN -> UP (creates up-up, breaks the constrained subspace)
        base = get_initial_state('Z3', N)
        down_sites = [i for i in range(N) if (i % 3 != 0)]
        defect_site = down_sites[len(down_sites) // 2]  # central DOWN
        state = sx_list[defect_site] * base

    elif state_name == 'Z3_flip_down':
        # Flip an UP -> DOWN (does not break the constrained subspace)
        base = get_initial_state('Z3', N)
        up_sites = [i for i in range(N) if (i % 3 == 0)]
        defect_site = up_sites[len(up_sites) // 2]  # central UP
        state = sx_list[defect_site] * base

    else:
        raise ValueError(f"State '{state_name}' not recognized.")

    return state
