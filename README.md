<p align="center">
	<img src="references/Header.png?raw=true" width=80% height=80%>
</p>

# Sentiment Analysis for Entresto&trade;
#### Daniel Eduardo López

<font size="-1"><a href="https://www.linkedin.com/in/daniel-eduardo-lopez">LinkedIn</a> | <a href="https://github.com/DanielEduardoLopez">GitHub </a></font>

**1 Apr 2025**

____
### **Contents**

1. [Introduction](#intro)<br>
2. [General Objective](#objective)<br>
3. [Research Question](#question)<br>
4. [Hypothesis](#hypothesis)<br>
5. [Methodology](#methodology)<br>
6. [Results](#results)<br>
	6.1 [Data Collection](#collection)<br>
	6.2 [Data Understanding](#exploration)<br>
	6.3 [Data Preparation](#preparation)<br>
  	6.4 [Exploratory Data Analysis](#eda)<br>
	6.5 [Data Modeling](#modeling)<br>
	6.6 [Evaluation](#evaluation)<br>
 		&emsp; &nbsp;6.6.1 [Average Sentiment](#avg_sentiment)<br>
   		&emsp; &nbsp;6.6.2 [Comments Count And Proportion by Sentiment](#count_by_sentiment)<br>
     	&emsp; &nbsp;6.6.3 [Average Objectiveness](#avg_subjectivity)<br>
   		&emsp; &nbsp;6.6.4 [Comments Count And Proportion by Objectiveness](#count_by_objectiveness)<br>
        &emsp; &nbsp;6.6.5 [Most Frequent Words for Positive and Negative Comments](#words_positive_negative)<br>
        &emsp; &nbsp;6.6.6 [Most Frequent Words for Objective and Subjective Comments](#words_objective_subjective)<br>
8. [Conclusions](#conclusions)<br>
9. [References](#references)<br>
10. [Description of Files in Repository](#files)<br>

____
<a class="anchor" id="intro"></a>
### **1. Introduction**
Entresto&trade; is a medicine used to treat adults with chronic heart failure who have symptoms of the disease and reduced ejection fraction to help reduce the risk of death and hospitalization. It contains the active substances sacubitril and valsartan. This medicine is available as tablets and granules to be taken by mouth twice a day [(European Medicines Agency, 2023)](#ema).

Collecting the opinions and experiences from the patients with a given medicine represents an important task for the drug manufacturer and regulatory agencies. In this sense, Natural Language Processing (NLP), understood as the programming of computers for processing and
analysing large amounts of natural language data, and the web, as a readily available source of information [(Rogel-Salazar, 2020)](#rogel), could be used as a feasible solution.

Sentiment analysis is the study of people's opinions, sentiments, appraisals, attitudes, and emotions expressed in written text towards an entity using NLP [(Bing, 2015)](#bing). It is commonly used to classify a sentiment or opinion as positive, negative, or neutral; and it is valuable to extract and exploit information from social media as its most important insight "is what people talk about and what their opinions are" [(Bing, 2015)](#bing).

Although several algorithms and approaches exist to perform sentiment analysis, such as supervised techniques using machine learning or custom score functions, it was decided to use a **lexicon-based approach** [(Medhat, Hassan & Korashy, 2014)](#medhat), which consists of lists of positive and negative words that occur frequently in product reviews that serves to calculate the sentiment score in a document [(Bing, 2015)](#bing). The lexicon-based approach was selected because, unlike machine learning models, it does not require labeled training data. 

In this context, the purpose of the present study is to perform a sentiment analysis on a sample of social media data about Entresto&trade;.

___
<a class="anchor" id="objective"></a>
## **2. General Objective**

To extract the opinions from patients on a sample of social media about Entresto&trade;.

___
<a class="anchor" id="question"></a>
## **3. Research Question**

What are the opinions from patients on a sample of social media about Entresto&trade;.

___
<a class="anchor" id="hypothesis"></a>
## **4. Hypothesis**

The opinions from patients on a sample of social media about Entresto&trade; are positive.

___
<a class="anchor" id="methodology"></a>
## **5. Methodology**

The methodology of the present study is based on the CRISP-DM [(Chapman et al., 2000)](#chapman) framework and Rollin’s *Foundational Methodology for Data Science* [(Rollins, 2015)](#rollins):

1. **Analytical approach**: Lexicon-based analysis.
2. **Data requirements**: Text data with comments from patients in English.
3. **Data collection**: Sample taken from <a href="https://www.reddit.com/">Reddit</a>.
4. **Data exploration**: Data was explored with Python 3 and its libraries Numpy, Pandas, Matplotlib and Seaborn.
5. **Data preparation**: Data was cleaned and prepared by performing steps of cleaning, tokenization, stopwords removal, POS tagging, and lemmatization using NLTK.
6. **Exploratory Data Analysis**: Statistical measures were assessed using Python 3 and its libraries Pandas, Matplotlib, and Seaborn.
7. **Data modeling**: Rule-based sentiment analysis using TextBlob.
8. **Evaluation**: No evaluation was performed as lexicon-based analysis is an unsupervised approach [(Bing, 2015)](#bing); however, the outcome from the sentiment analysis was used to answer the research question.

___
<a class="anchor" id="results"></a>
## **6. Results**

### **6.1 Data Collection** <a class="anchor" id="collection"></a>
Data was collected on October 20, 2024, from <a href="https://www.reddit.com/">Reddit</a>, under the thread *"Entresto -- your experience"*. To recover the whole page with users comments, the extension <a href="https://github.com/gildas-lormeau/SingleFile">SingleFile</a> was used on a Mozilla FireFox web browser.

### **6.2 Data Understanding** <a class="anchor" id="exploration"></a>
The sample dataset was explored to identify its basic text statistics and assess its quality. To do so, it was explored the format and quantity of data, the number of comments, the length of comments, the distribution of comments length, the number of words, the number of unique words, the distribution of words count, the most common words, and the number of missing and duplicated values.

### **6.3 Data Preparation** <a class="anchor" id="preparation"></a>
The text was preprocessed to remove non-alphabetical characters (like special characters and numbers), tokenize words, remove stop words, add POS tagging, remove stopwords, and obtaining of the lemma, or dictionary form, of a word.

### **6.4 Exploratory Data Analysis** <a class="anchor" id="eda"></a>
Then, the processed text was analized to explore its general features.

A summary is shown in the table below:

| Feature | Value |
| :----: | :----: |
| Comments count | 19 |
| Avg comments length | 418 |
| Median comments length | 111 |
| Words count | 1178 |
| Unique words count | 649 |

The 20 most frequent words are shown below:

<p align="center">
	<img src="reports/figures/fig_top_20_most_frequent_words.png?raw=true" width=70% height=60%>
</p>

On the other hand, the distribution of words is shown in the plot below:

<p align="center">
	<img src="reports/figures/fig_words_distribution.png?raw=true" width=70% height=60%>
</p>

Thus, according to the plot above, most of the words in the comments appear up to 4 times; where the most mentioned word -Entresto-, appeared 17 times.

### **6.5 Modeling** <a class="anchor" id="modeling"></a>
The sentiment analysis was performed on the prepared comments using the library *TextBlob* in order to get two measures from each comment:

1. **Polarity**: Float number within the range [-1.0, 1.0], which represents the how positive (1.0) or negative (-1.0) a comment is.
2. **Subjectivity**: Float number within the range [0.0, 1.0], where 0.0 is very objective and 1.0 is very subjective.

Processed dataset can be found <a href="https://github.com/DanielEduardoLopez/SentimentAnalysisEntresto/blob/main/data/processed/processed_data.csv">here</a>.

### **6.6 Evaluation** <a class="anchor" id="evaluation"></a>
In this section, the results of the sentiment analysis were evaluated to answer the research question.

#### **6.6.1 Average Sentiment** <a class="anchor" id="avg_sentiment"></a>
The average polarity score for all comments was calculated to estimate the average sentiment:

```bash
0.0937
```
So, the overall sentiment of all the comments is **Positive**.

#### **6.6.2 Comments Count And Proportion by Sentiment** <a class="anchor" id="count_by_sentiment"></a>

The number of positive, neutral, and negative comments was assessed as follows:

<p align="center">
	<img src="reports/figures/fig_total_comments_by_sentiment.png?raw=true" width=70% height=60%>
</p>

<p align="center">
	<img src="reports/figures/fig_comments_percentage_by_sentiment.png?raw=true" width=70% height=60%>
</p>

So, most of the comments were positive (68%), with only a few portion of them being negative (21%.)


#### **6.6.3 Average Objectiveness** <a class="anchor" id="avg_subjectivity"></a>

The overall average objectiveness is as follows:

```bash
0.402
```

So, the overall objectiveness of all the comments was **Objective**.


#### **6.6.4 Comments Count And Proportion by Objectiveness** <a class="anchor" id="count_by_objectiveness"></a>

The number of objective and subjective comments was assessed as follows:

<p align="center">
	<img src="reports/figures/fig_total_comments_by_objectiveness.png?raw=true" width=70% height=60%>
</p>

<p align="center">
	<img src="reports/figures/fig_comments_percentage_by_objectiveness.png?raw=true" width=70% height=60%>
</p>

So, most of the comments were deemed objective (68%); whereas only a few portion of them were classified as subjective (32%.)

#### **6.6.5 Most Frequent Words for Positive and Negative Comments** <a class="anchor" id="words_positive_negative"></a>

In this section, word clouds were created to assess which words were the most frequent for both positive and negative comments.

The word cloud from positive comments is shown below:

<p align="center">
	<img src="reports/figures/fig_word_cloud_from_positive_comments.png?raw=true" width=70% height=40%>
</p>

Word cloud from positive comments suggested that: (1) Dosification schema is appreciated by patients, (2) Copay program is useful for patients to reduce the economic burden of getting the medicine, and (3) The drug is effective to reduce heart risk.

On the other hand, the word cloud from negative comments is shown below:

<p align="center">
	<img src="reports/figures/fig_word_cloud_from_negative_comments.png?raw=true" width=70% height=40%>
</p>

On the other hand, the word cloud from negative comments suggested that the cost of the drug could be too high.

#### **6.6.6 Most Frequent Words for Objective and Subjective Comments** <a class="anchor" id="words_objective_subjective"></a>

Likwise, word clouds were created to assess which words were the most frequent for both objective and subjective comments.

The word cloud from objective comments is shown below:

<p align="center">
	<img src="reports/figures/fig_word_cloud_from_objective_comments.png?raw=true" width=70% height=40%>
</p>

Word cloud from objective comments suggested that: (1) Copay program is useful for patients to reduce the economic burden of getting the medicine, and (2) The drug is effective to reduce heart failure.

On the other hand, the word cloud from subjective comments is shown below:

<p align="center">
	<img src="reports/figures/fig_word_cloud_from_subjective_comments.png?raw=true" width=70% height=40%>
</p>

On the other hand, the word cloud from subjective comments refered to personal experiences from the patients when using the medicine, with no clear insight.

____
<a class="anchor" id="conclusions"></a>
### **8. Conclusions**

From the sample of social media about Entresto&trade;, 58% of the patient opinions ($n=19$) were **positive**, against 21% of negative opinions. On the other hand, from those opinions, 68% were deemed as **objective**.

Analysis from the positive and the objective comments suggested that the **dosification schema** and the **copay** program for Entresto&trade; were appreciated by patients; as well as its **effectiveness** to reduce heart failure. Whereas, negative comments pointed out to the **high cost** of the drug.

Thus, overall, the results from the present study indicated that the experiences of the patients with the medicine were **satisfactory**.

____
<a class="anchor" id="references"></a>
### **9. References**

* <a class="anchor" id="bing"></a>**Bing, L. (2015).** *Sentiment analysis: mining opinions, sentiments, and emotions*. Cambridge University Press.
* <a class="anchor" id="chapman"></a>**Chapman, P., Clinton, J., Kerber, R., Khabaza, T., Reinartz, T., Shearer, C., & Wirth, R. (2000)**. *CRISP-DM 1.0: Step-by-step data mining guide*. CRISP-DM consortium. https://api.semanticscholar.org/CorpusID:59777418
* <a class="anchor" id="ema"></a>**European Medicines Agency (2023).** *Entresto (sacubitril / valsartan)*. https://www.ema.europa.eu/en/documents/overview/entresto-epar-summary-public_en.pdf
* <a class="anchor" id="medhat"></a>**Medhat, W., Hassan, A. & Korashy, H. (2014).** Sentiment analysis algorithms and applications:
A survey. *Ain Shams Engineering Journal*. 5: 1093-1113. http://dx.doi.org/10.1016/j.asej.2014.04.011 
* <a class="anchor" id="rogel"></a>**Rogel-Salazar, J. (2020).** *Advanced Data Science and Analytics with Python*. CRC Press.
* <a class="anchor" id="rollins"></a> **Rollins, J. B. (2015)**. *Foundational Methodology for Data Science*. Somers: IBM Corporation. https://tdwi.org/~/media/64511A895D86457E964174EDC5C4C7B1.PDF
* <a class="anchor" id="turki"></a> **Turki Khemakhem, I., Jamoussi, S., & Ben Hamadou, A. (2016).** POS Tagging without a Tagger: Using Aligned Corpora for Transferring Knowledge to Under-Resourced Languages. *Computación y Sistemas*, 20(4), 667-679. https://doi.org/10.13053/cys-20-4-2430

____
<a class="anchor" id="files"></a>
### **10. Description of Files in Repository**

Path | File name | Description
:----: | :----: | :----:
./data/raw/ | raw_data.html |  Raw dataset extracted from Reddit
./data/processed/ | processed_data.csv | Processed dataset
./notebooks/ | SentimentAnalysisEntresto.ipynb | Jupyter notebook with the project's code
./references/ | Header.png | Header of the README file
./reports/ | SentimentAnalysisEntresto.html | Report in HTML version
./src/ | charts.py | Python library for plotting charts
./src/ | preprocessing.py | Python library for processing text data
./src/ | scraping.py | Python library for performing web scraping
./src/ | sentiment_analysis.py | Python library for performing sentiment analysis