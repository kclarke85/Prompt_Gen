import streamlit as st

# Hide streamlit header and footer using CSS
hide_streamlit_style = """
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        /* Optionally hide "Made with Streamlit" footer text */
        .reportview-container .main footer {visibility: hidden;}
        /* Hide Streamlit default top padding */
        .block-container {padding-top: 1rem;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Rest of your existing code remains the same
def main() -> None:
    st.set_page_config(
        page_title="QA Test Case Generator",
        page_icon="https://120water.com/wp-content/uploads/2020/05/120WaterAudit_Logo_2C_RGB-1.png"
    )

    # Add custom CSS right after page config
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    # Add header image
    st.image(
        "https://images.pexels.com/photos/9749/hands-water-poor-poverty.jpg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
        use_container_width=True
    )

    st.title("QA Test Case Generator")
    # Rest of your main function code...
