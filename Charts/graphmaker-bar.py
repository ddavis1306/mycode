#!/usr/bin/env python3

import numpy as np
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

def main():
    N = 4
    minFPS = (90, 120, 150, 70) #LAN length of outage (mins)
    maxFPS = (110, 150, 180, 90) #WAN length of outage (min)
    ind = np.arange(N)    # the x locations for the groups
    # the width of the bars: can also be len(x) sequence
    width = 0.35

    # describe where to display p1
    p1 = plt.bar(ind, minFPS, width)
    # stack p2 on top of p1
    p2 = plt.bar(ind, maxFPS, width, bottom=minFPS)

    # Describe the table metadata
    plt.ylabel("FPS")
    plt.title("2022 POPULAR GPU FPS")
    plt.xticks(ind, ("3080", "4080", "4090", "3070"))
    plt.yticks(np.arange(0, 360, 30))
    plt.legend((p1[0], p2[0]), ("MIN FPS", "MAX FPS"))

    # display the graph
    plt.savefig("/home/student/mycode/gpuChart.png")
    plt.savefig("/home/student/static/gpuChart.png")

if __name__ == "__main__":
    main()

