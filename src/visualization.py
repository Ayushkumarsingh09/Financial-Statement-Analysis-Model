import matplotlib.pyplot as plt


def plot_trend(data, title, xlabel, ylabel, output_path):
    """
    Plot a trend and save it as an image.

    Args:
        data (pd.Series): Data to plot.
        title (str): Chart title.
        xlabel (str): X-axis label.
        ylabel (str): Y-axis label.
        output_path (str): Path to save the chart.
    """
    plt.figure(figsize=(10, 6))
    data.plot(kind="line", marker="o")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid()
    plt.savefig(output_path)
    plt.close()
