# SAT word analysis

This project extracts data from SAT practice tests and then performs frequency analysis. 

### Stages:
1. Reading raw HTML data
2. Data cleaning (in particular removing HTML tags)
3. Sentence tokenization and word lemmatization
4. Heuristical filtering of low-value words
5. Counting word frequencies
6. Visualizing frequencis with a word cloud

The result may be seen, for example, [here](results/result1e-05.png).

### Requirements:
The project uses pandas, nltk, beautifulsoup4, wordcloud, matplotlib, spacy.
