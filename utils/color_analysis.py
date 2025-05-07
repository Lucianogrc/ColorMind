import colorsys

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb)

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hsv(rgb):
    return colorsys.rgb_to_hsv(*(c / 255.0 for c in rgb))

def hsv_to_rgb(hsv):
    return tuple(int(c * 255) for c in colorsys.hsv_to_rgb(*hsv))

def generate_palette(base_rgb, concept="modern"):
    """
    Generates a list of 3 RGB colors based on the concept.
    """
    base_hsv = rgb_to_hsv(base_rgb)
    h, s, v = base_hsv

    if concept == "modern":
        colors = [
            base_rgb,
            hsv_to_rgb(((h + 0.08) % 1.0, min(s + 0.2, 1.0), max(v - 0.2, 0.4))),
            hsv_to_rgb(((h + 0.5) % 1.0, s, v))
        ]
    elif concept == "elegant":
        colors = [
            base_rgb,
            hsv_to_rgb((h, min(s + 0.1, 1.0), max(v - 0.3, 0.3))),
            hsv_to_rgb(((h + 0.1) % 1.0, s * 0.5, v * 0.7))
        ]
    elif concept == "youthful":
        colors = [
            base_rgb,
            hsv_to_rgb(((h + 0.1) % 1.0, min(s + 0.3, 1.0), min(v + 0.3, 1.0))),
            hsv_to_rgb(((h + 0.6) % 1.0, s, v))
        ]
    else:
        # Default: complementary + analog
        colors = [
            base_rgb,
            hsv_to_rgb(((h + 0.5) % 1.0, s, v)),       # complementary
            hsv_to_rgb(((h + 0.08) % 1.0, s, v))       # analog
        ]

    return [tuple(map(int, color)) for color in colors]
