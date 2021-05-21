import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def visualise(lst: list):
    """
    Give a visual representation of the given path on the map of Chicago City.
    """
    for point in lst_lat_long:
        ax.scatter(float(point[0]), float(point[1]), zorder=10, alpha=0.8, c='black', s=30)
    ax.set_title('Plotting a path on Chicago map')
    ax.set_xlim(41.65900629, 42.0128288601)
    ax.set_ylim(-87.535052, -87.8367650119)
    for i, txt in enumerate(lst):
        ax.annotate(txt + ' ,' + str(i), (lst_lat_long[i][0], lst_lat_long[i][1]))
    ax.imshow(map_img, zorder=0, extent=Box, aspect='equal')
