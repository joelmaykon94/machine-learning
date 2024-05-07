import gensim
import string

# Uses gensim to process the sentences
def sentence_to_words(sentences):
    for sentence in sentences:
        sentence_tokenized = gensim.utils.simple_preprocess(sentence,
                                                            deacc=True,
                                                            min_len=2,
                                                            max_len=15)
        
        # Make sure we don't yield empty arrays
        if len(sentence_tokenized) > 0:
            yield sentence_tokenized

# Process the sentences manually
def sentence_to_words_from_scratch(sentences):
    for sentence in sentences:
        sentence_tokenized = [token.lower() for token in 
               word_tokenize(sentence.translate(str.maketrans('','',string.punctuation)))]
        
        # Make sure we don't yield empty arrays
        if len(sentence_tokenized) > 0:
            yield sentence_tokenized

sentences = list(sentence_to_words(sentences))