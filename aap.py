import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

# Ensure font loading works across environments by using a safer default
try:
    font = ImageFont.truetype("arial.ttf", 20)
except IOError:
    font = ImageFont.load_default()

def create_image_from_text(text):
    # Create a blank image with a white background
    width, height = 600, 200
    image = Image.new("RGB", (width, height), color="white")
    
    # Initialize ImageDraw
    draw = ImageDraw.Draw(image)
    
    # Calculate text width and height to center it
    text_width, text_height = draw.textsize(text, font=font)
    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2

    # Add text to the image
    draw.text((text_x, text_y), text, fill="black", font=font)
    
    return image

def main():
    st.set_page_config(page_title="Text-to-Image App", layout="centered")
    st.title("🖼️ Text-to-Image Generator")
    st.write("Enter any text below and see it converted into an image!")

    user_input = st.text_input("Enter text here:")

    if user_input:
        st.write("Preview of the image created from your text:")
        image = create_image_from_text(user_input)
        buf = io.BytesIO()
        image.save(buf, format="PNG")
        byte_im = buf.getvalue()
        st.image(byte_im, caption=f"Image created from: '{user_input}'", use_column_width=True)

if __name__ == "__main__":
    main()
