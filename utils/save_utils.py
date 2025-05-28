import numpy as np
import os

def save_results(
    result,
    output_dir,
    filename,
    header=None,
    W=None
):
    """
    Save simulation results to a file, optionally adding W as a column.

    Parameters
    ----------
    result : tuple or dict
        Tuple (times, values) or dict with 'times', 'correlation', 'overlap'/‘fidelity’.
    output_dir : str
        Directory where the file will be saved.
    filename : str
        Name of the output file.
    header : str, optional
        Header for the file.
    W : float, optional
        Value of W to add as a column (if given).
    """
    os.makedirs(output_dir, exist_ok=True)

    if isinstance(result, dict):
        times = result['times']
        col1 = result['correlation']
        col2 = result.get('overlap', result.get('fidelity'))
    else:
        times, col1 = result
        col2 = None

    if W is not None:
        W_col = np.full_like(times, W)
        if col2 is not None:
            data = np.column_stack((times, col1, col2, W_col))
        else:
            data = np.column_stack((times, col1, W_col))
    else:
        if col2 is not None:
            data = np.column_stack((times, col1, col2))
        else:
            data = np.column_stack((times, col1))

    np.savetxt(os.path.join(output_dir, filename), data, header=header, comments='')
    print(f"Saved to {os.path.join(output_dir, filename)}")
