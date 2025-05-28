import matplotlib.pyplot as plt


def plot_fidelity_and_correlation(times, fidelity, correlation, title, output_path=None):
    """
    Plot fidelity and correlation over time.

    If correlation is None, only plots fidelity (e.g., entropy or any single curve).

    Parameters
    ----------
    times : array
        Time steps.
    fidelity : array
        Fidelity values or entropy values.
    correlation : array or None
        Correlation values over time. If None, only fidelity is plotted.
    title : str
        Title for the plot.
    output_path : str or None
        Path to save the plot as PNG. If None, plot is shown but not saved.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(times, fidelity, label="Fidelity/Entropy", lw=2)

    if correlation is not None:
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



def plot_overlap_scatter(eigenvals, log_overlaps, title, output_path=None):
    import matplotlib.pyplot as plt

    plt.figure(figsize=(8, 5))
    plt.scatter(eigenvals, log_overlaps, color='blue')
    plt.xlabel('Eigenenergy')
    plt.ylabel(r'$\log_{2}|\langle E_n | \psi_0 \rangle|^2$')
    plt.title(title)
    plt.grid()

    if output_path:
        plt.savefig(output_path, dpi=300, transparent=True)
        print(f"Plot saved to {output_path}")

    plt.show()
