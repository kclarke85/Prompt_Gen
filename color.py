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
