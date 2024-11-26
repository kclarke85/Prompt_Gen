# import streamlit as st
#
# # Page Configuration
# st.set_page_config(
#     page_title="Coming Soon!",
#     page_icon="🚀",
#     layout="centered"
# )
#
# # Custom CSS for Styling
# st.markdown(
#     """
#     <style>
#     body {
#         font-family: "Arial", sans-serif;
#         background: linear-gradient(to right, #f8f9fa, #e9ecef);
#         margin: 0;
#         padding: 0;
#     }
#     .header-image {
#         width: 60%;
#         max-width: 500px;
#         display: block;
#         margin: 20px auto 40px;
#         border-radius: 10px;
#         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
#     }
#     .main-text {
#         font-size: 26px;
#         text-align: center;
#         font-weight: bold;
#         color: #333;
#         margin-bottom: 20px;
#         line-height: 1.5;
#     }
#     .sub-text {
#         font-size: 18px;
#         text-align: center;
#         color: #555;
#         margin-bottom: 40px;
#     }
#     .footer {
#         text-align: center;
#         font-size: 14px;
#         margin-top: 50px;
#         color: #777;
#     }
#     .cta-button {
#         display: block;
#         width: 200px;
#         margin: 20px auto;
#         padding: 12px 20px;
#         font-size: 18px;
#         color: #fff !important;  /* Force white text */
#         background: #28a745;  /* Green background */
#         border: none;
#         border-radius: 5px;
#         text-align: center;
#         text-decoration: none;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )
#
# # Header Image
# st.markdown(
#     f'<img src="https://images.pexels.com/photos/8422134/pexels-photo-8422134.jpeg?auto=compress&cs=tinysrgb&w=600" class="header-image">',
#     unsafe_allow_html=True,
# )
#
# # Main Content
# st.markdown(
#     """
#     <div class="main-text">
#         Supercharge your Middle Schooler’s Test Prep with our AI-powered Flashcard Generator!
#     </div>
#     <div class="sub-text">
#         Create printable, engaging flashcards across multiple subjects in just a few clicks.
#         Perfect for boosting study efficiency and making learning fun!
#     </div>
#     """,
#     unsafe_allow_html=True,
# )
#
# # Call-to-Action Button
# st.markdown(
#     '<a href="#" class="cta-button">December 4, 2024 Try Free</a>',
#     unsafe_allow_html=True,
# )
#
# # Footer
# st.markdown(
#     """
#     <div class="footer">
#         &copy; Encounter Engineering 2024-25
#     </div>
#     """,
#     unsafe_allow_html=True,
# )
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Coming Soon!",
    page_icon="🚀",
    layout="centered"
)

# Custom CSS for Styling
st.markdown(
    """
    <style>
    body {
        font-family: "Arial", sans-serif;
        background: linear-gradient(to right, #f8f9fa, #e9ecef);
        margin: 0;
        padding: 0;
    }
    .header-image {
        width: 60%;
        max-width: 500px;
        display: block;
        margin: 20px auto 40px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    .main-text {
        font-size: 26px;
        text-align: center;
        font-weight: bold;
        color: #333;
        margin-bottom: 20px;
        line-height: 1.5;
    }
    .sub-text {
        font-size: 18px;
        text-align: center;
        color: #555;
        margin-bottom: 40px;
    }
    .footer {
        text-align: center;
        font-size: 14px;
        margin-top: 50px;
        color: #777;
    }
    .cta-button {
        display: block;
        width: 200px;
        margin: 20px auto;
        padding: 12px 20px;
        font-size: 18px;
        color: #fff !important;  /* Force white text */
        background: #28a745;  /* Green background */
        border: none;
        border-radius: 5px;
        text-align: center;
        text-decoration: none;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header Image
st.markdown(
    f'<img src="https://images.pexels.com/photos/8422134/pexels-photo-8422134.jpeg?auto=compress&cs=tinysrgb&w=600" class="header-image">',
    unsafe_allow_html=True,
)

# Main Content
st.markdown(
    """
    <div class="main-text">
        Supercharge your Middle Schooler’s Test Prep with our AI-powered Flashcard Generator!
    </div>
    <div class="sub-text">
        Create printable, engaging flashcards across multiple subjects in just a few clicks.  
        Perfect for boosting study efficiency and making learning fun!
    </div>
    """,
    unsafe_allow_html=True,
)

# Call-to-Action Button
st.markdown(
    '<a href="#" class="cta-button">December 4, 2024 Try Free</a>',
    unsafe_allow_html=True,
)

# Footer
st.markdown(
    """
    <div class="footer">
        &copy; Encounter Engineering 2024-25
    </div>
    """,
    unsafe_allow_html=True,
)
