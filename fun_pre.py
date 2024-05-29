import re
import string
from nltk.corpus import stopwords

# List of additional Arabic stop words
additional_stopwords = [
    'هذا', 'ذلك', 'لكن', 'لقد', 'على', 'حتى', 'ولا', 'اذا', 'ما', 'في', 'لم', 'لن', 'بعد', 'بين', 
    'من', 'هو', 'هي', 'ان', 'انها', 'انه', 'هذه', 'الى', 'إلى', 'عن', 'عند', 'أو', 'ثم', 'كان', 'قد'
]

def remove_diacritics(text):
    arabic_diacritics = re.compile("""
                                ّ    | # Tashdid
                                َ    | # Fatha
                                ً    | # Tanwin Fath
                                ُ    | # Damma
                                ٌ    | # Tanwin Damm
                                ِ    | # Kasra
                                ٍ    | # Tanwin Kasr
                                ْ    | # Sukun
                                ـ     # Tatwil/Kashida
                            """, re.VERBOSE)
    


    
    text = re.sub(arabic_diacritics, '', text)
    return text

def normalize_arabic(text):
    text = re.sub("[إأآا]", "ا", text)
    text = re.sub("ى", "ي", text)
    text = re.sub("ؤ", "و", text)
    text = re.sub("ئ", "ي", text)
    text = re.sub("ة", "ه", text)
    return text

def preprocess_text_arabic(text):
    # Remove user mentions
    text = re.sub(r'@\w+', '', text)
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    # Remove special characters and emojis
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Remove Arabic diacritics
    text = remove_diacritics(text)
    # Normalize Arabic text
    text = normalize_arabic(text)
    # Remove numbers
    text = re.sub(r'\d+', '', text)
    # Remove non-Arabic characters
    text = re.sub(r'[^\u0600-\u06FF\s]', '', text)
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    # Convert to lowercase (optional for Arabic)
    # Combine NLTK and additional stopwords
    arabic_stopwords = set(stopwords.words('arabic')).union(additional_stopwords)
    # Remove stop words
    text = ' '.join([word for word in text.split() if word not in arabic_stopwords])
    
    
    return text
