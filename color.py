# # from PIL import Image, ImageFilter, ImageOps
# #
# #
# # def create_coloring_page(image_path):
# #     img = Image.open(image_path)
# #     img = img.convert("L")  # Convert to grayscale
# #     img = img.filter(ImageFilter.FIND_EDGES)  # Apply edge detection filter
# #
# #     # Invert the colors to make the background white and edges black
# #     img = ImageOps.invert(img)
# #
# #     img.show()  # Display the result
# #     img.save("coloring_page.jpg")  # Save the result
# #
# #
# # create_coloring_page("dogs.jpg")
# # import streamlit as st
# # from PIL import Image, ImageFilter, ImageOps, ImageDraw, ImageFont
# # import io
# #
# # # Create the Streamlit app
# # def main():
# #     # 1. Add a logo at the top (replace with your own image path if needed)
# #     st.image('123_1.png', use_column_width=True)  # Ensure you have a logo named 'logo.png'
# #
# #     # 2. Add a description
# #     st.write("""
# #     ## Upload your own photos or royalty-free photos and create custom coloring book pages.
# #     Perfect for kids, adults, or seniors.
# #     """)
# #
# #     # 3. Add functionality to upload a photo (PNG or JPG)
# #     uploaded_image = st.file_uploader("Choose a PNG or JPG image", type=["png", "jpg", "jpeg"])
# #
# #     # 7. Add an input for custom text to add to the image
# #     user_text = st.text_input("Add custom text to your coloring page", "")
# #
# #     # 4. Add a submit button
# #     if st.button("Submit"):
# #         if uploaded_image is not None:
# #             # Open the uploaded image
# #             img = Image.open(uploaded_image)
# #             coloring_page = create_coloring_page(img, user_text)
# #
# #             # 5. Display the resulting image
# #             st.image(coloring_page, caption='Your Coloring Page', use_column_width=True)
# #
# #             # 6. Add a download button
# #             download_coloring_page(coloring_page)
# #
# # # Function to create a coloring page
# # def create_coloring_page(img, user_text):
# #     # Convert the image to grayscale and apply edge detection
# #     img = img.convert("L")
# #     img = img.filter(ImageFilter.FIND_EDGES)
# #     img = ImageOps.invert(img)
# #
# #     # Add the custom text to the image if provided
# #     if user_text:
# #         draw = ImageDraw.Draw(img)
# #         # Load a font (you can use a different font path if needed)
# #         font = ImageFont.load_default()
# #         text_position = (10, img.height - 30)  # Position at the bottom-left corner
# #         draw.text(text_position, user_text, fill="black", font=font)
# #
# #     return img
# #
# # # Function to add a download button for the image
# # def download_coloring_page(image):
# #     # Save the image to an in-memory file
# #     img_byte_arr = io.BytesIO()
# #     image.save(img_byte_arr, format='JPEG')
# #     img_byte_arr = img_byte_arr.getvalue()
# #
# #     # Add download button
# #     st.download_button(
# #         label="Download Coloring Page",
# #         data=img_byte_arr,
# #         file_name="coloring_page.jpg",
# #         mime="image/jpeg"
# #     )
# #
# # if __name__ == "__main__":
# #     main()
# import streamlit as st
# from PIL import Image
# import io
#
# # Function to create a poster
# def create_poster(img, poster_size=(7200, 10800)):
#     # Resize the image to the poster size
#     img = img.resize(poster_size, Image.ANTIALIAS)
#     return img
#
# # Function to add a download button for the image
# def download_poster(image):
#     # Save the image to an in-memory file
#     img_byte_arr = io.BytesIO()
#     image.save(img_byte_arr, format='JPEG')
#     img_byte_arr = img_byte_arr.getvalue()
#
#     # Add download button
#     st.download_button(
#         label="Download Poster",
#         data=img_byte_arr,
#         file_name="poster_image.jpg",
#         mime="image/jpeg"
#     )
#
# # Create the Streamlit app
# def main():
#     # 1. Add a logo at the top (replace with your own image path if needed)
#     st.image('123_1.png', use_column_width=True)  # Ensure you have a logo named '123_1.png'
#
#     # 2. Add a description
#     st.write("""
#     ## Upload your image and convert it into a poster.
#     Perfect for decorations, events, or personal use.
#     """)
#
#     # 3. Add functionality to upload a photo (PNG or JPG)
#     uploaded_image = st.file_uploader("Choose a PNG or JPG image", type=["png", "jpg", "jpeg"])
#
#     # 4. Add a submit button
#     if st.button("Create Poster"):
#         if uploaded_image is not None:
#             # Open the uploaded image
#             img = Image.open(uploaded_image)
#             poster_image = create_poster(img)
#
#             # 5. Display the resulting image
#             st.image(poster_image, caption='Your Poster', use_column_width=True)
#
#             # 6. Add a download button
#             download_poster(poster_image)
#
#     # 7. Printing Options
#     st.write("### Choose a printing option:")
#     printing_option = st.selectbox("Select a printing provider:", ["Select", "FedEx", "Walmart", "UPS"])
#
#     # 8. Open link based on selection
#     if printing_option == "FedEx":
#         st.markdown("[Go to FedEx Printing](https://www.fedex.com/en-us/printing.html)")
#     elif printing_option == "Walmart":
#         st.markdown("[Go to Walmart Photo Printing](https://photos.walmart.com/)")
#     elif printing_option == "UPS":
#         st.markdown("[Go to UPS Print Services](https://www.theupsstore.com/print)")
#
# if __name__ == "__main__":
#     main()
# import streamlit as st
# from PIL import Image, ImageFilter, ImageOps, ImageDraw, ImageFont
# import io
# from pathlib import Path
#
# # Set page configuration
# st.set_page_config(
#     page_title="Image Processing Studio",
#     page_icon="🎨",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )
#
# # Apply custom CSS
# st.markdown("""
#     <style>
#     .stApp {
#         max-width: 1200px;
#         margin: 0 auto;
#     }
#     .st-emotion-cache-1v0mbdj.e115fcil1 {
#         width: 100%;
#     }
#     </style>
# """, unsafe_allow_html=True)
#
#
# class ImageProcessor:
#     @staticmethod
#     def create_coloring_page(img, edge_detection_strength=3):
#         # Convert the image to grayscale
#         img = img.convert("L")
#
#         # Apply edge detection with adjustable strength
#         for _ in range(edge_detection_strength):
#             img = img.filter(ImageFilter.FIND_EDGES)
#
#         # Invert and enhance the edges
#         img = ImageOps.invert(img)
#         return img
#
#     @staticmethod
#     def create_poster(img, width, height):
#         # Calculate aspect ratio and resize maintaining proportions
#         img_ratio = img.size[0] / img.size[1]
#         target_ratio = width / height
#
#         if img_ratio > target_ratio:
#             new_width = width
#             new_height = int(width / img_ratio)
#         else:
#             new_height = height
#             new_width = int(height * img_ratio)
#
#         img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
#
#         # Create new white background image
#         background = Image.new('RGB', (width, height), 'white')
#
#         # Paste resized image in center
#         offset = ((width - new_width) // 2, (height - new_height) // 2)
#         background.paste(img, offset)
#
#         return background
#
#
# def add_text_to_image(img, text, position="bottom", font_size=40):
#     draw = ImageDraw.Draw(img)
#     try:
#         font = ImageFont.truetype("arial.ttf", font_size)
#     except:
#         font = ImageFont.load_default()
#
#     # Calculate text position
#     text_bbox = draw.textbbox((0, 0), text, font=font)
#     text_width = text_bbox[2] - text_bbox[0]
#     text_height = text_bbox[3] - text_bbox[1]
#
#     if position == "bottom":
#         text_position = ((img.width - text_width) // 2, img.height - text_height - 20)
#     else:  # top
#         text_position = ((img.width - text_width) // 2, 20)
#
#     # Add text with shadow effect
#     shadow_offset = 2
#     draw.text((text_position[0] + shadow_offset, text_position[1] + shadow_offset),
#               text, fill="gray", font=font)
#     draw.text(text_position, text, fill="black", font=font)
#
#     return img
#
#
# def download_image(image, file_name):
#     img_byte_arr = io.BytesIO()
#     image.save(img_byte_arr, format='PNG')
#     img_byte_arr = img_byte_arr.getvalue()
#
#     return st.download_button(
#         label="⬇️ Download Image",
#         data=img_byte_arr,
#         file_name=file_name,
#         mime="image/png"
#     )
#
#
# def main():
#     # Sidebar configuration
#     with st.sidebar:
#         st.image('123_1.png', use_column_width=True)
#         st.title("Settings")
#
#         mode = st.radio(
#             "Choose Mode",
#             ["Coloring Page Creator", "Poster Generator"],
#             index=0
#         )
#
#         uploaded_file = st.file_uploader(
#             "Upload Image (PNG/JPG)",
#             type=["png", "jpg", "jpeg"]
#         )
#
#     # Main content area
#     st.title("🎨 Image Processing Studio")
#
#     if mode == "Coloring Page Creator":
#         st.header("Coloring Page Creator")
#         st.write("Transform your photos into beautiful coloring pages!")
#
#         col1, col2 = st.columns(2)
#
#         with col1:
#             edge_strength = st.slider(
#                 "Edge Detection Strength",
#                 1, 5, 3,
#                 help="Adjust how pronounced the edges should be"
#             )
#
#         with col2:
#             custom_text = st.text_input(
#                 "Add Custom Text",
#                 placeholder="Enter text to add to your coloring page"
#             )
#
#     else:  # Poster Generator
#         st.header("Poster Generator")
#         st.write("Create high-quality posters from your images!")
#
#         col1, col2 = st.columns(2)
#
#         with col1:
#             poster_size = st.selectbox(
#                 "Choose Poster Size",
#                 [
#                     "A4 (210×297mm)",
#                     "A3 (297×420mm)",
#                     "A2 (420×594mm)",
#                     "A1 (594×841mm)",
#                     "Custom"
#                 ]
#             )
#
#         with col2:
#             if poster_size == "Custom":
#                 width = st.number_input("Width (pixels)", 1000, 10000, 2400)
#                 height = st.number_input("Height (pixels)", 1000, 10000, 3600)
#             else:
#                 # Convert standard sizes to pixels (assuming 300 DPI)
#                 sizes = {
#                     "A4": (2480, 3508),
#                     "A3": (3508, 4961),
#                     "A2": (4961, 7016),
#                     "A1": (7016, 9933)
#                 }
#                 size_key = poster_size.split()[0]
#                 width, height = sizes.get(size_key, (2400, 3600))
#
#     # Process image when uploaded
#     if uploaded_file is not None:
#         try:
#             image = Image.open(uploaded_file)
#
#             # Create columns for before/after comparison
#             col1, col2 = st.columns(2)
#
#             with col1:
#                 st.subheader("Original Image")
#                 st.image(image, use_column_width=True)
#
#             with col2:
#                 st.subheader("Processed Image")
#                 if mode == "Coloring Page Creator":
#                     processed_image = ImageProcessor.create_coloring_page(
#                         image.copy(),
#                         edge_detection_strength=edge_strength
#                     )
#                     if custom_text:
#                         processed_image = add_text_to_image(processed_image, custom_text)
#                     file_name = "coloring_page.png"
#                 else:
#                     processed_image = ImageProcessor.create_poster(
#                         image.copy(),
#                         width,
#                         height
#                     )
#                     file_name = "poster.png"
#
#                 st.image(processed_image, use_column_width=True)
#
#             # Download section
#             st.markdown("---")
#             col1, col2, col3 = st.columns([1, 2, 1])
#
#             with col2:
#                 download_image(processed_image, file_name)
#
#                 if mode == "Poster Generator":
#                     st.markdown("### 🖨️ Print Services")
#                     services = {
#                         "FedEx": "https://www.fedex.com/en-us/printing.html",
#                         "Walmart": "https://photos.walmart.com/",
#                         "UPS": "https://www.theupsstore.com/print",
#                         "Vistaprint": "https://www.vistaprint.com/",
#                     }
#
#                     for service, url in services.items():
#                         st.markdown(f"[{service}]({url})")
#
#         except Exception as e:
#             st.error(f"Error processing image: {str(e)}")
#     else:
#         # Show demo/placeholder when no image is uploaded
#         st.info("👆 Upload an image to get started!")
#
#
# if __name__ == "__main__":
#     main()
import streamlit as st
from PIL import Image, ImageFilter, ImageOps, ImageDraw, ImageFont
import io

