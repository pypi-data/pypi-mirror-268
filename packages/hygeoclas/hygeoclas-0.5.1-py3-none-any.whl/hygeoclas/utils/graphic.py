import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
import seaborn as sns

from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from matplotlib.ticker import FuncFormatter, MaxNLocator
from mpl_toolkits.axes_grid1 import make_axes_locatable
from scipy.interpolate import interp1d

from hygeoclas.fonts import cambria
from hygeoclas.utils.changeover import rgb_to_matplotlib

def plot_curve(ax, x, y, color, label, dotSize) -> None:
    """
    Plots a curve on a given axes.

    Args:
        ax (matplotlib.axes.Axes): The axes on which to plot the curve.
        x (np.ndarray): The x-coordinates of the points.
        y (np.ndarray): The y-coordinates of the points.
        color (tuple): The color of the curve.
        label (str): The label for the curve.
        dotSize (int): The size of the dots.
    """
    kind = "linear" if len(x) == 2 else "quadratic" if len(x) == 3 else "cubic"
    function = interp1d(x, y, kind=kind)
    xInterpolated = np.linspace(1, len(x), num=1000)
    yInterpolated = function(xInterpolated)
    ax.plot(xInterpolated, yInterpolated, color=color, label=label, zorder=1)
    ax.scatter(x, y, color=color, s=dotSize, edgecolors="white", linewidths=1, zorder=2)

def plot_train_validation_curve(trainLosses, validationLosses, **kwargs) -> None:
    """
    Plots the training and validation loss curves.

    Args:
        trainLosses (np.ndarray): The training losses.
        validationLosses (np.ndarray): The validation losses.

    Kwargs:
        fontFamily (str): The font family to use in the plot. Default is "Cambria".
        axisLabelNames (list): A list of two names for the axis labels. Default is ["Epoch", "Error"].
        legendLabelNames (list): A list of two names for the legend labels. Default is ["Training", "Validation"].
        fontSize (int): The font size to use in the plot. Default is 11.
        dotSize (int): The size of the dots. Default is 15.
        labelFontSize (int): The font size to use for the labels. Default is 12.
        numberFontSize (int): The font size to use for the numbers. Default is 10.
        legendFontSize (int): The font size to use for the legend. Default is 10.
        save (bool): If True, saves the figure to a file. Default is False.
        savePath (str): The path where the figure will be saved. Default is "./fig.png".
    """
    plt.rcParams["font.family"] = kwargs.get("fontFamily", "Cambria")
    plt.rcParams["font.size"] = kwargs.get("fontSize", 11)
    
    legendLabelNames =kwargs.get("legendLabelNames", ["Training", "Validation"])
    axisLabelNames = kwargs.get("axisLabelNames", ["Epoch", "Error"])
    dotSize = kwargs.get("dotSize", 15)
    labelFontSize = kwargs.get("labelFontSize", 12)

    red = rgb_to_matplotlib((136, 0, 21))
    blue = rgb_to_matplotlib((0, 2, 61))

    if len(trainLosses) == 1:
        print("Only one value was found in the losses, impossible to generate a training-validation curve.")
    else:
        fig, ax = plt.subplots()

        plot_curve(ax, np.linspace(1, len(trainLosses), len(trainLosses)), trainLosses, red, legendLabelNames[0], dotSize)
        plot_curve(ax, np.linspace(1, len(validationLosses), len(validationLosses)), validationLosses, blue, legendLabelNames[1], dotSize)

        ax.set_xlabel(axisLabelNames[0], fontsize=labelFontSize)
        ax.set_ylabel(axisLabelNames[1], fontsize=labelFontSize)
        ax.tick_params(axis="both", which="major", labelsize=kwargs.get("numberFontSize", 10))
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        
        sns.despine()
        for axis in ["bottom","left"]:
            ax.spines[axis].set_linewidth(1.2) 
        
        blueLine = Line2D([], [], color=red, marker='o', markersize=2, label='Entrenamiento')
        redLine = Line2D([], [], color=blue, marker='o', markersize=2, label='Validación')
        ax.legend(frameon=False, fontsize=kwargs.get("legendFontSize", 10), bbox_to_anchor=(1, 1.05), handles=[blueLine, redLine])

        if kwargs.get("save", False):
            fig.savefig(kwargs.get("savePath", "./fig.png"), dpi=300, bbox_inches="tight")

        plt.show()

