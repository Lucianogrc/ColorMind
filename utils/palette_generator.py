import cv2
import numpy as np
from sklearn.cluster import KMeans
from utils.color_analysis import generate_palette, rgb_to_hex


def extract_dominant_color(image_path, n_clusters=5):
    """
    Loads an image and returns the most dominant RGB color.
    """
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (200, 200))
    pixels = img.reshape((-1, 3))

    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(pixels)

    counts = np.bincount(kmeans.labels_)
    dominant_color = kmeans.cluster_centers_[np.argmax(counts)]
    return tuple(map(int, dominant_color))

def build_palette(image_path, concept="modern"):
    """
    Returns a list of HEX colors based on the dominant color and design concept.
    """
    base_rgb = extract_dominant_color(image_path)
    palette_rgb = generate_palette(base_rgb, concept)
    palette_hex = [rgb_to_hex(color) for color in palette_rgb]
    return palette_hex
