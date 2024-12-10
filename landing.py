# import streamlit as st
# from datetime import datetime
#
#
# def main():
#     # Page configuration
#     st.set_page_config(
#         page_title="TeachTech Solutions",
#         page_icon="📚",
#         layout="wide"
#     )
#
#     # Custom CSS for styling
#     st.markdown("""
#     <style>
#     .hero-section {
#         background-color: #f0f4f8;
#         padding: 50px 20px;
#         text-align: center;
#         border-radius: 10px;
#     }
#     .feature-section {
#         display: flex;
#         justify-content: space-between;
#         margin-top: 30px;
#     }
#     .feature-card {
#         background-color: white;
#         border-radius: 10px;
#         padding: 20px;
#         box-shadow: 0 4px 6px rgba(0,0,0,0.1);
#         text-align: center;
#         width: 30%;
#     }
#     .copyright {
#         text-align: center;
#         padding: 20px;
#         background-color: #f0f4f8;
#         color: #666;
#     }
#     </style>
#     """, unsafe_allow_html=True)
#
#     # Hero Section
#     st.markdown("""
#     <div class="hero-section">
#         <p>Innovative technology tools designed to simplify teaching and enhance learning experiences</p>
#         <a href="#solutions" style="display: inline-block; background-color: #4CAF50; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; margin-top: 20px;">Explore Our Solutions</a>
#     </div>
#     """, unsafe_allow_html=True)
#
#     # Featured Image
#     st.image(
#         "https://images.pexels.com/photos/5212700/pexels-photo-5212700.jpeg",
#         caption="Transforming Education Through Technology",
#         use_column_width=True
#     )
#
#     # Features Section
#     st.markdown("""
#     <div class="feature-section">
#         <div class="feature-card">
#             <h3>📊 Learning Analytics</h3>
#             <p>Comprehensive student performance tracking and insights</p>
#         </div>
#         <div class="feature-card">
#             <h3>🤖 AI-Powered Tools</h3>
#             <p>Smart assistants to personalize learning experiences</p>
#         </div>
#         <div class="feature-card">
#             <h3>📚 Resource Management</h3>
#             <p>Centralized platform for lesson plans and educational materials</p>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)
#
#     # Solutions Section
#     st.markdown("## Our Solutions", unsafe_allow_html=True)
#
#     col1, col2, col3 = st.columns(3)
#
#     with col1:
#         st.header("Classroom Management")
#         st.write("Streamline administrative tasks and focus on teaching")
#
#     with col2:
#         st.header("Student Engagement")
#         st.write("Interactive tools to make learning more dynamic and fun")
#
#     with col3:
#         st.header("Professional Development")
#         st.write("Continuous learning resources for educators")
#
#     # Footer with Copyright
#     current_year = datetime.now().year
#     st.markdown(f"""
#     <div class="copyright">
#         © {current_year} Encounter Engineering. All Rights Reserved.
#     </div>
#     """, unsafe_allow_html=True)
#
#
# if __name__ == "__main__":
#     main()
import streamlit as st
from datetime import datetime


def main():
    # Page configuration
    st.set_page_config(
        page_title="TeachTech Solutions",
        page_icon="📚",
        layout="wide"
    )

    # Custom CSS for styling
    st.markdown("""
    <style>
    .hero-section {
        background-color: #f0f4f8;
        padding: 50px 20px;
        text-align: center;
        border-radius: 10px;
    }
    .feature-section {
        display: flex;
        justify-content: space-between;
        margin-top: 30px;
    }
    .feature-card {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
        width: 30%;
    }
    .iframe-container {
        margin-top: 20px;
        display: flex;
        justify-content: space-around;
    }
    iframe {
        border: 1px solid #ddd;
        border-radius: 10px;
        width: 300px;
        height: 400px;
    }
    .copyright {
        text-align: center;
        padding: 20px;
        background-color: #f0f4f8;
        color: #666;
    }
    </style>
    """, unsafe_allow_html=True)

    # Hero Section
    st.markdown("""
 <div class="hero-section">
    <img src="https://yt3.ggpht.com/3_qK2m2jT1jyag8JD6KGr0kgpUur7T-G5TxP0sLj_6SKXfEmeqO4ty_66Tox0vbL_OG_f5SBBTE=s88-c-k-c0x00ffffff-no-rj" alt="Logo" style="width: 88px; height: auto; display: block; margin: 0 auto;">
    <p>Innovative technology tools designed to simplify teaching and enhance learning experiences</p>
</div>

    """, unsafe_allow_html=True)

    # Featured Image
    st.image(
        "https://images.pexels.com/photos/5212700/pexels-photo-5212700.jpeg",
        caption="Transforming Education Through Technology",
        use_column_width=True
    )

    # Features Section
    st.markdown("""
    <div class="feature-section">
        <div class="feature-card">
            <h3>📊 Learning Analytics</h3>
            <p>Comprehensive student performance tracking and insights</p>
        </div>
        <div class="feature-card">
            <h3>🤖 AI-Powered Tools</h3>
            <p>Smart assistants to personalize learning experiences</p>
        </div>
        <div class="feature-card">
            <h3>📚 Resource Management</h3>
            <p>Centralized platform for lesson plans and educational materials</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Solutions Section with Embedded Previews
    st.markdown("## Our Solutions", unsafe_allow_html=True)

    st.markdown("""
    <div class="iframe-container">
        <iframe src="https://payhip.com/b/CK8Os"></iframe>
        <iframe src="https://payhip.com/b/W5uIQ" title="Solution 2"></iframe>
        <iframe src="https://payhip.com/b/X0t6C" title="Solution 3"></iframe>
    </div>
    """, unsafe_allow_html=True)

    # Footer with Copyright
    current_year = datetime.now().year
    st.markdown(f"""
    <div class="copyright">
        © {current_year} Encounter Engineering. All Rights Reserved.
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
