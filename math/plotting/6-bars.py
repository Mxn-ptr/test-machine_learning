#!/usr/bin/env python3
""" Bars """
import numpy as np
import matplotlib.pyplot as plt


def bars():
    """ Creates a stacked bar graph """
    np.random.seed(5)
    fruit = np.random.randint(0, 20, (4, 3))
    plt.figure(figsize=(6.4, 4.8))

    x = ['Farrah', 'Fred', 'Felicia']
    y1 = fruit[0]
    y2 = fruit[1]
    y3 = fruit[2]
    y4 = fruit[3]

    plt.ylim(0, 80)
    plt.yticks(np.arange(0, 90, 10))
    plt.ylabel('Quantity of Fruit')
    plt.title('Number of Fruit per Person')

    plt.bar(x, y1, color='red', label='apples', width=0.5)
    plt.bar(x, y2, bottom=y1, color='yellow', label='bananas', width=0.5)
    plt.bar(x, y3, bottom=y1+y2, color='#ff8000', label='oranges', width=0.5)
    plt.bar(x, y4, bottom=y1+y2+y3, color='#ffe5b4',
            label='peaches', width=0.5)

    plt.legend()
    plt.show()
