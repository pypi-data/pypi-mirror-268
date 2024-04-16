import re
import nltk
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt')
from gensim import corpora
stop_words = set(stopwords.words('english'))
en_stop = get_stop_words('en')
def tokenize(x,sep=r"\w+"):
	tokenizer = RegexpTokenizer(sep)
	return tokenizer.tokenize(x.lower())

def stopwords(x):

	return [y for y in x if y not in en_stop]

def stem(x):
	p_stemmer = PorterStemmer()
	return [p_stemmer.stem(y) for y in x]

def dictionary(collectiion):
	Vocabulary = []
	for x in collectiion:
		Vocabulary.extend(x)
	Vocabulary = list(set(Vocabulary))
	dictionary = corpora.Dictionary(collectiion)
	dictlist = list(dictionary.token2id.items())
	ID_Word = {}
	for it in dictlist:
		ID_Word[it[1]] = it[0]
	return Vocabulary,dictionary,ID_Word

def words_frequency (collectiion,dictionary):
	return  [dictionary.doc2bow(d) for d in collectiion]

def preprocess_text(text):
    # Tokenize
    tokens = word_tokenize(text.lower())

    # Remove stopwords
    stop_words =en_stop# set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]

    # Stemming
    #stemmer = PorterStemmer()
    #tokens = [stemmer.stem(token) for token in tokens]

    # Remove special characters, digits, and HTML tags
    tokens = [token for token in tokens if token.isalpha()]

    return " ".join(tokens)
def preprocess_token(text):
    # Tokenize
    tokens = word_tokenize(text.lower())

    # Remove stopwords
    stop_words =en_stop# set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]

    # Stemming
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(token) for token in tokens]

    # Remove special characters, digits, and HTML tags
    tokens = [token for token in tokens if token.isalpha()]

    return tokens

def getHashtag(tweet):
	# return list of hashtags
	hashtag_rx = re.compile(r'#\w+')
	hashtags = hashtag_rx.findall(tweet)
	return hashtags

def getAllHashtags(all_tweets):
	all_hashtags = []
	for tweet in all_tweets:
		hashtags_list = getHashtag(tweet)
		all_hashtags.extend(hashtags_list)
	return all_hashtags


def cleanTweetText(tweet):
	retweet_rx = re.compile(r'RT @\w+:\s')
	url_rx = re.compile(r'https://\w\.\w+/\w+')
	hashtag_rx = re.compile(r'#\w+\s')
	to_user_rx = re.compile(r'@\w+\s')
	regex      = [retweet_rx, url_rx, hashtag_rx, to_user_rx]
	for rx in regex:
		tweet = re.sub(rx, '', tweet)
		tweet=re.sub(r'[^\w\s#@/:%.,_-]', '', tweet)
	return  re.sub(r'\n\n', ' ', tweet)