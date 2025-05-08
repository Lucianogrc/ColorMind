from utils.color_analysis import rgb_to_hex

def build_palette(image_path, concept):
    from utils.color_analysis import extract_dominant_color
    base_rgb = extract_dominant_color(image_path)

    return generate_palette(base_rgb, concept)

def generate_palette(base_rgb, concept):
    import colorsys

    r, g, b = [x / 255.0 for x in base_rgb]
    h, s, v = colorsys.rgb_to_hsv(r, g, b)

    palette = []

    if concept == "modern":
        shifts = [0, 0.08, 0.16, 0.5]
    elif concept == "elegant":
        shifts = [0, 0.03, -0.03, 0.5]
    elif concept == "youthful":
        shifts = [0, 0.2, -0.2, 0.6]
    else:
        shifts = [0, 0.1, 0.2, 0.5]

    for shift in shifts:
        h_mod = (h + shift) % 1.0
        r_new, g_new, b_new = colorsys.hsv_to_rgb(h_mod, s, v)
        rgb = (int(r_new * 255), int(g_new * 255), int(b_new * 255))
        palette.append(rgb)

    return palette