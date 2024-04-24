import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

# Download NLTK stopwords if not already downloaded
nltk.download('stopwords')
nltk.download('punkt')

# Read the contents of the file
with open("C:\Users\gozef\Downloads\PROJECT-master\PROJECT-master\\random_paragraphs.txt", "r") as file:
    text = file.read()

# Tokenize the text
words = word_tokenize(text)

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.lower() not in stop_words]

# Count word frequencies
word_freq = Counter(filtered_words)

# Display word frequency count
for word, freq in word_freq.items():
    print(f"{word}: {freq}")
