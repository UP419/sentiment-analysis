import string
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = open('text.txt', encoding='utf-8').read()

# change text to lowercase and remove all punctuation
text = text.lower().translate(str.maketrans('', '', string.punctuation))

# tokenization
tokenized_words = word_tokenize(text, 'english')

final_words = []
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)


emotions_list = dict()
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.translate(str.maketrans("", "", "\n',")).strip()
        word, emotion = clear_line.split(':')
        emotions_list[word] = emotion


emotions_count = dict()
for word in final_words:
    if word in emotions_list:
        emotion = emotions_list[word]
        emotions_count[emotion] = emotions_count.get(emotion, 0) + 1

plt.bar(emotions_count.keys(), emotions_count.values())
plt.savefig('graph.png')
plt.show()