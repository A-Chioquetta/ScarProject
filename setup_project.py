
import os


def create_folder_structure(base_dir="ScarProject"):
    folders = [
        f"{base_dir}/models",
        f"{base_dir}/utils",
        f"{base_dir}/run",
        f"{base_dir}/tests",
        f"{base_dir}/results/ResultsEvolution/PXP",
        f"{base_dir}/results/ResultsEvolution/PXPSW",
        f"{base_dir}/results/ResultsEvolution/Rydberg",
        f"{base_dir}/results/ResultsEvolution/Perturbation",
        f"{base_dir}/results/ResultsEntropy",
        f"{base_dir}/results/ResultsSubspace",
        f"{base_dir}/plots"
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Created folder: {folder}")

    for subfolder in ["models", "utils", "run", "tests"]:
        with open(f"{base_dir}/{subfolder}/__init__.py", "w") as f:
            f.write("# Init file for package\n")
        print(f"Created __init__.py in {subfolder}")


def create_readme(base_dir="ScarProject"):
    content = """
# ScarProject

This repository contains simulations of quantum many-body systems, focusing on the PXP model, Rydberg chains, and extensions with Schrieffer-Wolff corrections and perturbations.

## Project Structure

- `models/`: Hamiltonians, operators, initial states, and subspace tools.
- `utils/`: General tools like entropy computation, data saving, and plotting utilities.
- `run/`: Executable scripts to run the simulations.
- `results/`: Where all output data is saved, organized by model.
- `tests/`: Small scripts for testing operators, states, and functions.

## Running Simulations

Example for running PXP with SW corrections:

```bash
python run/run_pxp_sw.py
```

## Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```
"""
    with open(f"{base_dir}/README.md", "w") as f:
        f.write(content.strip())
    print("Created README.md")


def create_requirements(base_dir="ScarProject"):
    with open(f"{base_dir}/requirements.txt", "w") as f:
        f.write("numpy\nqutip\nmatplotlib\n")
    print("Created requirements.txt")


def create_utils_files(base_dir="ScarProject"):
    save_utils = """
import os
import numpy as np


def save_results(result, output_dir, filename, header):
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)

    data = np.column_stack(result)

    np.savetxt(filepath, data, header=header)
    print(f"Saved to {filepath}")
"""

    plotting_utils = """
import matplotlib.pyplot as plt


def plot_fidelity_and_correlation(times, fidelity, correlation, title, output_path=None):
    plt.figure(figsize=(10, 6))
    plt.plot(times, fidelity, label="Fidelity", lw=2)
    plt.plot(times, correlation, label="Correlation", lw=2)
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title(title)
    plt.legend()
    plt.grid()
    if output_path:
        plt.savefig(output_path, dpi=300, transparent=True)
        print(f"Plot saved to {output_path}")
    plt.show()
"""

    with open(f"{base_dir}/utils/save_utils.py", "w") as f:
        f.write(save_utils.strip())

    with open(f"{base_dir}/utils/plotting_utils.py", "w") as f:
        f.write(plotting_utils.strip())

    print("Created utils/save_utils.py and utils/plotting_utils.py")


if __name__ == "__main__":
    base_dir = "ScarProject"
    create_folder_structure(base_dir)
    create_readme(base_dir)
    create_requirements(base_dir)
    create_utils_files(base_dir)
    print("\n✅ Project setup complete.")
