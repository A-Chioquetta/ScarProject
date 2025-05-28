import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.initial_states import get_initial_state
import numpy as np


def qobj_to_string(state, N):
    """
    Convert a Qobj state vector into a string like 'ududdd...'

    Parameters
    ----------
    state : qutip.Qobj
        The state vector.
    N : int
        Number of spins.

    Returns
    -------
    str
        String representation with 'u' for up and 'd' for down.
    """
    basis_states = [format(i, '0{}b'.format(N)) for i in range(2**N)]
    coeffs = state.full().flatten()

    index = np.argmax(np.abs(coeffs))
    bitstring = basis_states[index]

    # Map '0' -> 'u' and '1' -> 'd'
    spin_string = ''.join(['u' if b == '0' else 'd' for b in bitstring])
    return spin_string


if __name__ == "__main__":
    N = 12  # Change as needed
    states_to_test = [
        'Z0',
        'Z2',
        'Z2_flip_down',
        'Z2_flip_up',
        'Z3',
        'Z3_flip_down',
        'Z3_flip_up',
    ]

    for state_name in states_to_test:
        state = get_initial_state(state_name, N)
        string_repr = qobj_to_string(state, N)
        print(f"{state_name}: {string_repr}")