# Set page configuration
st.set_page_config(
    page_title="Coloring Page Creator",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS and JavaScript
st.markdown("""
    <style>
    /* Hide Streamlit default header and footer */
    header {visibility: hidden;}
    footer {visibility: hidden;}

    /* Custom styling */
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .main-header {
        text-align: center;
        padding: 2rem 0;
        color: #1E88E5;
    }
    .upload-section {
        background-color: #f5f5f5;
        padding: 2rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .controls-section {
        background-color: #e3f2fd;
        padding: 2rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .result-section {
        background-color: #fff;
        padding: 2rem;
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stButton button {
        width: 100%;
        background-color: #1E88E5;
        color: white;
    }
    .download-button {
        text-align: center;
        padding: 1rem;
    }
    </style>
""", unsafe_allow_html=True)


class ColoringPageCreator:
    @staticmethod
    def process_image(img, edge_detection_strength=3, brightness_adjustment=1.2):
        # Convert to grayscale
        img = img.convert("L")

        # Adjust brightness
        img = ImageOps.autocontrast(img, cutoff=2)

        # Apply edge detection multiple times for stronger edges
        for _ in range(edge_detection_strength):
            img = img.filter(ImageFilter.FIND_EDGES)

        # Invert colors and enhance contrast
        img = ImageOps.invert(img)
        img = ImageOps.autocontrast(img, cutoff=0)

        return img

    @staticmethod
    def add_text(img, text, position="bottom", font_size=40):
        draw = ImageDraw.Draw(img)

        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except:
            font = ImageFont.load_default()

        # Calculate text size and position
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

        if position == "bottom":
            text_position = ((img.width - text_width) // 2, img.height - text_height - 20)
        else:  # top
            text_position = ((img.width - text_width) // 2, 20)

        # Add text with shadow effect
        shadow_offset = 2
        draw.text(
            (text_position[0] + shadow_offset, text_position[1] + shadow_offset),
            text,
            fill="gray",
            font=font
        )
        draw.text(text_position, text, fill="black", font=font)

        return img


def download_image(image, file_name):
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG', quality=95)
    img_byte_arr = img_byte_arr.getvalue()

    return st.download_button(
        label="⬇️ Download Coloring Page",
        data=img_byte_arr,
        file_name=file_name,
        mime="image/png",
        key='download_button'
    )


def main():
    st.markdown('<h1 class="main-header">🎨 Coloring Page Creator</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div style='text-align: center; padding: 0 2rem;'>
        <h3>Transform your photos into beautiful coloring pages!</h3>
        <p>Perfect for kids, adults, and seniors. Upload any image to get started.</p>
    </div>
    """, unsafe_allow_html=True)

    # Create two columns for the main layout
    col1, col2 = st.columns([2, 3])

    with col1:
        st.markdown('<div class="upload-section">', unsafe_allow_html=True)
        uploaded_file = st.file_uploader(
            "Choose an image (PNG or JPG)",
            type=["png", "jpg", "jpeg"],
            help="Upload a clear image with good contrast for best results"
        )
        st.markdown('</div>', unsafe_allow_html=True)

        if uploaded_file:
            st.markdown('<div class="controls-section">', unsafe_allow_html=True)
            edge_strength = st.slider(
                "Edge Detection Strength",
                1, 5, 3,
                help="Adjust how pronounced the edges should be"
            )

            text_options = st.expander("Text Options")
            with text_options:
                custom_text = st.text_input(
                    "Add Custom Text",
                    placeholder="Enter text for your coloring page"
                )
                text_position = st.radio(
                    "Text Position",
                    ["top", "bottom"],
                    index=1
                )
            st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        if uploaded_file:
            try:
                # Process the image
                with st.spinner("Creating your coloring page..."):
                    # Load and process image
                    image = Image.open(uploaded_file)

                    # Create tabs for before/after comparison
                    tab1, tab2 = st.tabs(["Original", "Coloring Page"])

                    with tab1:
                        st.image(image, use_column_width=True)

                    with tab2:
                        # Process image
                        processed_image = ColoringPageCreator.process_image(
                            image.copy(),
                            edge_detection_strength=edge_strength
                        )

                        # Add text if provided
                        if custom_text:
                            processed_image = ColoringPageCreator.add_text(
                                processed_image,
                                custom_text,
                                position=text_position
                            )

                        st.image(processed_image, use_column_width=True)

                        # Center the download button
                        st.markdown('<div class="download-button">', unsafe_allow_html=True)
                        download_image(processed_image, "coloring_page.png")
                        st.markdown('</div>', unsafe_allow_html=True)

            except Exception as e:
                st.error(f"Error processing image: {str(e)}")
                st.info("Please try uploading a different image or adjusting the settings.")

        else:
            st.info("👈 Upload an image to get started!")

            # Show example/preview
            st.markdown("""
            ### Tips for best results:
            - Use images with clear subjects and good contrast
            - Avoid very busy or cluttered images
            - Simple portraits or objects work best
            - Higher resolution images produce better results
            """)


if __name__ == "__main__":
    main()
