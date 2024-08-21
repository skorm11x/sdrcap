"""
    Basic plot output for raw sdr readings
"""

import matplotlib.pyplot as plt
import pandas as pd
import argparse
from sdrcap import rtl_interface

stream = 0


parser = argparse.ArgumentParser(description="Process radio parameters.")
parser.add_argument("--stream", type=int, default=0, help="streaming option")
args = parser.parse_args()
assert isinstance(args, argparse.Namespace)

if stream:
    rtl_interface.record_sdr(args=args)
    df_active = pd.read_csv("recordings/stream.csv", sep="[,]", engine="python")
    # df_none = pd.read_csv('nothing/disp0.csv', sep='[,]', engine='python')

    y = df_active["Imaginary Value"]
    x = df_active["Real Value"]

    # plotting the first frame
    graph = plt.plot(x, y)[0]
    plt.ylim(0, 10)
    plt.pause(1)

    # the update loop
    while True:
        # updating the data

        y = df_active["Imaginary Value"]
        x = df_active["Real Value"]

        # removing the older graph
        graph.remove()

        # plotting newer graph
        graph = plt.scatter(x, y, s=10, c="b", marker="s", label="active")

        plt.pause(0.25)

else:
    df_active = pd.read_csv("active/disp0.csv", sep="[,]", engine="python")
    df_none = pd.read_csv("nothing/disp0.csv", sep="[,]", engine="python")

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_title("Active RF 462MHZ vs. Ambient")

    ax1.set_ylabel("Raw Imaginary Value")
    ax1.set_xlabel("Raw Real Value")
    ax1.scatter(
        df_none["Real Value"],
        df_none["Imaginary Value"],
        s=10,
        c="b",
        marker="s",
        label="active",
    )
    ax1.scatter(
        df_active["Real Value"],
        df_active["Imaginary Value"],
        s=10,
        c="r",
        marker="o",
        label="none",
    )
    plt.legend(loc="upper left")
    plt.savefig("active_vs_ambient")