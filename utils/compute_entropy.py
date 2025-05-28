import numpy as np


def compute_entropy(state, N, partition_size=None):
    """
    Compute the entanglement entropy (log2) via Schmidt decomposition.

    Parameters
    ----------
    state : qutip.Qobj
        State vector in the full Hilbert space.
    N : int
        Number of qubits.
    partition_size : int or None
        Size of subsystem A. If None, defaults to N//2.

    Returns
    -------
    float
        Entanglement entropy (base 2).
    """
    if partition_size is None:
        partition_size = N // 2

    dim_A = 2 ** partition_size
    dim_B = 2 ** (N - partition_size)

    # Reshape the state vector into (dim_A, dim_B)
    data = state.full().reshape((dim_A, dim_B))

    # Compute singular values (Schmidt coefficients)
    schmidt_coeffs = np.linalg.svd(data, compute_uv=False)

    # Compute entanglement entropy
    probs = schmidt_coeffs ** 2
    probs = probs[probs > 1e-15]  # Remove zeros for stability
    entropy = -np.sum(probs * np.log2(probs))

    return entropy
