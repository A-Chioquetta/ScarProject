import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.generate_operators import generate_operators
from models.initial_states import get_initial_state


# Example: generate initial state Z2 for N=4
N = 2
state = get_initial_state('Z2', N)
print("Initial state |Z2> for N=4:")
print(state)

# Example: generate only sigma_x and sigma_z operators for N=4
ops = generate_operators(N, ops_to_generate=['sx', 'sz'])

# Access sigma_x at site 0
sx0 = ops['sx'][0]
print("\nSigma_x at site 0:")
print(sx0)

# Access sigma_z at site 1
sz1 = ops['sz'][1]
print("\nSigma_z at site 1:")
print(sz1)

# Generate all operators
all_ops = generate_operators(N, ops_to_generate='all')

print("\nAll available operators keys:")
print(list(all_ops.keys()))

# Example: generate initial state Z2_flip_up (which breaks the subspace)
state_defect = get_initial_state('Z2_flip_up', N)
print("\nInitial state |Z2_flip_up> for N=4:")
print(state_defect)
