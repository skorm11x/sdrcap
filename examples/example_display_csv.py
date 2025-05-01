"""
    Basic plot output for raw sdr readings
"""

import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

base_dir = Path(__file__).parent

active_path = base_dir / "active" / "disp0.csv"
nothing_path = base_dir / "nothing" / "disp0.csv"

df_active = pd.read_csv(active_path, sep="[,]", engine="python")
df_none = pd.read_csv(nothing_path, sep="[,]", engine="python")

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

save_path = Path(base_dir) / "active_vs_ambient.png"

plt.savefig(save_path)
