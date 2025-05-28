import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.generate_operators import generate_operators


def print_operator(op):
    """
    Helper function to print operator matrix in a readable form.
    """
    print(op.full())


if __name__ == "__main__":
    N = 1  # Number of spins

    # Generate all operators for N=2
    ops = generate_operators(N, ops_to_generate='all')

    print("\n=== sigma_x operators ===")
    for i, op in enumerate(ops['sx']):
        print(f"sigma_x at site {i}:")
        print_operator(op)

    print("\n=== sigma_z operators ===")
    for i, op in enumerate(ops['sz']):
        print(f"sigma_z at site {i}:")
        print_operator(op)

    print("\n=== p operators ===")
    for i, op in enumerate(ops['p']):
        print(f"p at site {i}:")
        print_operator(op)

    print("\n=== q operators ===")
    for i, op in enumerate(ops['q']):
        print(f"q at site {i}:")
        print_operator(op)

    print("\n=== sigma_plus operators ===")
    for i, op in enumerate(ops['sp']):
        print(f"sigma_plus at site {i}:")
        print_operator(op)

    print("\n=== sigma_minus operators ===")
    for i, op in enumerate(ops['sm']):
        print(f"sigma_minus at site {i}:")
        print_operator(op)

    print("\n=== sigma_y operators ===")
    for i, op in enumerate(ops['sy']):
        print(f"sigma_y at site {i}:")
        print_operator(op)
