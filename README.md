# 🎨 ColorMind

**ColorMind** is a computer vision-powered tool that helps designers extract the dominant color from a logo or brand image and generates three complementary colors based on a selected design concept. It also provides a live web preview using the generated palette to inspire creative direction.

---

## 📌 Objective

To simplify the workflow for designers by automatically analyzing brand logos and suggesting aesthetically compatible color combinations tailored to specific brand styles (modern, elegant, youthful, etc.). ColorMind also demonstrates how the selected palette would look in a web interface mockup.

---

## 🚀 How It Works

1. Upload a logo or brand image.
2. The system detects the most dominant color using K-Means clustering or histogram analysis.
3. Choose a design concept (e.g., modern, elegant, tech, minimalist).
4. ColorMind generates 3 complementary colors based on that concept.
5. A visual preview of a web page is rendered using the full palette.

---

## 🧠 Technologies Used

- **Python**
- **OpenCV** – for image processing and color extraction
- **Scikit-learn** – for color clustering (KMeans)
- **matplotlib / seaborn** – for color palette visualization
- **Streamlit / Flask** (optional) – for building the interactive UI
- **HTML/CSS** – for rendering the web interface mockup

---

## 📸 Example Use Case

Upload this logo:

![Sample Logo](assets/sample_logo.png)

Output:

- Dominant color: `#1F75FE`
- Suggested palette for **modern** concept:
  - `#1F75FE` (primary)
  - `#0F3057` (dark contrast)
  - `#28C7FA` (accent)
  - `#E3F2FD` (background)

![Preview](assets/mockup_preview.png)
