# from PIL import Image, ImageFilter, ImageOps
#
#
# def create_coloring_page(image_path):
#     img = Image.open(image_path)
#     img = img.convert("L")  # Convert to grayscale
#     img = img.filter(ImageFilter.FIND_EDGES)  # Apply edge detection filter
#
#     # Invert the colors to make the background white and edges black
#     img = ImageOps.invert(img)
#
#     img.show()  # Display the result
#     img.save("coloring_page.jpg")  # Save the result
#
#
# create_coloring_page("dogs.jpg")
import streamlit as st
from PIL import Image, ImageFilter, ImageOps, ImageDraw, ImageFont
import io

# Create the Streamlit app
def main():
    # 1. Add a logo at the top (replace with your own image path if needed)
    # st.image('123_1.png', use_column_width=True)  # Ensure you have a logo named 'logo.png'

    # 2. Add a description
    st.write("""
    ## Upload your own photos or royalty-free photos and create custom coloring book pages. 
    Perfect for kids, adults, or seniors.
    """)

    # 3. Add functionality to upload a photo (PNG or JPG)
    uploaded_image = st.file_uploader("Choose a PNG or JPG image", type=["png", "jpg", "jpeg"])

    # 7. Add an input for custom text to add to the image
    user_text = st.text_input("Add custom text to your coloring page", "")

    # 4. Add a submit button
    if st.button("Submit"):
        if uploaded_image is not None:
            # Open the uploaded image
            img = Image.open(uploaded_image)
            coloring_page = create_coloring_page(img, user_text)

            # 5. Display the resulting image
            st.image(coloring_page, caption='Your Coloring Page', use_column_width=True)

            # 6. Add a download button
            download_coloring_page(coloring_page)

# Function to create a coloring page
def create_coloring_page(img, user_text):
    # Convert the image to grayscale and apply edge detection
    img = img.convert("L")
    img = img.filter(ImageFilter.FIND_EDGES)
    img = ImageOps.invert(img)

    # Add the custom text to the image if provided
    if user_text:
        draw = ImageDraw.Draw(img)
        # Load a font (you can use a different font path if needed)
        font = ImageFont.load_default()
        text_position = (10, img.height - 30)  # Position at the bottom-left corner
        draw.text(text_position, user_text, fill="black", font=font)

    return img

# Function to add a download button for the image
def download_coloring_page(image):
    # Save the image to an in-memory file
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='JPEG')
    img_byte_arr = img_byte_arr.getvalue()

    # Add download button
    st.download_button(
        label="Download Coloring Page",
        data=img_byte_arr,
        file_name="coloring_page.jpg",
        mime="image/jpeg"
    )

if __name__ == "__main__":
    main()
