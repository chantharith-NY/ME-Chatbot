import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

# Ensure required resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Preprocessing function
def preprocess(text):
    text = text.lower()  # Convert to lowercase
    words = word_tokenize(text)  # Tokenize words
    words = [w for w in words if w not in stopwords.words('english') and w not in string.punctuation]
    return " ".join(words)  # Return processed text as a string