def plot_database(compressedDatabase: pd.DataFrame, **kwargs) -> None:
    """
    This function generates plots from the data contained in a pandas DataFrame. 
    The plots represent the presence and absence of water in a compressed database.

    Parameters:
    compressedDatabase (pd.DataFrame): A pandas DataFrame containing the data to be plotted.
    **kwargs: Additional arguments for customizing the plots. Possible arguments are:
        - colors (list): A list of two colors for the plots. Default is ["gray", "blue"].
        - axisLabelNames (list): A list of two names for the axis labels. Default is ["Coefficient", "Amplitude"].
        - numberSize (int): The size of the numbers on the plots. Default is 10.
        - legendFontSize (int): The font size of the legend. Default is 9.
        - legendLabelNames (list): A list of two names for the legend labels. Default is ["NPoW", "PoW"].
        - fontFamily (str): The font family for the plots. Default is "Cambria".
        - fontSize (int): The font size for the plots. Default is 11.
        - formatterAx1 (str): The format of the y-axis for the first plot. Default is "normal".
        - formatterAx3 (str): The format of the y-axis for the third plot. Default is "normal".
        - saveFigures (bool): If True, saves the plots as .png files. Default is False.
        - savePaths (list): A list of three file paths to save the plots. Default is ["fig1.png", "fig2.png", "fig3.png"].

    Returns:
    None. Displays the plots and, if saveFigures is True, saves the plots at the specified paths.
    """
    data = {
        "NPoW": compressedDatabase[compressedDatabase["Label"] == 0],
        "PoW": compressedDatabase[compressedDatabase["Label"] == 1]
    }

    coefficients = np.arange(1, len(data["PoW"].mean()[1:])+1)
    formatters = {
        "normal": FuncFormatter(lambda y, _: "{:.16g}".format(y*1e-0)),
        "kilo": FuncFormatter(lambda y, _: "{:.16g}K".format(y*1e-3)),
        "mega": FuncFormatter(lambda y, _: "{:.16g}M".format(y*1e-6))
    }

    colors = kwargs.get("colors", ["gray", "blue"])
    axisLabelNames = kwargs.get("axisLabelNames", ["Coefficient", "Amplitude"])
    numberSize = kwargs.get("numberSize", 10)
    legendFontSize = kwargs.get("legendFontSize", 9)
    legendLabelNames = kwargs.get("legendLabelNames", ["NPoW", "PoW"])

    plt.rcParams["font.family"] = kwargs.get("fontFamily", "Cambria")
    plt.rcParams["font.size"] = kwargs.get("fontSize", 11)
    
    figs = []
    for i, (set, color) in enumerate(zip(["NPoW", "PoW"], colors)):
        fig, ax = plt.subplots()
        ax.fill_between(coefficients, data[set].min()[1:], data[set].max()[1:], color=color, alpha=0.3)
        ax.plot(coefficients, data[set].mean()[1:], color=color)
        ax.set_xlabel(axisLabelNames[0])
        ax.set_ylabel(axisLabelNames[1])
        ax.tick_params(axis="both", which="major", labelsize=numberSize)
        ax.yaxis.set_major_formatter(formatters[kwargs.get(f"formatterAx{i+1}", "normal")])
        sns.despine()
        figs.append(fig)

    fig3, ax = plt.subplots()
    for set, label, color in zip(["NPoW", "PoW"], legendLabelNames, colors):
        ax.fill_between(coefficients, data[set].min()[1:], data[set].max()[1:], color=color, alpha=0.3, label=label)
    ax.set_xlabel(axisLabelNames[0])
    ax.set_ylabel(axisLabelNames[1])
    ax.tick_params(axis="both", which="major", labelsize=numberSize)
    ax.yaxis.set_major_formatter(formatters[kwargs.get("formatterAx3", "normal")])
    legend = ax.legend(frameon=False, fontsize=kwargs.get("legendFontSize", 10), bbox_to_anchor=(1, 1.05))
    for handle in legend.legend_handles:
        handle.set_width(legendFontSize*2.25)
        handle.set_height(legendFontSize/2.75)
    sns.despine()
    figs.append(fig3)

    plt.show()

    if kwargs.get("saveFigures", False):
        savePaths = kwargs.get("savePaths", ["fig1.png", "fig2.png", "fig3.png"])
        for fig, savePath in zip(figs, savePaths):
            fig.savefig(f"{savePath}", dpi=300, bbox_inches="tight")

