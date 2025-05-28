
from itertools import product
from qutip import basis, tensor


def generate_pxp_subspace(N, boundary='PBC'):
    basis_states = []
    basis_strings = []

    for bits in product('01', repeat=N):
        bitstring = ''.join(bits)

        if boundary.lower() == 'pbc':
            condition = '11' not in (bitstring + bitstring[0])
        elif boundary.lower() == 'obc':
            condition = '11' not in bitstring
        else:
            raise ValueError("Boundary must be 'PBC' or 'OBC'.")

        if condition:
            basis_strings.append(bitstring)
            state = tensor([basis(2, 0) if b == '0' else basis(2, 1) for b in bitstring])
            basis_states.append(state)

    return basis_states, basis_strings
