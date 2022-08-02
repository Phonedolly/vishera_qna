import time

from wordcloud import WordCloud
from konlpy.tag import Hannanum
from collections import Counter
import matplotlib.pyplot as plt


def analyze(data: list) -> None:
    hannanum = Hannanum()
    line = []

    line = hannanum.pos(''.join(data))

    n_adj = []

    for word, tag in line:
        if tag in ['N']:
            n_adj.append(word)

    # stop_words = "를 의 "
    # stop_words = set(stop_words.split(' '))
    #
    # n_adj = [word for word in n_adj if not (word in stop_words)]

    counts = Counter(n_adj)
    tags = counts.most_common(50)
    print(tags)

    # mask = Image.new('RGBA', (3840, 2160), (255, 255, 255))
    # image = Image.open('out.png').convert('RGBA')
    # x, y = image.size
    # mask.paste((image, (0, 0, x, y), image), image)
    # mask = np.array(mask)

    wc = WordCloud(font_path='C:\\Windows\Fonts\malgunbd.ttf', width=3840, height=2160, scale=2.0,
                   background_color='white',
                   colormap='prism',
                   max_font_size=250)
    cloud = wc.generate_from_frequencies(dict(tags))

    plt.figure(figsize=(38.4, 21.6))
    plt.imshow(cloud)
    plt.axis('off')

    cloud.to_file('out_' + time.time() + '.png')
    plt.show()
