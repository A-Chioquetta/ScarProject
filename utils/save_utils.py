import os
import numpy as np


def save_results(result, output_dir, filename, header):
    """
    Save results to a CSV or .dat file.

    Parameters
    ----------
    result : list or array
        Data to be saved (typically np.column_stack with time, correlation, fidelity, etc.)
    output_dir : str
        Directory where the file will be saved.
    filename : str
        Name of the output file.
    header : str
        Header for the file columns.
    """
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)

    np.savetxt(filepath, result, header=header)
    print(f"Saved to {filepath}")
