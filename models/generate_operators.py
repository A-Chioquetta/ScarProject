from qutip import qeye, sigmax, sigmay, sigmaz, sigmap, sigmam, tensor


def generate_operators(N, ops_to_generate='all'):
    """
    Generate local operators for a spin-1/2 chain of size N.

    Parameters
    ----------
    N : int
        Number of spins.
    ops_to_generate : list of str or 'all'
        List of operators to generate. Possible options are:
        ['sx', 'sy', 'sz', 'sp', 'sm', 'p', 'q']
        or 'all' to generate everything.

    Returns
    -------
    dict
        Dictionary where keys are operator names and values are lists of qutip.Qobj operators.
    """
    # Define local operators
    si = qeye(2)
    sx = sigmax()
    sy = sigmay()
    sz = sigmaz()
    sp = sigmap()
    sm = sigmam()
    p = (si - sz) / 2.0
    q = (si + sz) / 2.0

    # Operator dictionary template
    local_ops = {
        'sx': sx,
        'sy': sy,
        'sz': sz,
        'sp': sp,
        'sm': sm,
        'p': p,
        'q': q
    }

    # If 'all', generate everything
    if ops_to_generate == 'all':
        ops_to_generate = list(local_ops.keys())

    # Validate input
    valid_ops = set(local_ops.keys())
    if not set(ops_to_generate).issubset(valid_ops):
        raise ValueError(
            f"Invalid operator requested. Valid options are {valid_ops}"
        )

    # Build tensor products
    operators = {}
    for op_name in ops_to_generate:
        op_list = []
        for n in range(N):
            tensor_list = [si] * N
            tensor_list[n] = local_ops[op_name]
            op_list.append(tensor(tensor_list))
        operators[op_name] = op_list

    return operators