def plot_database_bars(compressedDatabase: pd.DataFrame, nPoWCountFromStructuredDB: int, poWCountFromStructuredDB: int, **kwargs) -> None:
    """
    Generates a bar chart comparing two databases.

    Args:
        compressedDatabase (pd.DataFrame): The compressed database.
        nPoWCountFromStructuredDB (int): The number of files for non water presence in the structured database.
        poWCountFromStructuredDB (int): The number of files for water presence in the structured database.

    Kwargs:
        fontFamily (str): The font to use in the chart. Default is "Cambria".
        fontSize (int): The font size to use in the chart. Default is 11.
        barLabels (list): The labels in vertical axis. Default ["PoA", "NPoA"].
        legendLabels (list): The labels for each bar in legend. Default ["Structured DB", "Compressed DB (NPoW)", "Compressed DB (PoW)"].
        saveFigure (bool): If True, saves the chart to a file. Default is False.
        savePath (str): The path where the chart will be saved. Default is "fig.png".

    Returns:
    None. Displays the bar and, if saveFigures is True, saves the bar at the specified paths.
    """
    plt.rcParams["font.family"] = kwargs.get("fontFamily", "Cambria")
    plt.rcParams["font.size"] = kwargs.get("fontSize", 11)

    barLabels = kwargs.get("barLabels", ["PoA", "NPoA"])
    legendLabels = kwargs.get("legendLabels", ["Structured DB", "Compressed DB (NPoW)", "Compressed DB (PoW)"])

    nPoWCount = compressedDatabase["Label"].value_counts().values[0]
    poWCount = compressedDatabase["Label"].value_counts().values[1]
    counts = {
        "Structured DB": np.array([poWCountFromStructuredDB, nPoWCountFromStructuredDB]),
        "Compressed DB": np.array([poWCount, nPoWCount]),
    }

    white = rgb_to_matplotlib((234, 234, 234))
    black = rgb_to_matplotlib((67, 67, 67))
    blue = rgb_to_matplotlib((72, 139, 202))
    colors = {
        "Structured DB": [white, white], 
        "Compressed DB": [blue, black],
    }

    fig, ax = plt.subplots(figsize=(3,1))
    for i, barLabel in enumerate(barLabels[::-1]):
        for databaseName, count in counts.items():
            p = ax.barh(barLabel, count[i], height=0.9, label=databaseName if i == 0 else "", color=colors[databaseName][i], edgecolor="black", linewidth=1.5)

    legendElements1 = [Patch(facecolor=white, edgecolor="black", label=legendLabels[0])]
    legendElements2 = [Patch(facecolor=black, edgecolor="black", label=legendLabels[1]),
                       Patch(facecolor=blue, edgecolor="black", label=legendLabels[2])]

    legend1 = ax.legend(handles=legendElements1, loc="upper right", bbox_to_anchor=(0.4, -0.25), frameon=False, fontsize=9)
    ax.legend(handles=legendElements2, loc="upper right", bbox_to_anchor=(1.15, -0.25), frameon=False, fontsize=9)
    ax.add_artist(legend1)

    if kwargs.get("save", False):
        savePath = kwargs.get("savePath", "fig.png")
        fig.savefig(f"{savePath}", dpi=300, bbox_inches="tight")

    sns.despine()
    plt.show()
    
