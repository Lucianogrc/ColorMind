import streamlit as st
from PIL import Image
from utils.palette_generator import build_palette



st.set_page_config(page_title="ColorMind", layout="centered")

st.title("🎨 ColorMind")
st.subheader("Upload a logo and get a custom color palette")

uploaded_file = st.file_uploader("Upload your logo", type=["png", "jpg", "jpeg"])
concept = st.selectbox("Select a design concept", ["modern", "elegant", "youthful"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Your Logo", use_column_width=True)

    # Save the file temporarily
# Save the file temporarily using PIL (avoids empty file error)
    image.save("temp_logo.png")


    # Generate palette
    st.subheader("🎨 Suggested Palette")
    palette = build_palette("temp_logo.png", concept)

    for hex_color in palette:
        st.markdown(
            f"<div style='background-color:{hex_color}; height:40px;'></div>",
            unsafe_allow_html=True
        )
        st.code(hex_color)
