# ScarProject

Simulations of quantum many-body systems focusing on the PXP model, Rydberg chains, Schrieffer-Wolff (SW) corrections, and constrained subspace analysis.
This project includes dynamics, entanglement entropy calculations, overlap with eigenstates, and studies of projected and non-projected perturbations.

## 📂 Project Structure

```plaintext
ScarProject/
├── models/           # Hamiltonians, operators, and initial states
├── utils/            # Auxiliary functions (save, plot, entropy)
├── run/              # Executable scripts
├── tests/            # Test scripts and usage examples
├── results/          # Automatically generated data
│   ├── ResultsEvolution/
│   │   ├── PXP/
│   │   ├── PXPSW/
│   │   ├── Rydberg/
│   │   └── Perturbation/
│   ├── ResultsEntropy/
│   └── ResultsSubspace/
├── .vscode/          # VS Code settings (optional)
├── README.md         # This file
├── requirements.txt  # Dependencies
├── setup.py          # Optional installation as a package
```

## 🚀 How to Run

Run from the project root:

```bash
python run/run_pxp.py
python run/run_pxp_perturbation.py
python run/run_pxp_sw.py
python run/run_rydberg.py
python run/run_entropy.py
python run/run_overlap_plot.py
```

> ✅ **IMPORTANT:** Always run from the project root `ScarProject/`.  
> ✔️ If using VS Code, it works perfectly with the PLAY button if you have `.vscode/settings.json` configured or the magic line `sys.path.append()` at the top of the scripts.

## 🧠 Features

- ✅ PXP model time evolution
- ✅ PXP with projected and non-projected perturbations (X, Y, Z, or all directions)
- ✅ PXP with second-order Schrieffer-Wolff (SW) corrections
- ✅ Rydberg chain with blockade constraint
- ✅ Entanglement entropy calculation over time
- ✅ Overlap analysis between initial states and eigenstates in the constrained subspace
- ✅ Automatic data organization
- ✅ Publication-ready plotting tools

## 🧠 Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

Dependencies:

- numpy
- qutip
- matplotlib

## 🗃️ Data Organization

Data is automatically saved under `/results/`:

- 📁 `ResultsEvolution/`
    - 🔸 `PXP/`
    - 🔸 `PXPSW/`
    - 🔸 `Rydberg/`
    - 🔸 `Perturbation/`
- 📁 `ResultsEntropy/`
- 📁 `ResultsSubspace/`

## 🔧 Install as a Package (optional)

Install locally as a package if desired:

```bash
pip install .
```

## 👨‍💻 Author

- 🔬 Code development, organization, and simulations by **Alessandra Chioquetta**.

## 📜 License

MIT License — free to use, modify, and contribute.

> ✔️ **Note:** This project is professionally structured to be replicable, scalable, and ready for academic use (thesis, paper, presentation) and public repositories such as GitHub and PyPI.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15531770.svg)](https://doi.org/10.5281/zenodo.15531770)