import string
import matplotlib.pyplot as plt

text = open('text.txt', encoding='utf-8').read()

# change text to lowercase and remove all punctuation
text = text.lower().translate(str.maketrans('', '', string.punctuation))

# tokenization
tokenized_words = text.split()

# stop words are the words that don't add any meaning to text, don't carry any emotion
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

final_words = []
for word in tokenized_words:
    if word not in stop_words:
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