<p align="center">
	<img src="references/Header.png?raw=true" width=80% height=80%>
</p>

# Sentiment Analysis for Entresto&trade;
#### Daniel Eduardo López

<font size="-1"><a href="https://www.linkedin.com/in/daniel-eduardo-lopez">LinkedIn</a> | <a href="https://github.com/DanielEduardoLopez">GitHub </a></font>

**2 Apr 2025**

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


### **6.2 Data Exploration** <a class="anchor" id="exploration"></a>


### **6.3 Data Preparation** <a class="anchor" id="preparation"></a>


### **6.4 Exploratory Data Analysis** <a class="anchor" id="eda"></a>


### **6.5 Modeling** <a class="anchor" id="modeling"></a>


### **6.6 Evaluation** <a class="anchor" id="evaluation"></a>


#### **6.6.1 Average Sentiment** <a class="anchor" id="avg_sentiment"></a>


#### **6.6.2 Comments Count And Proportion by Sentiment** <a class="anchor" id="count_by_sentiment"></a>


#### **6.6.3 Average Objectiveness** <a class="anchor" id="avg_subjectivity"></a>


#### **6.6.4 Comments Count And Proportion by Objectiveness** <a class="anchor" id="count_by_objectiveness"></a>


#### **6.6.5 Most Frequent Words for Positive and Negative Comments** <a class="anchor" id="words_positive_negative"></a>


#### **6.6.6 Most Frequent Words for Objective and Subjective Comments** <a class="anchor" id="words_objective_subjective"></a>


____
<a class="anchor" id="conclusions"></a>
### **8. Conclusions**


____
<a class="anchor" id="references"></a>
### **9. References**


____
<a class="anchor" id="files"></a>
### **10. Description of Files in Repository**