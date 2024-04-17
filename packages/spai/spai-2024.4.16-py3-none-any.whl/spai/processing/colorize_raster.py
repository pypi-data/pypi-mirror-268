import matplotlib
import numpy as np


def colorize_raster(raster, colors=["darkgreen"]):
    raster = raster.squeeze(axis=0)

    # Define color mapping
    color_mapping = {i: colors[i - 1] for i in range(1, len(colors) + 1)}

    # Create an array for colors
    colored_image = np.zeros((raster.shape[0], raster.shape[1], 4))
    for value, color in color_mapping.items():
        colored_image[raster == value] = matplotlib.colors.to_rgba(color)

    return colored_image
