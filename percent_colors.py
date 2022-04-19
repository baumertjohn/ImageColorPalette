# A script to find common colors and percentages in a given image.
# https://towardsdatascience.com/finding-most-common-colors-in-python-47ea0767a06a
# Method 3.1 - K-Means + Proportion Display

from collections import Counter

import cv2 as cv
import numpy as np
from sklearn.cluster import KMeans


def percent_colors(working_img):
    """Takes image loaded with cv2 library and finds 10 most common colors with
    percentages of each. Returns a list of tuples in form of (percent, color)."""
    number_of_colors = KMeans(
        n_clusters=10
    )  # This determines the number of colors to look for
    working_img = cv.cvtColor(working_img, cv.COLOR_BGR2RGB)
    k_cluster = number_of_colors.fit(working_img.reshape(-1, 3))
    n_pixels = len(k_cluster.labels_)
    counter = Counter(k_cluster.labels_)  # count how many pixels per cluster
    percent = {}
    for i in counter:
        percent[i] = int(np.round(counter[i] / n_pixels, 2) * 100)
    percent = dict(sorted(percent.items()))
    # Sort above data into two lists and combine
    color_tuples = []
    for index, item in enumerate(k_cluster.cluster_centers_):
        color = tuple(map(int, item))
        color_tuples.append((percent[index], color))
    return sorted(color_tuples, reverse=True)


def main():
    img = cv.imread("./gfg-660x249.png")
    # img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    # Method 3.1 - Using K-Means clustering + Proportion display
    # ten_colors = percent_colors(NUMBER_OF_COLORS.fit(img.reshape(-1, 3)))

    ten_colors = percent_colors(img)

    for color in ten_colors:
        print(color)


if __name__ == "__main__":
    main()
