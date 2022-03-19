# PreprocessingNLP
A comprehensive library for text preprocessing, exploratory text data analysis and information extraction. 

All functions take in strings as inputs.

## INSTALLATION
```
xx
```
## DEPENDENCIES
```
pip install nltk
python -m nltk download stopwords, wordnet, punkt, averaged_perceptron_tagger
pip install beautifulsoup
pip install textblob

```
## DATA CLEANUP
Available functions: 

remove_stopwords() • remove_tags() • remove_links() • remove_punctuation() • remove_emails() • remove_whitespaces() • remove_html()

**Example:**
```
text = "Today I met with @elonmusk to discuss plans to colonize Mars."

text = remove_tags(text)
text = remove_stopwords(text)

print(text)
---
"Today I met discuss plans colonize Mars."

```
## DATA PREPROCESSING
Available functions:

correct_spelling() • stem() • lemmatize()

**Example:**
```
text = "We are planning to erect multiple buildings within the Utopia Planitia, where our new civilization will thrive."

lemmatize(text)
---
"We be planning to erect multiple building within the Utopia Planitia, where our new civilization will thrive."

```

## DATA ANALYSIS
Available functions:

count_words() • count_words_unique() • count_stopwords() • count_stopwords_unique() • count_hashtags() • count_hashtags_unique() • count_tags() • count_characters_with_spaces() • count_characters_without_spaces() • avg_word_len() • avg_sent_len()

**Example:**
```
text = "Our plans are now well underway and we are proud to present the first draft of our manifesto."

avg_word_len(text)
---
4.222222222222222
```

## DATA EXTRACTION
Available functions:

get_emails() • get_tags() • get_hashtags() • get_URLs()

**Example:**
```
text = "Me and @Elon Musk at the @this_is_the_future. #tech #AI #innovation"

get_hashtags(text)
---
['#tech', '#AI', '#innovation']

```
