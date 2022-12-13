import matplotlib.pyplot as plt

from pathlib import Path
from wordcloud import WordCloud, STOPWORDS

wdir = Path(r'C:\Users\212628255\PycharmProjects\data_science')
file = wdir / 'words1.txt'

with open(file, 'r') as reader:
    s = reader.read()

word_wc = WordCloud(
    background_color='white',
    max_words=100,
    width=1200,
    height=300
)

word_wc.generate(s)

plt.imshow(word_wc, interpolation='bilinear')
plt.axis('off')
plt.show()
plt.savefig('linkedin.jpg')