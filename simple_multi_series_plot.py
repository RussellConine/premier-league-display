# simple_multi_series_plot.py

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd

# create the figure and axes objects
fig, ax = plt.subplots()

y1 = [1, 2, 3, 4] # season and placement
y2 = [2,3,4,1]
y3 = [4,3,2,1]

df = pd.DataFrame([y1,y2,y3])
df.rename(columns={0: 'Arsenal', 1: 'Everton', 2: 'Newcastle', 3: 'Watford'}, inplace=True)

graph_df = pd.DataFrame()

def animate(i):
    global graph_df
    graph_df = graph_df.append(df.loc[i])

    ax.clear()
    for col in graph_df.columns:
        ax.plot(graph_df.index, graph_df[col])

ani = FuncAnimation(fig, animate, frames=len(df.index), interval=500, repeat=False)

# plt.legend()
plt.show()