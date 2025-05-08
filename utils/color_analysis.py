import cv2
import numpy as np
from sklearn.cluster import KMeans

def extract_dominant_color(image_path, k=5):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Filtrar blancos y zonas irrelevantes
    lower = np.array([0, 10, 10])
    upper = np.array([180, 255, 255])
    mask = cv2.inRange(img, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)

    result = cv2.cvtColor(result, cv2.COLOR_HSV2RGB)
    result = result.reshape((-1, 3))
    result = result[np.any(result != [0, 0, 0], axis=1)]  # eliminar fondo

    kmeans = KMeans(n_clusters=k, n_init=10)
    kmeans.fit(result)
    counts = np.bincount(kmeans.labels_)
    dominant = kmeans.cluster_centers_[np.argmax(counts)]

    return tuple(map(int, dominant))

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb)
