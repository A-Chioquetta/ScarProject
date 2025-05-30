
from itertools import product
from qutip import basis, tensor, Qobj
import numpy as np


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


def embed_subspace_state_to_full(state_sub, basis_strings, N):
    """
    Embed a state vector from the subspace into the full Hilbert space.

    Parameters
    ----------
    state_sub : Qobj
        State vector in the subspace basis.
    basis_strings : list of str
        List of bitstrings representing the subspace basis.
    N : int
        Total number of sites (defines the full Hilbert space dimension 2^N).

    Returns
    -------
    Qobj
        State vector represented in the full Hilbert space.
    """
    dim_full = 2 ** N
    state_full = np.zeros(dim_full, dtype=complex)

    for i, bitstring in enumerate(basis_strings):
        index = int(bitstring, 2)
        state_full[index] = state_sub.full()[i, 0]

    return Qobj(state_full, dims=[[2] * N, [1]])


def project_operator_to_subspace(operator_full: Qobj, basis_full: list[list[int]]) -> Qobj:
    """
    Project a full Hilbert space operator onto a subspace defined by a list of basis states.

    Parameters
    ----------
    operator_full : Qobj
        Operator in the full Hilbert space (2^N-dimensional).
    basis_full : list of list of int
        List of basis vectors (bitstrings) defining the subspace. Each element is a list of 0s and 1s.

    Returns
    -------
    Qobj
        Operator projected onto the subspace.
    """
    
    dim = operator_full.shape[0]
    num_basis = len(basis_full)
    
    # Create a matrix to hold the projection
    projection_matrix = np.zeros((num_basis, dim), dtype=complex)

    for i, bitstring in enumerate(basis_full):
        # Convert bitstring to index in computational basis
        index = sum(int(bit) << (len(bitstring) - 1 - pos) for pos, bit in enumerate(bitstring))

        projection_matrix[i, index] = 1
    
    # Convert to Qobj
    P = Qobj(projection_matrix)
    operator_full = Qobj(operator_full.full(), dims=[[dim],[dim]])
    

    
    # Apply projection: H_sub = P H P^†
    H_sub = P @ operator_full @ P.dag()
    

    return H_sub