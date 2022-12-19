import matplotlib.pyplot as plt

from pathlib import Path
from wordcloud import WordCloud, STOPWORDS

wdir = Path(r'C:\Users\212628255\PycharmProjects\data_science')
out = Path(r"C:\Users\212628255\Desktop")
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

# fig, ax = plt.subplots()
# ax.imshow(word_wc, interpolation='bilinear')
#
# plt.axis('off')
# plt.figure(dpi=300)
#
# plt.show()
# fig.savefig(out / 'linkedin111.jpg')



plt.imshow(word_wc, interpolation='bilinear')

plt.axis('off')

plt.savefig((out / 'linkedin111.jpg'), dpi=300)
plt.show()
