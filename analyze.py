import os
import time
from threading import Thread

import jpype
from wordcloud import WordCloud
from konlpy.tag import Hannanum
from collections import Counter
import matplotlib.pyplot as plt

hannanum = Hannanum()


def do_concurrent_tagging(start, end, lines, result):
    jpype.attachThreadToJVM()
    l = [hannanum.pos(lines[i]) for i in range(start, end)]
    result.append(l)
    return


def analyze(data: list) -> None:
    # line = []
    # line = hannanum.pos(''.join(data))
    nlines = len(data)
    n_adj = []
    print(nlines)

    print('cpu_count: ' + str(os.cpu_count()))
    print('concurrent tagging:')
    t = time.perf_counter()
    result = []
    threads = []
    cpu_count = os.cpu_count()
    for i in range(cpu_count):
        threads += [Thread(target=do_concurrent_tagging,
                           args=(int(nlines / cpu_count) * i, int(nlines / cpu_count) * (i + 1), data, result))]
        threads[i].start()
        threads[i].join()
    # for i in range(cpu_count):
    #     threads[i].join()
    m = sum(sum(result, []), [])
    print(time.perf_counter() - t)
    for word, tag in m:
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

    wc = WordCloud(font_path='C:\\Windows\Fonts\KoPubWorld Dotum Bold.ttf', width=3840, height=2160, scale=2.0,
                   background_color='white',
                   colormap='Set2',
                   max_font_size=700)
    cloud = wc.generate_from_frequencies(dict(tags))

    plt.figure(figsize=(38.4, 21.6))
    plt.imshow(cloud)
    plt.axis('off')

    cloud.to_file('out_' + str(time.time()) + '.png')
    plt.show()
