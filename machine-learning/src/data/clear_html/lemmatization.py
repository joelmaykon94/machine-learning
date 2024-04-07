from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import SnowballStemmer
nltk.download('stopwords')
nltk.download('wordnet')

# Remove all stopwords
stop_words = stopwords.words('english')
def remove_stopwords(tokenized_sentences):
    for sentence in tokenized_sentences:
        yield([token for token in sentence if token not in stop_words])

# Lemmatize all words
wordnet_lemmatizer = WordNetLemmatizer()
def lemmatize_words(tokenized_sentences):
    for sentence in tokenized_sentences:
        yield([wordnet_lemmatizer.lemmatize(token) for token in sentence])

snowball_stemmer = SnowballStemmer('english')
def stem_words(tokenized_sentences):
    for sentence in tokenized_sentences:
        yield([snowball_stemmer.stem(token) for token in sentence])

sentences = list(remove_stopwords(sentences))
sentences = list(lemmatize_words(sentences))
sentences = list(stem_words(sentences))