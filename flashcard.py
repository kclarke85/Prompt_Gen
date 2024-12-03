import streamlit as st
import google.generativeai as genai
import pandas as pd
import io

# Hardcoded API Key - REPLACE WITH YOUR ACTUAL GOOGLE AI API KEY
GOOGLE_API_KEY = 'AIzaSyCFU0Ogo8N-aFqDkdh5r-b1mEDStwN9K_Y'

# Configure Google AI
def configure_google_ai():
    genai.configure(api_key=GOOGLE_API_KEY)
    return genai.GenerativeModel('gemini-pro')


# Generate comprehensive Q&A content
def generate_comprehensive_qa(model, main_topic, subjects, num_questions):
    # Construct a prompt to generate multiple questions and answers
    prompt = f"""
    Create a comprehensive multi-subject Q&A set about {main_topic}.
    Cover these subjects: {', '.join(subjects)}

    Generate {num_questions} unique, in-depth questions and answers.

    Format each entry as:
    Question|Answer|Subject|Difficulty

    Ensure questions:
    - Are varied and explore different aspects
    - Demonstrate interdisciplinary connections
    - Range from basic to advanced understanding
    """

    # Generate Q&A content
    qa_response = model.generate_content(prompt)
    return qa_response.text


# Parse Q&A into DataFrame
def parse_qa_content(qa_text):
    qa_lines = qa_text.split('\n')
    qa_data = []

    for line in qa_lines:
        if '|' in line:
            try:
                question, answer, subject, difficulty = line.split('|')
                qa_data.append({
                    'Question': question.strip(),
                    'Answer': answer.strip(),
                    'Subject': subject.strip(),
                    'Difficulty': difficulty.strip()
                })
            except ValueError:
                continue

    return pd.DataFrame(qa_data)


# Function to download a single flashcard
def download_flashcard(question, answer):
    flashcard_text = f"Question: {question}\nAnswer: {answer}\n"
    return flashcard_text


# Main Streamlit app
def main():
    # Display the image in the header
    st.image(
        "https://images.pexels.com/photos/21696/pexels-photo.jpg?auto=compress&cs=tinysrgb&w=600",
        use_column_width=True
    )

    st.title("🧠 Multi-Subject Q&A Flashcard Generator")

    # Main topic input
    main_topic = st.text_input("Enter the main topic:",
                               placeholder="Climate Change")

    # Subject selection
    available_subjects = [
        "Science", "Biology", "Chemistry", "Physics",
        "Environmental Studies", "Geography",
        "Social Studies", "Economics",
        "Mathematics", "Technology"
    ]
    selected_subjects = st.multiselect(
        "Select relevant subjects:",
        available_subjects,
        default=["Science", "Environmental Studies"]
    )

    # Number of questions
    num_questions = st.slider(
        "Number of Q&A Flashcards",
        min_value=5,
        max_value=30,
        value=15
    )

    # Generate button
    if st.button("Generate Comprehensive Q&A Flashcards"):
        # Validate inputs
        if not main_topic:
            st.error("Please enter a main topic")
            return

        if not selected_subjects:
            st.error("Please select at least one subject")
            return

        try:
            # Configure model
            model = configure_google_ai()

            # Generate Q&A content
            with st.spinner("Generating comprehensive Q&A..."):
                qa_text = generate_comprehensive_qa(
                    model,
                    main_topic,
                    selected_subjects,
                    num_questions
                )

            # Parse Q&A into DataFrame
            qa_df = parse_qa_content(qa_text)

            # Display Q&A
            st.subheader(f"Q&A Flashcards on {main_topic}")
            st.dataframe(qa_df)

            # Export options
            if not qa_df.empty:
                st.markdown("### Download Individual Flashcards")
                for idx, row in qa_df.iterrows():
                    st.write(f"**Flashcard {idx + 1}**")
                    st.write(f"**Question:** {row['Question']}")
                    st.write(f"**Answer:** {row['Answer']}")
                    flashcard_txt = download_flashcard(row['Question'], row['Answer'])
                    st.download_button(
                        label=f"Download Flashcard {idx + 1}",
                        data=flashcard_txt,
                        file_name=f"Flashcard_{idx + 1}.txt",
                        mime="text/plain"
                    )

        except Exception as e:
            st.error(f"An error occurred: {e}")

    # Additional Information
    st.sidebar.header("How to Use")
    st.sidebar.markdown("""
    1. Enter a main topic
    2. Select relevant subjects
    3. Choose number of flashcards
    4. Click "Generate"
    5. Review and download flashcards
    """)

    # Add footer with copyright
    st.markdown(
        """
        <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: #f1f1f1;
            text-align: center;
            padding: 10px 0;
            font-size: 12px;
        }
        </style>
        <div class="footer">
            © Encounter Engineering 2024-25
        </div>
        """,
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
