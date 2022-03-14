# --- TO DO LIST --- #

# REMOVE: multiple letters
# APPLY: normalization
# VISUALIZE:
# ideas for exploratory data analysis??
# PIPELINE !!!!

# -------- IMPORTS -------- #

import nltk
import re
import matplotlib.pyplot as plt

from bs4 import BeautifulSoup
from textblob import TextBlob

# -------- CLEAN -------- #

# everything is substituted with a whitespace, rather than fully deleted to prevent accidental mergers
# this is later dealt with by removing the resulting multiple whitespaces

# --- STOP WORDS --- #
from nltk.corpus import stopwords

nltk.download("stopwords")
all_stopwords = stopwords.words("english")

# negation is important, don't even know why it's considered a stopword
all_stopwords.remove("not")

def remove_stopwords(text):
  # tokenize the text
  text = text.split()
  # checked and removed
  text = [word for word in text if not word in all_stopwords]
  # joined back to a single string
  text = " ".join(text)
  return text

def remove_html(text):
  return BeautifulSoup(text, "lxml").get_text()

def remove_tags(text):
  # @ + name, but preserves emails
  return re.sub(r"^@[A-Za-z0-9]{1,}|\s@[A-Za-z0-9]{1,}", " ", text)

def remove_hashtags(text):
  # deletes the whole hashtag, if the content is to be preserved, using only remove_punctuation does the trick
  return re.sub(r"#[A-Za-z0-9]+", " ", text)

def remove_links(text):
  # http or https
  return re.sub(r"https?://[A-Za-z0-9./-]+", " ", text)

def remove_punctuation(text):   
  # except '
  return re.sub(r"[^A-Za-z']", " ", text)

def remove_emails(text):
  # name_surname00@domain.co.uk
  return re.sub(r"[a-z0-9+_.-]+@[a-z0-9+_.-]+.[a-z0-9+_-]+.[a-z]+", " ", text)

# TO-DO - handle exceptions for legit words with double letters
def remove_doubles(text):
  # recurring 1+ times, substituted by it ocurring once
  return re.sub(r"([A-Za-z])\1+", r"\1", text)

def remove_whitespaces(text):
  return re.sub(r" +", " ", text)

# -------- PROCESS -------- #

def correct_spelling(text):
  return TextBlob(text).correct()

# TO-DO - normalization

# --- STEM --- #
from nltk.stem import PorterStemmer
porter = PorterStemmer()

def stem(text):
  text = text.split()
  return " ".join([porter.stem(word) for word in text])

# --- LEMMATIZE --- #
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

# avoids errors ??
nltk.download("wordnet")
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")

lemmatizer = WordNetLemmatizer()

def get_wordnet_pos(word):
  # Map POS tag to first character accepted by lemmatize()
  tag = nltk.pos_tag([word])[0][1][0].upper()
  tag_dict = {"J": wordnet.ADJ,
              "N": wordnet.NOUN,
              "V": wordnet.VERB,
              "R": wordnet.ADV}

  return tag_dict.get(tag, wordnet.NOUN)

def lemmatize(text):
  text = text.split()
  return " ".join([lemmatizer.lemmatize(word, get_wordnet_pos(word)) for word in text])

# -------- ANALYZE -------- #

def count_words(text):
  # tokenizes the text
  words = text.split()
  return len(words)

def count_words_unique(text):
  # tokenizes the text
  words = text.split()
  # set removes the duplicates
  return len(set(words))

def count_stopwords(text):
  # tokenizes the text
  text = text.split()
  # collects all stopwords
  stopwords = [word for word in text if word in all_stopwords]
  return len(stopwords)

def count_stopwords_unique(text):
  # tokenizes the text
  text = text.split()
  # collects all stopwords
  stopwords = [word for word in text if word in all_stopwords]
  # set removes the duplicates
  return len(set(stopwords))

def count_hashtags(text):
  # will also count expressions such as "he is my #1", but trying to exclude that would also exclude hashtags like #2022
  hashtags = re.findall(r"#[A-Za-z0-9]+", text)
  return len(hashtags)

def count_hashtags_unique(text):
  # will also count expressions such as "he is my #1", but trying to exclude that would also exclude hashtags like #2022
  hashtags = re.findall(r"#[A-Za-z0-9]+", text)
  # set removes the duplicates
  return len(set(hashtags))

def count_tags(text):
  # @ + name
  tags = re.findall(r"^@[A-Za-z0-9]{1,}|\s@[A-Za-z0-9]{1,}", text)
  return len(tags)

def count_characters_without_spaces(text):
  # removes the spaces
  text = text.replace(" ", "")
  return len(text)

def count_characters_with_spaces(text):
  return len(text)

def avg_word_len(text):
  # separates the words
  words = text.split()
  # gets the number of characters
  lengths = [len(word) for word in words]
  # avg
  return sum(lengths) / len(lengths)

def avg_sent_len(text):
  # separates the sentences
  sents = nltk.sent_tokenize(text)
  # gets the number of words
  lengths = [len(sent.split()) for sent in sents]
  # avg
  return sum(lengths) / len(lengths)

# -------- VISUALIZE -------- #

# TO-DO - everything

# -------- EXTRACT -------- #

def get_emails(text):
  # name_surname00@domain.co.uk
  emails = re.findall(r"[a-z0-9+_.-]+@[a-z0-9+_.-]+.[a-z0-9+_-]+.[a-z]\s", text)
  # the regex returns a space after the address for some reason which needs to be removed
  emails = [email.replace(" ", "") for email in emails]
  return emails

def get_tags(text):
  # # @ + name, but avoids fetching emails
  tags = re.findall(r"^@[A-Za-z0-9]{1,}|\s@[A-Za-z0-9]{1,}", text)
  # the regex returns a space before the tag for some reason which needs to be removed
  tags = [tag.replace(" ", "") for tag in tags]
  return tags

def get_hashtags(text):
  # will also fetch expressions such as "he is my #1", but trying to exclude that would also exclude hashtags like #2022
  hashtags = re.findall(r"#[A-Za-z0-9]+", text)
  return hashtags

def get_URLs(text):
  # http or https
  URLs = re.findall(r"https?://[A-Za-z0-9./]+", text)
  return URLs