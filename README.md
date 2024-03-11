Capstone Project - NLP Sentiment Analysis

## Table of Contents 
- [Overview](#Overview)
- [Files](#files)
- [Methodology](#methodology)
- [Results](#results)
- [Conclusion](#conclusion)
- [Installation](#installation)
- [Usage](#Usage)
- [Credits](#credits)

## Overview

This respository contains code, documentation, and dataset for a capstone project focused on sentiment analysis using Natural Language Processing (NLP).The project aims to analyse customer sentiment towards various products by extracting insights from textual data. By leveraging NLP methods, businesses can understand customer feedback and enhance their products or services accordingly. 

## Files

Code: The main code for this project is 'sentimentc_analysis.py'. This python script includes functions for data preprocessing, sentiment analysis, and sample review testing. The code written is written in Python. Additionally, ensuring it has the required libraries installed. 
Dataset: The project utilises a dataset compromising product reviews obatined from Kaggle. The dataset is stored in a CSV file format ('amazon_product_reviews.csv') and features multiples columns encapsulating diverse attributes of the reviews, such as product ID, reviewer ID, review text, and rating. 
PDF documentation: The product also includes a pdf document ('Practical Task 21 - Capstone Project.pdf') providing detailed insights into the project's methodology, results, limitations, and future work. This documentations serves as supplementary documentation to understand the project's objectives and outcomes comphrehensively. 

## Methodology

Prior to sentiment analysis, the dataset undergoes preprocessing to prepare the textual data for analysis. This involves tokenisation and the elimination of stop words and non alphabetic tokens from the review text. The spaCy library is used for text processing, and the TextBlob library is employed for sentiment analysis. 

## Results

The effectiveness of the sentiment analysis model is evaluated using sample product reviews. However, discrepancies in sentiment classification are identified indicating potential misclassifications and highlighting the need for further refinement of the model. 

## Conclusion

In conclusion, this capstone project underscores the significance of sentiment analysis in decipering customer sentiments towards products. Despite challenges such as data inconsistencies and misclassifications, continous refinement of sentiment analysis models is imperative to harness the full potential of NLP in understanding customer sentiment. 

## Installation

To install and run this project locally, follow these steps: 
1. Clone this repository to your local machine:
   ''' bash
   git clone https://github.com/anzeelakabir/respository name

## Usage 

1. Navtigate to the project directory.
   Open your command prompt or terminal. Use the 'cd' command to navigate to the directory where you cloned the respository:
   cd path/to/your/respository
Replace 'path/to/your/respository' with the actual path to your project directory.
2. Install Dependencies.
   pip install -r requirements.txt
4. Execute the main script by running the main script provided.
   python sentiment_analysis.py
   
## Credits

This project was created by Anzeela Kabir.



