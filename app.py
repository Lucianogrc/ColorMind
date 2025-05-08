import streamlit as st
from PIL import Image
import os
from utils.palette_generator import build_palette
from utils.color_analysis import extract_dominant_color
from utils.color_analysis import rgb_to_hex
from utils.palette_generator import generate_palette
import uuid
from jinja2 import Environment, FileSystemLoader
from utils.palette_generator import build_palette, generate_palette
from utils.color_analysis import extract_dominant_color, rgb_to_hex

st.set_page_config(page_title="ColorMind", layout="centered")

# Mostrar logo centrado con título
logo_path = "ColorMind Logo.png"
logo = Image.open(logo_path)

st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
st.image(logo, width=160)
st.markdown("<h1 style='text-align: center; font-size: 48px;'>ColorMind</h1>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Subida de logo
st.subheader("Upload a logo and get a custom color palette")
uploaded_file = st.file_uploader("Upload your logo", type=["png", "jpg", "jpeg"])
concept = st.selectbox("Select a design concept", ["modern", "elegant", "youthful"])



if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Your Logo", use_container_width=True)

    # Guardar imagen temporal
    temp_path = "temp_logo.png"
    image.save(temp_path)

    # Detectar color predominante
    dominant_rgb = extract_dominant_color(temp_path)
    dominant_hex = rgb_to_hex(dominant_rgb)

    st.subheader("Detected Dominant Color")
    st.markdown(
        f"<div style='background-color:{dominant_hex}; height:40px;'></div>",
        unsafe_allow_html=True
    )
    st.code(dominant_hex)

    # Generar paleta
    st.subheader("Suggested Palette")
    palette = generate_palette(dominant_rgb, concept)

    hex_palette = [rgb_to_hex(c) for c in palette]
    for hex_color in hex_palette:
        st.markdown(
            f"<div style='background-color:{hex_color}; height:40px;'></div>",
            unsafe_allow_html=True
        )
        st.code(hex_color)

    # Mostrar color principal detectado
    dominant_rgb = extract_dominant_color("temp_logo.png")
    dominant_hex = rgb_to_hex(dominant_rgb)

    st.subheader("🎯 Dominant Color Detected")
    st.markdown(
        f"<div style='background-color:{dominant_hex}; height:40px;'></div>",
        unsafe_allow_html=True
    )
    st.code(dominant_hex)
    # Mostrar mockup de interfaz usando la paleta
    st.subheader("Interface Preview")

    # Asignar roles de color
    primary = hex_palette[0] if len(hex_palette) > 0 else "#000000"
    secondary = hex_palette[1] if len(hex_palette) > 1 else "#111111"
    accent = hex_palette[2] if len(hex_palette) > 2 else "#222222"
    text = "#ffffff"
    background = "#000000"

    # Renderizar HTML con Jinja2
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("mockup.html")
    rendered_html = template.render(
        primary=primary,
        secondary=secondary,
        accent=accent,
        text=text,
        background=background
    )

    # Mostrar HTML en Streamlit
    st.components.v1.html(rendered_html, height=700, scrolling=True)