def plot_confusion_matrix(confusionMatrix: np.ndarray, **kwargs) -> None:
    """
    Plots a confusion matrix using seaborn's heatmap.

    Args:
        confusionMatrix (np.ndarray): The confusion matrix to plot.

    Kwargs:
        fontFamily (str): The font family to use in the plot. Default is "Cambria".
        fontSize (int): The font size to use in the plot. Default is 18.
        tickLabelSize (int): The font size to use for the tick labels. Default is 12.
        figSize (tuple): The size of the confusion matrix. Default (1.6,1.2).
        annotSize (int): The font size of the annotations in the cells. Default 15.
        cBarLabelSize (int): The font size to use for the colorbar labels. Default is 12.
        save (bool): If True, saves the figure to a file. Default is False.
        savePath (str): The path where the figure will be saved. Default is "./fig.png".

    Note:
        This function uses seaborn's heatmap to plot the confusion matrix, and matplotlib's colorbar to add a colorbar to the right of the plot.
    """
    plt.rcParams["font.family"] = kwargs.get("fontFamily", "Cambria")
    plt.rcParams["font.size"] = kwargs.get("fontSize", 18)

    tickLabelSize = kwargs.get("tickLabelSize", 12)

    fig, ax = plt.subplots(figsize=kwargs.get("figSize", (1.6,1.2)))
    cax = sns.heatmap(confusionMatrix, annot=True, fmt=".0f", cmap=plt.cm.Blues, annot_kws={"size": kwargs.get("annotSize", 15)}, linewidths=0, ax=ax, cbar=False)

    for _, spine in ax.spines.items():
        spine.set_visible(True)
        spine.set_linewidth(1)

    ax.set_xticklabels(["NPdA", "PdA"], fontsize=tickLabelSize, rotation=67.5)
    ax.set_yticklabels(["NPdA", "PdA"], fontsize=tickLabelSize, rotation=0)

    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="20%", pad=0.1)
    cbar = fig.colorbar(ax.collections[0], cax=cax, orientation="vertical")

    minVal = confusionMatrix.min().min()
    maxVal = confusionMatrix.max().max()
    ticks = [minVal, int((minVal+maxVal)/3), int(2*(minVal+maxVal)/3), maxVal]
    cbar.set_ticks(ticks)
    cbar.set_ticklabels([str(tick) for tick in ticks])

    cbar.ax.tick_params(labelsize=kwargs.get("cBarLabelSize", 12))

    if kwargs.get("save", False):
        fig.savefig(kwargs.get("savePath", "./fig.png"), dpi=300, bbox_inches="tight")

    plt.show()

def plot_performance_scores(scores: list, **kwargs) -> None:
    """
    Plots the "Model Performance Scores Penalized by Variance".

    Args:
        scores (list): The performance scores to plot.

    Kwargs:
        fontFamily (str): The font family to use in the plot. Default is "Cambria".
        fontSize (int): The font size to use in the plot. Default is 11.
        axisLabelNames (list): A list of two names for the axis labels. Default is ["Cycle", "Score"]
        labelFontSize (int): The font size to use for the labels. Default is 12.
        numberFontSize (int): The font size to use for the numbers. Default is 10.
        dotSize (int): The size of the dots. Default is 15.
        save (bool): If True, saves the figure to a file. Default is False.
        savePath (str): The path where the figure will be saved. Default is "./fig.png".

    Note:
        This function uses seaborn's despine to remove the top and right spines from the plot.
    """
    plt.rcParams["font.family"] = kwargs.get("fontFamily", "Cambria")
    plt.rcParams["font.size"] = kwargs.get("fontSize", 11)

    axisLabelNames = kwargs.get("axisLabelNames", ["Cycle", "Score"])
    labelFontSize = kwargs.get("labelFontSize", 12)

    orange = rgb_to_matplotlib((240, 134, 80))

    fig, ax = plt.subplots()
    plot_curve(ax, np.linspace(1, len(scores), len(scores)), scores, orange, "", kwargs.get("dotSize", 15))

    ax.set_xlabel(axisLabelNames[0], fontsize=labelFontSize)
    ax.set_ylabel(axisLabelNames[1], fontsize=labelFontSize)
    ax.tick_params(axis="both", which="major", labelsize=kwargs.get("numberFontSize", 10))
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))

    sns.despine()
    for axis in ["bottom","left"]:
        ax.spines[axis].set_linewidth(1.2) 

    if kwargs.get("save", False):
        fig.savefig(kwargs.get("savePath", "./fig.png"), dpi=300, bbox_inches="tight")

    plt.show()