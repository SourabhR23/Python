from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from contractions import CONTRACTION_MAP
from nltk.corpus import stopwords
from string import punctuation
import unicodedata
import nltk
import re

nltk.download('wordnet')
nltk.download('words')
nltk.download('stopwords')

class NLTK_preprocessing():

    def __init__(self, text):
        self.__text = text
        self.__result = None
        
    def tokenization(self, parameter_dictionary):
        token_type = parameter_dictionary.get("token_type", "word")
        if token_type == "word":
            res = word_tokenize(self.__text)
        else:
            res = sent_tokenize(self.__text)
        self.__result = res
        return self.__result
    
    def stemming(self, parameter_dictionary):
        ps = PorterStemmer()
        words = word_tokenize(self.__text)
        stem_res = []
        for word in words:
            stem_res.append(ps.stem(word))
        return stem_res
    
    def lemmatization(self, parameter_dictionary):
        word_lemma = WordNetLemmatizer()
        words = word_tokenize(self.__text)
        lemma_res = []
        for word in words:
            lemma_res.append(word_lemma.lemmatize(word))
        return lemma_res

    def POS(self, parameter_dictionary):
        words = word_tokenize(self.__text)
        POS_token_list = (nltk.pos_tag(words))
        return POS_token_list
    
    def NER_tag(self, parameter_dictionary):
        words = nltk.word_tokenize(self.__text)
        for i in str(words):
            tag = nltk.pos_tag(words)
            nameEnt = (nltk.ne_chunk(tag, binary=True))
            return nameEnt
        
    def remove_stopwords(self, parameter_dictionary):
        stop_words = set(stopwords.words('english'))
        words = nltk.word_tokenize(self.__text)
        filtered_sent = []
        for w in words:
            if w.lower() not in stop_words:
                filtered_sent.append(w)
        filtered_text = ' '.join(filtered_sent)
        return filtered_text
    
    def remove_numbers(self, parameter_dictionary):
        numbers = re.compile(r'[0-9]')
        result = []
        for nums in self.__text:
            nums_removed = numbers.sub("", nums)
            if len(nums_removed) > 0:
                result.append(nums_removed)
        return ''.join(result)
    
    def remove_html_tags(self, parameter_dictionary):
        text = self.__text
        html_tags = re.compile('<.*?>')
        return re.sub(html_tags, '', text)
    
    def remove_emails(self, parameter_dictionary):
        sentence = self.__text
        emails = re.compile("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)")
        return re.sub(emails, '', sentence)
    
    def remove_punctuations(self, parameter_dictionary):
        text = self.__text
        res = []
        for i in text:
            if i not in punctuation:
                res.append(i)
        return ''.join(res)
    
    def remove_unicode(self, parameter_dictionary):
        text = self.__text
        newstring = unicodedata.normalize('NFKD',self.__text).encode('ascii', 'ignore').decode("utf-8", 'ignore')
        return newstring
        
    def remove_specialcharacters(self, parameter_dictionary):
        text = self.__text
        result = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", self.__text).split())
        return result
    
    def expand_contractions(self, parameter_dictionary, contraction_mapping=CONTRACTION_MAP):
        text = self.__text
        contractions_pattern = re.compile('({})'.format('|'.join(contraction_mapping.keys())), 
                                          flags=re.IGNORECASE|re.DOTALL)
        def expand_match(contraction):
            match = contraction.group(0)
            first_char = match[0]
            expanded_contraction = contraction_mapping.get(match)\
                                    if contraction_mapping.get(match)\
                                    else contraction_mapping.get(match.lower())                       
            expanded_contraction = first_char + expanded_contraction[1:]
            return expanded_contraction

        expanded_text = contractions_pattern.sub(expand_match, text)
        expanded_text = re.sub("'", "", expanded_text)
        return expanded_text
    
if __name__ == "__main__":
    nk = NLTK_preprocessing("<html><a href = 'www.google.com'>This is HTML code</a></html>"
                           "\n@##$ Special characters, 42 numbers test, mobile numb 1230456891, email google@gmail.com"
                           "\nY'all can't expand contractions I'd think."
                           "\nThe, and, if are stopwords, computer is not. \n'Sómě Áccěntěd těxt'")

    print("\n", nk.tokenization({"token type": "word"}))
    print("\n", nk.stemming({}))
    print("\n", nk.lemmatization({}))
    print("\n", nk.POS({}))
    print("\n", nk.NER_tag({}))
    print("\n", nk.remove_stopwords({}))
    print("\n", nk.remove_numbers({}))
    print("\n", nk.remove_html_tags({}))
    print("\n", nk.remove_emails({}))
    print("\n", nk.remove_punctuations({}))
    print("\n", nk.remove_unicode({}))
    print("\n", nk.remove_specialcharacters({}))
    print("\n", nk.expand_contractions({}))
