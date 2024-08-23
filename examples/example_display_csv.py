"""
    Basic plot output for raw sdr readings
"""

import matplotlib.pyplot as plt
import pandas as pd
import argparse
from sdrcap import rtl_interface

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