import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from collections import Counter
from tkinter import Tk, filedialog

def select_image():
    Tk().withdraw()
    file_path = filedialog.askopenfilename(title="Select a logo image")
    return file_path

def load_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def extract_colors(image, num_colors=5):
    img_resized = cv2.resize(image, (200, 200))  # speed up processing
    pixels = img_resized.reshape((-1, 3))

    kmeans = KMeans(n_clusters=num_colors, random_state=42)
    kmeans.fit(pixels)

    centers = np.round(kmeans.cluster_centers_).astype(int)
    counts = Counter(kmeans.labels_)
    ordered_colors = [centers[i] for i in counts.keys()]

    return ordered_colors

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % tuple(rgb)

def show_palette(colors):
    hex_colors = [rgb_to_hex(color) for color in colors]

    plt.figure(figsize=(8, 2))
    for i, color in enumerate(colors):
        plt.subplot(1, len(colors), i+1)
        plt.axis("off")
        plt.imshow(np.ones((50, 50, 3), dtype=np.uint8) * color)

    plt.suptitle("Dominant Colors")
    plt.show()

    print("Palette HEX codes:")
    for i, color in enumerate(hex_colors):
        print(f"Color {i+1}: {hex_colors[i]}")

if __name__ == "__main__":
    path = select_image()
    if not path:
        print("No image selected.")
        exit()

    img = load_image(path)
    dominant_colors = extract_colors(img)
    show_palette(dominant_colors)
