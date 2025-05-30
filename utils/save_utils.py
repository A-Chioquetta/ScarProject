import numpy as np
import os

def save_results(result, output_dir, filename, header="", W=None):
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)

    # Handle dictionary input (e.g., {'times': ..., 'fidelity': ..., 'correlation': ...})
    if isinstance(result, dict):
        data = np.column_stack([result[key] for key in result])
        if W is not None:
            W_column = np.full(len(result[list(result.keys())[0]]), W)
            data = np.column_stack((data, W_column))
            header += " W" if header else "W"

    # Handle direct ndarray or tuple/list input
    else:
        data = np.array(result)
        if W is not None:
            if data.ndim == 1:
                data = np.column_stack((data, np.full_like(data, W)))
            elif data.ndim == 2:
                W_column = np.full((data.shape[0], 1), W)
                data = np.hstack((data, W_column))
                header += " W" if header else "W"

    np.savetxt(filepath, data, header=header, comments='')
    print(f"Saved to {filepath}")
