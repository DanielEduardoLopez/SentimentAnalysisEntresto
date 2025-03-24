"""
Collection of functions for making charts.
"""

# Libraries importation
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib_inline.backend_inline
import seaborn as sns
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

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
    
    color_list = [sns.color_palette('Blues')[-1] if i == 0 else 'lightgray' for i in range(len(data[column].unique()))]
    color_list.insert(1, 'gray')

    return color_list


def plot_barchart(data: pd.DataFrame, x: str, y: str, ylabel: str, xlabel: str, title: str) -> None:
    """
    Plots and saves in disk a barchart with the data provided.

    Parameters:
    data (pd.DataFrame): Input data.
    x (str): Column name for x axis.
    y (str): Column name for y axis.
    ylabel (str): Label for y axis.
    xlabel (str): Label for x axis.
    title (str): Chart title.
    
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


def plot_donutchart(data: pd.DataFrame, x: str, y: str, title: str) -> None:
    """
    Plots and saves in disk a piechart with the data provided.

    Parameters:
    data (pd.DataFrame): Input data.
    column (str): Column name for x axis.
    title (str): Chart title.
    
    Returns:
    None

    """

    fig, ax = plt.subplots(figsize = (8, 5))
    colors = sns.color_palette('Blues_r')
    wedges, texts, autotexts = ax.pie(x = data[y].values, 
                                    #labels = count_by_sentiment.sentiment.values,
                                    wedgeprops=dict(edgecolor='w', linewidth= 2, alpha=0.8),
                                    textprops = dict(size=14, weight="bold"), 
                                    colors = return_color_list(data, x), #[colors[0], 'gray', 'lightgray'], 
                                    autopct='%.0f%%', 
                                    pctdistance=1.15, 
                                    startangle = 90, 
                                    counterclock = False,                                   
                                    #explode = [0.01, 0.01, 0.01]
                                    )
    center = plt.Circle( (0,0), 0.7, color='white')
    p = plt.gcf()
    p.gca().add_artist(center)
    plt.legend(wedges, 
                data[x].values, 
                fontsize=13, 
                #loc="center right", 
                bbox_to_anchor=(1, 0, 0.3, 0.8)
                )
    plt.tight_layout()
    title_adj = process_string(title)
    plt.savefig(f'../reports/figures/fig_{title_adj}.png',  bbox_inches = 'tight')
    plt.show()


def plot_word_cloud(text: pd.Series, title: str, remove_stopwords: bool = False) -> None:
    """
    Plots and saves into disk a Word Cloud from a Pandas series.

    Parameters:
    text (pd.series): Pandas series with text strings.
    title (str): Chart title.
    remove_stopwords (bool): Flag to remove or not the stop words from the output word cloud.

    Returns:
    None 

    """

    words_flatten = text.str.split().explode().tolist()
    all_text = ' '.join(words_flatten)

    if remove_stopwords:
        wordcloud = WordCloud(width = 3000, height = 1500,
                            background_color ='white',
                            #mask = maskArray,      
                            stopwords = stopwords.words('english'),
                            min_font_size = 10)

    else:
        wordcloud = WordCloud(width = 3000, height = 1500,
                            background_color ='white',
                            #mask = maskArray,                                  
                            min_font_size = 10)
    
    wordcloud.generate(all_text)

    plt.figure(figsize = (10, 8)) 
    plt.imshow(wordcloud) 
    plt.axis("off") 
    plt.tight_layout(pad = 0) 

    title_adj = process_string(title)
    plt.savefig(f'../reports/figures/fig_{title_adj}.png')
    plt.show()