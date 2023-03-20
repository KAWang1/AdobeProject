import matplotlib.pyplot as plt

def display_color_palette(hex_colors):
    # Create a list of RGB tuples from the hex color values
    rgb_colors = [(int(hex_color[1:3], 16) / 255.0,
                   int(hex_color[3:5], 16) / 255.0,
                   int(hex_color[5:], 16) / 255.0)
                  for hex_color in hex_colors]

    # Create a color palette using the RGB tuples
    plt.figure(figsize=(len(rgb_colors), 1))
    plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
    for i, color in enumerate(rgb_colors):
        plt.bar(i, 1, color=color)
    plt.axis('off')
    plt.show()


# Example usage
# display_color_palette(['#FF0000', '#00FF00', '#0000FF'])
# display_color_palette(['#4A4A4A', '#8B8B8B', '#C7C7C7', '#114951', '#177894', '#D8E8F9'])