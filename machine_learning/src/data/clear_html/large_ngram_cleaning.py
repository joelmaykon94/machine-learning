import nltk
nltk.download('punkt')
import matplotlib.pyplot as plt
from nltk.util import ngrams
from nltk.tokenize import word_tokenize

# Helper method for generating n-grams
def extract_ngrams_sentences(sentences, num):
    all_grams = []
    for sentence in sentences:
        n_grams = ngrams(sentence, num)
        all_grams += [ ' '.join(grams) for grams in n_grams]
    return all_grams

# Splits text up by newline and period
def split_by_newline_and_period(pages):
    sentences = []
    for page in pages:
        sentences += re.split('\n|\. ', page)
    return sentences

# Break the dataset up into sentences, split by newline characters and periods
sentences = split_by_newline_and_period(parsed_texts)

# Add unwanted strings into this array
filter_strs = []

# Filter out unwanted strings
sentences = [x for x in sentences
             if not any([re.search(filter_str, x, re.IGNORECASE)
                         for filter_str in filter_strs])]

# Tokenize the sentences
tokenized_sentences = [word_tokenize(sentence) for sentence in sentences]

# Adjust NGRAM_SIZE to capture unwanted phrases
NGRAM_SIZE = 15
ngrams_all = extract_ngrams_sentences(tokenized_sentences, NGRAM_SIZE)

# Sort the n-grams by most common
n_gram_all = nltk.FreqDist(ngrams_all).most_common()

# Print out the top 10 most commmon n-grams
print(f'{NGRAM_SIZE}-Gram Frequencies')
for gram, count in n_gram_all[:10]:
    print(f'{count}\t\"{gram}\"')

# Plot the distribution of n-grams
plt.plot([count for _, count in n_gram_all])
plt.xlabel('n-gram')
plt.ylabel('frequency')
plt.title(f'{NGRAM_SIZE}-Gram Frequencies')
plt.show()