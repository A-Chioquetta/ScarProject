
from qutip import Qobj, sesolve, Options
import numpy as np
from models.generate_operators import generate_operators
from models.initial_states import get_initial_state



def build_rydberg_hamiltonian(N, sx_list, q_list, V=10.0, Omega=1.0, boundary='PBC'):
    """
    Build the Rydberg chain Hamiltonian.
    """
    H = 0

    for n in range(N - 1):
        H += V * q_list[n] * q_list[n + 1]

    for n in range(N):
        H += Omega * sx_list[n]

    if boundary.lower() == 'pbc':
        H += V * q_list[N - 1] * q_list[0]

    return H



def run_rydberg_evolution(N, state_name, boundary='PBC',
                           V=10.0, Omega=1.0,
                           t_max=20, nt=500):
    """
    Run Rydberg chain evolution.
    """
    ops = generate_operators(N)
    sx_list = ops['sx']
    sz_list = ops['sz']
    q_list = ops['q']

    psi0 = get_initial_state(state_name, N)

    H = build_rydberg_hamiltonian(N, sx_list, q_list, V=V, Omega=Omega, boundary=boundary)

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