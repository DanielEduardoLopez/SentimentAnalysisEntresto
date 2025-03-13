"""
Collection of functions for making charts.
"""

# Libraries importation
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib_inline.backend_inline
import seaborn as sns

# Setting theme and plot resolution
sns.set_theme(context = 'notebook', style = 'darkgrid')
mpl.rcParams["figure.dpi"] = 100
mpl.rcParams["savefig.dpi"] = 300
matplotlib_inline.backend_inline.set_matplotlib_formats('svg')

# Setting default plot's aesthetics
plotfontcolor = 'dimgray'
mpl.rcParams['text.color'] = plotfontcolor
mpl.rcParams['axes.labelcolor'] = plotfontcolor
mpl.rcParams['xtick.color'] = plotfontcolor
mpl.rcParams['ytick.color'] = plotfontcolor
mpl.rcParams["font.size"] = 10
mpl.rcParams['axes.titlesize'] = 14
mpl.rcParams['axes.labelsize'] = 12
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['legend.fontsize'] = 11
mpl.rcParams["axes.labelweight"] = "bold"
mpl.rcParams["axes.titleweight"] = "bold"


# Functions

def process_string(input_string: str) -> str:
    """
    Process an input string to conver it to lowercase, remove blank spaces and punctuation signs.

    Parameters:
    input_string (str): Raw string.    

    Returns:
    output_string (str): Processed string.
    """

    char_dict = {'á': 'a',
                'é': 'e',
                'í': 'i',
                'ó': 'o',
                'ú': 'u',
                '^': '',
                '.': '',
                ' ': '_'}

    translation_table = str.maketrans(char_dict)

    output_string = input_string.lower().translate(translation_table)

    return output_string


def return_color_list(data: pd.DataFrame, column: str) -> list:
    """
    Return a list of colors for a given column in a DataFrame, 
    with the first column being blue and the rest gray.

    Parameters:

    data (pd.DataFrame): Input data.
    column (str): Column name.

    Returns:
    color_list (list): List of colors.
    """
    
    color_list = [sns.color_palette('Blues')[-1] if i == 0 else 'gray' for i in range(len(data[column].unique()))]

    return color_list


def plot_barchart(data: pd.DataFrame, x: str, y: str, ylabel: str, xlabel: str, title: str) -> None:
    """
    Plots and saves in disk a barchart with the data provided.

    Parameters:
    data (pd.DataFrame): Input data.
    x (str): Column name for x axis.
    y (str): Column name for y axis.
    
    Returns:
    None

    """

    # Drawing base plot
    fig = plt.figure(figsize=(8,5))
    ax = sns.barplot(data, 
                    x=x, 
                    y=y, 
                    palette=return_color_list(data, x),
                    alpha=0.7)

    # Adding data labels for each bar
    for label in range(len(ax.containers)):
        ax.bar_label(ax.containers[label], label_type='edge', padding=3)
    ax.margins(y=0.1)

    # Adding title and labels
    title_adj = process_string(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.savefig(f'../reports/figures/fig_{title_adj}.png', bbox_inches = 'tight')
    plt.show()

