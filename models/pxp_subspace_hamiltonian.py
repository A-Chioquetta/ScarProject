
from qutip import Qobj
import numpy as np


def build_pxp_hamiltonian_direct_in_subspace(N, basis_strings, boundary='PBC'):
    dim = len(basis_strings)
    H = np.zeros((dim, dim), dtype=complex)

    for i, state in enumerate(basis_strings):
        bits = list(state)

        for site in range(N):
            left = (site - 1) % N
            right = (site + 1) % N

            if boundary.lower() == 'obc':
                left_valid = True if site == 0 else bits[left] == '0'
                right_valid = True if site == N - 1 else bits[right] == '0'
            elif boundary.lower() == 'pbc':
                left_valid = bits[left] == '0'
                right_valid = bits[right] == '0'
            else:
                raise ValueError("Boundary must be 'PBC' or 'OBC'.")

            if left_valid and right_valid:
                flipped_bits = bits.copy()
                flipped_bits[site] = '0' if bits[site] == '1' else '1'
                flipped_str = ''.join(flipped_bits)

                if flipped_str in basis_strings:
                    j = basis_strings.index(flipped_str)
                    H[i, j] += 1.0

    return Qobj(H)
