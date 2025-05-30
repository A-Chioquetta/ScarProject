
from qutip import Qobj
import numpy as np


def generate_initial_state(N, basis_strings, pattern='Z2', defect_position=None):
    """
    Gera um estado inicial no subespaço.

    Parameters
    ----------
    N : int
        Número de spins.
    basis_strings : list of str
        Lista dos bitstrings do subspace.
    pattern : str
        Tipo de estado ('Z2', 'Z2_shifted', 'Z0', 'Z1', etc.).
    defect_position : int or None
        Posição do spin a ser flipado (se relevante).

    Returns
    -------
    qutip.Qobj
        Estado no subspace.
    str
        Bitstring do estado gerado.
    """

    if pattern.lower() == 'z2':
        bitstring = ''.join(['0' if i % 2 == 0 else '1' for i in range(N)])
    elif pattern.lower() == 'z2_shifted':
        bitstring = ''.join(['1' if i % 2 == 0 else '0' for i in range(N)])
    elif pattern.lower() == 'z0':
        bitstring = '0' * N
    elif pattern.lower() == 'z1':
        bitstring = '1' * N
    else:
        raise ValueError(f"Unknown pattern {pattern}")

    if defect_position is not None:
        bits = list(bitstring)
        bits[defect_position] = '0' if bits[defect_position] == '1' else '1'
        bitstring = ''.join(bits)

    if bitstring not in basis_strings:
        raise ValueError(f"State {bitstring} is not in the subspace!")

    index = basis_strings.index(bitstring)
    vec = np.eye(len(basis_strings))[:, index]

    return Qobj(vec.reshape(-1, 1)), bitstring
