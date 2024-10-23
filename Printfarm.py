import streamlit as st
import dropbox
from PIL import Image
import os
from datetime import datetime

# Initialize Dropbox client with access token from Streamlit secrets
DROPBOX_ACCESS_TOKEN = st.secrets["DROPBOX_ACCESS_TOKEN"]
dbx = dropbox.Dropbox(DROPBOX_ACCESS_TOKEN)

def upload_to_dropbox(file_bytes, filename, folder="/uploads"):
    """Upload a file to Dropbox"""
    try:
        path = f"{folder}/{filename}"
        dbx.files_upload(file_bytes, path, mode=dropbox.files.WriteMode.overwrite)
        return path
    except Exception as e:
        st.error(f"Error uploading to Dropbox: {str(e)}")
        return None

def main():
    # Header
    st.set_page_config(page_title="3D Print Farm Service", layout="wide")

    st.title("🖨️ Welcome to PrintMaster Pro")
    st.markdown("""
    ### Your One-Stop 3D Printing Solution
    Transform your ideas into reality with our professional 3D printing service.
    Fast turnaround times • High-quality prints • Competitive pricing
    """)

    # Body
    with st.container():
        # Customer Information
        st.header("📋 Order Details")
        col1, col2 = st.columns(2)

        with col1:
            customer_name = st.text_input("Name")
            customer_email = st.text_input("Email")

        with col2:
            phone = st.text_input("Phone Number")
            delivery_address = st.text_area("Delivery Address")

        # Project Details
        st.header("🎯 Project Specifications")

        project_name = st.text_input("Project Name")

        # Material Selection
        material = st.selectbox(
            "Select Material",
            ["PLA", "PETG", "ABS", "TPU", "Nylon", "Resin"]
        )

        # Color Selection
        color = st.color_picker("Choose Color", "#000000")

        # Print Settings
        col3, col4, col5 = st.columns(3)

        with col3:
            layer_height = st.select_slider(
                "Layer Height (mm)",
                options=[0.1, 0.15, 0.2, 0.3]
            )

        with col4:
            infill = st.slider("Infill (%)", 0, 100, 20)

        with col5:
            quantity = st.number_input("Quantity", min_value=1, value=1)

        # File Upload Section
        st.header("📁 Upload Files")

        upload_option = st.radio(
            "Choose upload type:",
            ["Upload STL file", "Upload image to convert to STL"]
        )

        if upload_option == "Upload STL file":
            uploaded_file = st.file_uploader(
                "Upload your STL file",
                type=['stl'],
                help="Upload your 3D model in STL format"
            )

            if uploaded_file:
                # Upload to Dropbox
                file_path = upload_to_dropbox(
                    uploaded_file.getvalue(),
                    f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uploaded_file.name}"
                )
                if file_path:
                    st.success("STL file uploaded successfully!")

        else:
            uploaded_image = st.file_uploader(
                "Upload your image",
                type=['png', 'jpg', 'jpeg'],
                help="Upload an image to convert to STL"
            )

            if uploaded_image:
                # Upload to Dropbox
                file_path = upload_to_dropbox(
                    uploaded_image.getvalue(),
                    f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uploaded_image.name}"
                )
                if file_path:
                    st.success("Image uploaded successfully! We'll convert it to STL format.")

        # Additional Notes
        st.text_area("Additional Notes", height=100)

        # Price Estimation
        st.header("💰 Price Estimation")
        if st.button("Calculate Price"):
            # Add your pricing logic here
            st.info("Price estimation: $XX.XX (Final price may vary based on actual print time and material usage)")

        # Submit Order
        if st.button("Submit Order", type="primary"):
            if not customer_name or not customer_email or not delivery_address:
                st.error("Please fill in all required fields")
            else:
                st.success("Order submitted successfully! We'll contact you shortly with confirmation.")

    # Footer
    st.markdown("""
    ---
    ### PrintMaster Pro
    🏢 7820 Wynfield DR. CUmming GA. 30040  
    📞 (470) 404-5798  
   

    #### Business Hours
    Monday - Friday: 9:00 AM - 6:00 PM  
    Saturday: 10:00 AM - 4:00 PM  
    Sunday: Closed

    *Quality 3D printing services since 2020*
    """)

if __name__ == "__main__":
    main()
