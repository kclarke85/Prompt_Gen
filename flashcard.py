# # # # import streamlit as st
# # # # import openai
# # # # from typing import Dict, List
# # # #
# # # # # IMPORTANT: Replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key
# # # # openai.api_key = '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'
# # # #
# # # # # Define subjects and their topics
# # # # SUBJECTS = {
# # # #     "Math": [
# # # #         "Algebra",
# # # #         "Geometry",
# # # #         "Trigonometry",
# # # #         "Pre-Algebra",
# # # #         "Basic Arithmetic"
# # # #     ],
# # # #     "Science": [
# # # #         "Biology",
# # # #         "Chemistry",
# # # #         "Physics",
# # # #         "Environmental Science",
# # # #         "Earth Science"
# # # #     ],
# # # #     "History": [
# # # #         "World History",
# # # #         "US History",
# # # #         "Ancient Civilizations",
# # # #         "Geography",
# # # #         "Social Studies"
# # # #     ],
# # # #     "Grammar": [
# # # #         "Sentence Structure",
# # # #         "Parts of Speech",
# # # #         "Punctuation",
# # # #         "Verb Tenses",
# # # #         "Writing Skills"
# # # #     ],
# # # #     "English Literature": [
# # # #         "Reading Comprehension",
# # # #         "Literary Devices",
# # # #         "Story Analysis",
# # # #         "Poetry",
# # # #         "Novel Studies"
# # # #     ]
# # # # }
# # # #
# # # #
# # # # class EducationalChatbot:
# # # #     def __init__(self):
# # # #         pass
# # # #
# # # #     def generate_question(self, subject: str, topic: str) -> Dict[str, str]:
# # # #         """Generate an educational multiple-choice question using OpenAI API."""
# # # #         try:
# # # #             # Detailed prompt for generating educational questions
# # # #             prompt = f"""Create an educational multiple-choice question for a middle school student
# # # #             with the following specifications:
# # # #             - Subject: {subject}
# # # #             - Topic: {topic}
# # # #             - Format:
# # # #               1. Question text
# # # #               2. Four answer choices (A, B, C, D)
# # # #               3. Correct answer (A, B, C, or D)
# # # #
# # # #             Example output:
# # # #             What is the capital of France?
# # # #             A) London
# # # #             B) Berlin
# # # #             C) Paris
# # # #             D) Rome
# # # #             Correct Answer: C
# # # #
# # # #             Your question:"""
# # # #
# # # #             # Use OpenAI's chat completion API
# # # #             response = openai.ChatCompletion.create(
# # # #                 model="gpt-3.5-turbo",
# # # #                 messages=[
# # # #                     {"role": "system",
# # # #                      "content": "You are an educational question generator for middle school students."},
# # # #                     {"role": "user", "content": prompt}
# # # #                 ],
# # # #                 temperature=0.7,
# # # #                 max_tokens=300,
# # # #                 n=1
# # # #             )
# # # #
# # # #             # Extract the question content
# # # #             question_text = response['choices'][0]['message']['content'].strip()
# # # #
# # # #             # Parse the question
# # # #             lines = question_text.split('\n')
# # # #             question = lines[0]
# # # #             choices = [line.strip() for line in lines[1:5] if line.strip()]
# # # #             correct_answer = lines[-1].split(': ')[1].strip()
# # # #
# # # #             return {
# # # #                 "question": question,
# # # #                 "choices": choices,
# # # #                 "correct_answer": correct_answer
# # # #             }
# # # #
# # # #         except Exception as e:
# # # #             st.error(f"Error generating question: {e}")
# # # #             return None
# # # #
# # # #
# # # # def main():
# # # #     st.title("🎓 Middle School Study Buddy")
# # # #
# # # #     # Sidebar for configuration
# # # #     st.sidebar.header("Study Settings")
# # # #
# # # #     # Subject selection
# # # #     subject = st.sidebar.selectbox(
# # # #         "Select Subject",
# # # #         list(SUBJECTS.keys())
# # # #     )
# # # #
# # # #     # Topic selection based on subject
# # # #     topic = st.sidebar.selectbox(
# # # #         "Select Topic",
# # # #         SUBJECTS[subject]
# # # #     )
# # # #
# # # #     # Number of questions
# # # #     num_questions = st.sidebar.slider(
# # # #         "Number of Questions",
# # # #         min_value=1,
# # # #         max_value=10,
# # # #         value=5
# # # #     )
# # # #
# # # #     # Initialize chatbot
# # # #     chatbot = EducationalChatbot()
# # # #
# # # #     # Generate questions
# # # #     if st.sidebar.button("Generate Questions"):
# # # #         questions = []
# # # #         for _ in range(num_questions):
# # # #             question = chatbot.generate_question(subject, topic)
# # # #             if question:
# # # #                 questions.append(question)
# # # #
# # # #         # Display questions as flashcards
# # # #         if questions:
# # # #             for i, q in enumerate(questions, 1):
# # # #                 with st.expander(f"Question {i}"):
# # # #                     st.write(q['question'])
# # # #                     selected_answer = st.radio(
# # # #                         "Select your answer:",
# # # #                         q['choices'],
# # # #                         key=f"q_{i}"
# # # #                     )
# # # #
# # # #                     if st.button(f"Check Answer for Question {i}"):
# # # #                         if selected_answer == q['correct_answer']:
# # # #                             st.success("Correct! 🎉")
# # # #                         else:
# # # #                             st.error(f"Incorrect. The correct answer is: {q['correct_answer']}")
# # # #         else:
# # # #             st.warning("Could not generate questions. Please check your API key and connection.")
# # # #
# # # #
# # # # if __name__ == "__main__":
# # # #     main()
# # # import streamlit as st
# # # from typing import Dict, List
# # # import requests  # For interacting with the Claude API
# # #
# # # # IMPORTANT: Replace 'YOUR_CLAUDE_API_TOKEN' with your actual Claude AI token
# # # CLAUDE_API_URL = "https://api.anthropic.com/v1/complete"  # Adjust this URL based on the specific endpoint
# # # CLAUDE_API_KEY = "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"
# # #
# # # # Define subjects and their topics
# # # SUBJECTS = {
# # #     "Math": [
# # #         "Algebra",
# # #         "Geometry",
# # #         "Trigonometry",
# # #         "Pre-Algebra",
# # #         "Basic Arithmetic"
# # #     ],
# # #     "Science": [
# # #         "Biology",
# # #         "Chemistry",
# # #         "Physics",
# # #         "Environmental Science",
# # #         "Earth Science"
# # #     ],
# # #     "History": [
# # #         "World History",
# # #         "US History",
# # #         "Ancient Civilizations",
# # #         "Geography",
# # #         "Social Studies"
# # #     ],
# # #     "Grammar": [
# # #         "Sentence Structure",
# # #         "Parts of Speech",
# # #         "Punctuation",
# # #         "Verb Tenses",
# # #         "Writing Skills"
# # #     ],
# # #     "English Literature": [
# # #         "Reading Comprehension",
# # #         "Literary Devices",
# # #         "Story Analysis",
# # #         "Poetry",
# # #         "Novel Studies"
# # #     ]
# # # }
# # #
# # #
# # # class EducationalChatbot:
# # #     def __init__(self):
# # #         pass
# # #
# # #     def generate_question(self, subject: str, topic: str) -> Dict[str, str]:
# # #         """Generate an educational multiple-choice question using Claude AI."""
# # #         try:
# # #             # Detailed prompt for generating educational questions
# # #             prompt = f"""Create an educational multiple-choice question for a middle school student
# # #             with the following specifications:
# # #             - Subject: {subject}
# # #             - Topic: {topic}
# # #             - Format:
# # #               1. Question text
# # #               2. Four answer choices (A, B, C, D)
# # #               3. Correct answer (A, B, C, or D)
# # #
# # #             Example output:
# # #             What is the capital of France?
# # #             A) London
# # #             B) Berlin
# # #             C) Paris
# # #             D) Rome
# # #             Correct Answer: C
# # #
# # #             Your question:"""
# # #
# # #             # Send request to Claude API
# # #             headers = {
# # #                 "Authorization": f"Bearer {CLAUDE_API_KEY}",
# # #                 "Content-Type": "application/json"
# # #             }
# # #             payload = {
# # #                 "model": "claude-2",  # Update with the correct model if needed
# # #                 "prompt": prompt,
# # #                 "max_tokens_to_sample": 300,
# # #                 "temperature": 0.7
# # #             }
# # #
# # #             response = requests.post(CLAUDE_API_URL, headers=headers, json=payload)
# # #
# # #             if response.status_code == 200:
# # #                 data = response.json()
# # #                 question_text = data["completion"].strip()
# # #
# # #                 # Parse the question
# # #                 lines = question_text.split('\n')
# # #                 question = lines[0]
# # #                 choices = [line.strip() for line in lines[1:5] if line.strip()]
# # #                 correct_answer = lines[-1].split(': ')[1].strip()
# # #
# # #                 return {
# # #                     "question": question,
# # #                     "choices": choices,
# # #                     "correct_answer": correct_answer
# # #                 }
# # #             else:
# # #                 st.error(f"Error from Claude API: {response.json().get('error', 'Unknown error')}")
# # #                 return None
# # #
# # #         except Exception as e:
# # #             st.error(f"Error generating question: {e}")
# # #             return None
# # #
# # #
# # # def main():
# # #     st.title("🎓 Middle School Study Buddy")
# # #
# # #     # Sidebar for configuration
# # #     st.sidebar.header("Study Settings")
# # #
# # #     # Subject selection
# # #     subject = st.sidebar.selectbox(
# # #         "Select Subject",
# # #         list(SUBJECTS.keys())
# # #     )
# # #
# # #     # Topic selection based on subject
# # #     topic = st.sidebar.selectbox(
# # #         "Select Topic",
# # #         SUBJECTS[subject]
# # #     )
# # #
# # #     # Number of questions
# # #     num_questions = st.sidebar.slider(
# # #         "Number of Questions",
# # #         min_value=1,
# # #         max_value=10,
# # #         value=5
# # #     )
# # #
# # #     # Initialize chatbot
# # #     chatbot = EducationalChatbot()
# # #
# # #     # Generate questions
# # #     if st.sidebar.button("Generate Questions"):
# # #         questions = []
# # #         for _ in range(num_questions):
# # #             question = chatbot.generate_question(subject, topic)
# # #             if question:
# # #                 questions.append(question)
# # #
# # #         # Display questions as flashcards
# # #         if questions:
# # #             for i, q in enumerate(questions, 1):
# # #                 with st.expander(f"Question {i}"):
# # #                     st.write(q['question'])
# # #                     selected_answer = st.radio(
# # #                         "Select your answer:",
# # #                         q['choices'],
# # #                         key=f"q_{i}"
# # #                     )
# # #
# # #                     if st.button(f"Check Answer for Question {i}"):
# # #                         if selected_answer == q['correct_answer']:
# # #                             st.success("Correct! 🎉")
# # #                         else:
# # #                             st.error(f"Incorrect. The correct answer is: {q['correct_answer']}")
# # #         else:
# # #             st.warning("Could not generate questions. Please check your API key and connection.")
# # #
# # #
# # # if __name__ == "__main__":
# # #
# # # Replace with your actual token when deploying
# #
# #
# # # Replace with your actual token when deploying
# # #GOOGLE_API_TOKEN = "AIzaSyCFU0Ogo8N-aFqDkdh5r-b1mEDStwN9K_Y"
# #
# #
# # # Replace with your actual token when deploying
# # # #GOOGLE_API_TOKEN = "AIzaSyCFU0Ogo8N-aFqDkdh5r-b1mEDStwN9K_Y"
# # # import streamlit as st
# # # import google.generativeai as genai
# # # import pandas as pd
# # # import io
# # #
# # # # Hardcoded API Key - REPLACE WITH YOUR ACTUAL GOOGLE AI API KEY
# # # GOOGLE_API_KEY = 'AIzaSyCFU0Ogo8N-aFqDkdh5r-b1mEDStwN9K_Y'
# # #
# # #
# # # # Configure Google AI
# # # def configure_google_ai():
# # #     genai.configure(api_key=GOOGLE_API_KEY)
# # #     return genai.GenerativeModel('gemini-pro')
# # #
# # #
# # # # Generate comprehensive Q&A content
# # # def generate_comprehensive_qa(model, main_topic, subjects, num_questions):
# # #     # Construct a prompt to generate multiple questions and answers
# # #     prompt = f"""
# # #     Create a comprehensive multi-subject Q&A set about {main_topic}.
# # #     Cover these subjects: {', '.join(subjects)}
# # #
# # #     Generate {num_questions} unique, in-depth questions and answers.
# # #
# # #     Format each entry as:
# # #     Question|Answer|Subject|Difficulty
# # #
# # #     Ensure questions:
# # #     - Are varied and explore different aspects
# # #     - Demonstrate interdisciplinary connections
# # #     - Range from basic to advanced understanding
# # #     """
# # #
# # #     # Generate Q&A content
# # #     qa_response = model.generate_content(prompt)
# # #     return qa_response.text
# # #
# # #
# # # # Parse Q&A into DataFrame
# # # def parse_qa_content(qa_text):
# # #     qa_lines = qa_text.split('\n')
# # #     qa_data = []
# # #
# # #     for line in qa_lines:
# # #         if '|' in line:
# # #             try:
# # #                 question, answer, subject, difficulty = line.split('|')
# # #                 qa_data.append({
# # #                     'Question': question.strip(),
# # #                     'Answer': answer.strip(),
# # #                     'Subject': subject.strip(),
# # #                     'Difficulty': difficulty.strip()
# # #                 })
# # #             except ValueError:
# # #                 continue
# # #
# # #     return pd.DataFrame(qa_data)
# # #
# # #
# # # # Main Streamlit app
# # # def main():
# # #     st.title("🧠 Multi-Subject Q&A Flashcard Generator")
# # #
# # #     # Main topic input
# # #     main_topic = st.text_input("Enter the main topic:",
# # #                                placeholder="Climate Change")
# # #
# # #     # Subject selection
# # #     available_subjects = [
# # #         "Science", "Biology", "Chemistry", "Physics",
# # #         "Environmental Studies", "Geography",
# # #         "Social Studies", "Economics",
# # #         "Mathematics", "Technology"
# # #     ]
# # #     selected_subjects = st.multiselect(
# # #         "Select relevant subjects:",
# # #         available_subjects,
# # #         default=["Science", "Environmental Studies"]
# # #     )
# # #
# # #     # Number of questions
# # #     num_questions = st.slider(
# # #         "Number of Q&A Flashcards",
# # #         min_value=5,
# # #         max_value=30,
# # #         value=15
# # #     )
# # #
# # #     # Generate button
# # #     if st.button("Generate Comprehensive Q&A Flashcards"):
# # #         # Validate inputs
# # #         if not main_topic:
# # #             st.error("Please enter a main topic")
# # #             return
# # #
# # #         if not selected_subjects:
# # #             st.error("Please select at least one subject")
# # #             return
# # #
# # #         try:
# # #             # Configure model
# # #             model = configure_google_ai()
# # #
# # #             # Generate Q&A content
# # #             with st.spinner("Generating comprehensive Q&A..."):
# # #                 qa_text = generate_comprehensive_qa(
# # #                     model,
# # #                     main_topic,
# # #                     selected_subjects,
# # #                     num_questions
# # #                 )
# # #
# # #             # Parse Q&A into DataFrame
# # #             qa_df = parse_qa_content(qa_text)
# # #
# # #             # Display Q&A
# # #             st.subheader(f"Q&A Flashcards on {main_topic}")
# # #             st.dataframe(qa_df)
# # #
# # #             # Export options
# # #             if not qa_df.empty:
# # #                 # CSV Export
# # #                 csv = qa_df.to_csv(index=False)
# # #                 st.download_button(
# # #                     label="Download Flashcards (CSV)",
# # #                     data=csv,
# # #                     file_name=f"{main_topic.replace(' ', '_')}_flashcards.csv",
# # #                     mime="text/csv"
# # #                 )
# # #
# # #                 # Detailed Text Export
# # #                 text_content = io.StringIO()
# # #                 text_content.write(f"Comprehensive Q&A Flashcards: {main_topic}\n")
# # #                 text_content.write(f"Subjects: {', '.join(selected_subjects)}\n\n")
# # #
# # #                 for idx, row in qa_df.iterrows():
# # #                     text_content.write(f"Flashcard {idx + 1}:\n")
# # #                     text_content.write(f"Question: {row['Question']}\n")
# # #                     text_content.write(f"Answer: {row['Answer']}\n")
# # #                     text_content.write(f"Subject: {row['Subject']}\n")
# # #                     text_content.write(f"Difficulty: {row['Difficulty']}\n\n")
# # #
# # #                 st.download_button(
# # #                     label="Download Flashcards (Text)",
# # #                     data=text_content.getvalue(),
# # #                     file_name=f"{main_topic.replace(' ', '_')}_flashcards.txt",
# # #                     mime="text/plain"
# # #                 )
# # #
# # #         except Exception as e:
# # #             st.error(f"An error occurred: {e}")
# # #
# # #     # Additional Information
# # #     st.sidebar.header("How to Use")
# # #     st.sidebar.markdown("""
# # #     1. Enter a main topic
# # #     2. Select relevant subjects
# # #     3. Choose number of flashcards
# # #     4. Click "Generate"
# # #     5. Review and download flashcards
# # #     """)
# # #
# # #
# # # if __name__ == "__main__":
# # #     main()
# #
# # import streamlit as st
# # import google.generativeai as genai
# # import pandas as pd
# # import io
# #
# # # Hardcoded API Key - REPLACE WITH YOUR ACTUAL GOOGLE AI API KEY
# # GOOGLE_API_KEY = 'AIzaSyCFU0Ogo8N-aFqDkdh5r-b1mEDStwN9K_Y'
# #
# #
# # # Configure Google AI
# # def configure_google_ai():
# #     genai.configure(api_key=GOOGLE_API_KEY)
# #     return genai.GenerativeModel('gemini-pro')
# #
# #
# # # Generate comprehensive Q&A content
# # def generate_comprehensive_qa(model, main_topic, subjects, num_questions):
# #     # Construct a prompt to generate multiple questions and answers
# #     prompt = f"""
# #     Create a comprehensive multi-subject Q&A set about {main_topic}.
# #     Cover these subjects: {', '.join(subjects)}
# #
# #     Generate {num_questions} unique, in-depth questions and answers.
# #
# #     Format each entry as:
# #     Question|Answer|Subject|Difficulty
# #
# #     Ensure questions:
# #     - Are varied and explore different aspects
# #     - Demonstrate interdisciplinary connections
# #     - Range from basic to advanced understanding
# #     """
# #
# #     # Generate Q&A content
# #     qa_response = model.generate_content(prompt)
# #     return qa_response.text
# #
# #
# # # Parse Q&A into DataFrame
# # def parse_qa_content(qa_text):
# #     qa_lines = qa_text.split('\n')
# #     qa_data = []
# #
# #     for line in qa_lines:
# #         if '|' in line:
# #             try:
# #                 question, answer, subject, difficulty = line.split('|')
# #                 qa_data.append({
# #                     'Question': question.strip(),
# #                     'Answer': answer.strip(),
# #                     'Subject': subject.strip(),
# #                     'Difficulty': difficulty.strip()
# #                 })
# #             except ValueError:
# #                 continue
# #
# #     return pd.DataFrame(qa_data)
# #
# #
# # # Main Streamlit app
# # def main():
# #     st.title("🧠 Multi-Subject Q&A Flashcard Generator")
# #
# #     # Main topic input
# #     main_topic = st.text_input("Enter the main topic:",
# #                                placeholder="Climate Change")
# #
# #     # Subject selection
# #     available_subjects = [
# #         "Science", "Biology", "Chemistry", "Physics",
# #         "Environmental Studies", "Geography",
# #         "Social Studies", "Economics",
# #         "Mathematics", "Technology"
# #     ]
# #     selected_subjects = st.multiselect(
# #         "Select relevant subjects:",
# #         available_subjects,
# #         default=["Science", "Environmental Studies"]
# #     )
# #
# #     # Number of questions
# #     num_questions = st.slider(
# #         "Number of Q&A Flashcards",
# #         min_value=5,
# #         max_value=30,
# #         value=15
# #     )
# #
# #     # Generate button
# #     if st.button("Generate Comprehensive Q&A Flashcards"):
# #         # Validate inputs
# #         if not main_topic:
# #             st.error("Please enter a main topic")
# #             return
# #
# #         if not selected_subjects:
# #             st.error("Please select at least one subject")
# #             return
# #
# #         try:
# #             # Configure model
# #             model = configure_google_ai()
# #
# #             # Generate Q&A content
# #             with st.spinner("Generating comprehensive Q&A..."):
# #                 qa_text = generate_comprehensive_qa(
# #                     model,
# #                     main_topic,
# #                     selected_subjects,
# #                     num_questions
# #                 )
# #
# #             # Parse Q&A into DataFrame
# #             qa_df = parse_qa_content(qa_text)
# #
# #             # Display Q&A
# #             st.subheader(f"Q&A Flashcards on {main_topic}")
# #             st.dataframe(qa_df)
# #
# #             # Export options
# #             if not qa_df.empty:
# #                 # CSV Export
# #                 csv = qa_df.to_csv(index=False)
# #                 st.download_button(
# #                     label="Download Flashcards (CSV)",
# #                     data=csv,
# #                     file_name=f"{main_topic.replace(' ', '_')}_flashcards.csv",
# #                     mime="text/csv"
# #                 )
# #
# #                 # Detailed Text Export
# #                 text_content = io.StringIO()
# #                 text_content.write(f"Comprehensive Q&A Flashcards: {main_topic}\n")
# #                 text_content.write(f"Subjects: {', '.join(selected_subjects)}\n\n")
# #
# #                 for idx, row in qa_df.iterrows():
# #                     text_content.write(f"Flashcard {idx + 1}:\n")
# #                     text_content.write(f"Question: {row['Question']}\n")
# #                     text_content.write(f"Answer: {row['Answer']}\n")
# #                     text_content.write(f"Subject: {row['Subject']}\n")
# #                     text_content.write(f"Difficulty: {row['Difficulty']}\n\n")
# #
# #                 st.download_button(
# #                     label="Download Flashcards (Text)",
# #                     data=text_content.getvalue(),
# #                     file_name=f"{main_topic.replace(' ', '_')}_flashcards.txt",
# #                     mime="text/plain"
# #                 )
# #
# #         except Exception as e:
# #             st.error(f"An error occurred: {e}")
# #
# #     # Additional Information
# #     st.sidebar.header("How to Use")
# #     st.sidebar.markdown("""
# #     1. Enter a main topic
# #     2. Select relevant subjects
# #     3. Choose number of flashcards
# #     4. Click "Generate"
# #     5. Review and download flashcards
# #     """)
# #
# #
# # if __name__ == "__main__":
# # #     main()
# import streamlit as st
# import google.generativeai as genai
# import pandas as pd
# import io
#
# # Hardcoded API Key - REPLACE WITH YOUR ACTUAL GOOGLE AI API KEY
# GOOGLE_API_KEY = 'AIzaSyCFU0Ogo8N-aFqDkdh5r-b1mEDStwN9K_Y'
#
# # Configure Google AI
# def configure_google_ai():
#     genai.configure(api_key=GOOGLE_API_KEY)
#     return genai.GenerativeModel('gemini-pro')
#
#
# # Generate comprehensive Q&A content
# def generate_comprehensive_qa(model, main_topic, subjects, num_questions):
#     # Construct a prompt to generate multiple questions and answers
#     prompt = f"""
#     Create a comprehensive multi-subject Q&A set about {main_topic}.
#     Cover these subjects: {', '.join(subjects)}
#
#     Generate {num_questions} unique, in-depth questions and answers.
#
#     Format each entry as:
#     Question|Answer|Subject|Difficulty
#
#     Ensure questions:
#     - Are varied and explore different aspects
#     - Demonstrate interdisciplinary connections
#     - Range from basic to advanced understanding
#     """
#
#     # Generate Q&A content
#     qa_response = model.generate_content(prompt)
#     return qa_response.text
#
#
# # Parse Q&A into DataFrame
# def parse_qa_content(qa_text):
#     qa_lines = qa_text.split('\n')
#     qa_data = []
#
#     for line in qa_lines:
#         if '|' in line:
#             try:
#                 question, answer, subject, difficulty = line.split('|')
#                 qa_data.append({
#                     'Question': question.strip(),
#                     'Answer': answer.strip(),
#                     'Subject': subject.strip(),
#                     'Difficulty': difficulty.strip()
#                 })
#             except ValueError:
#                 continue
#
#     return pd.DataFrame(qa_data)
#
#
# # Main Streamlit app
# def main():
#     # Display the image in the header
#     st.image(
#         "https://images.pexels.com/photos/21696/pexels-photo.jpg?auto=compress&cs=tinysrgb&w=600",
#         use_column_width=True
#     )
#
#     st.title("🧠 Multi-Subject Q&A Flashcard Generator")
#
#     # Main topic input
#     main_topic = st.text_input("Enter the main topic:",
#                                placeholder="Climate Change")
#
#     # Subject selection
#     available_subjects = [
#         "Science", "Biology", "Chemistry", "Physics",
#         "Environmental Studies", "Geography",
#         "Social Studies", "Economics",
#         "Mathematics", "Technology"
#     ]
#     selected_subjects = st.multiselect(
#         "Select relevant subjects:",
#         available_subjects,
#         default=["Science", "Environmental Studies"]
#     )
#
#     # Number of questions
#     num_questions = st.slider(
#         "Number of Q&A Flashcards",
#         min_value=5,
#         max_value=30,
#         value=15
#     )
#
#     # Generate button
#     if st.button("Generate Comprehensive Q&A Flashcards"):
#         # Validate inputs
#         if not main_topic:
#             st.error("Please enter a main topic")
#             return
#
#         if not selected_subjects:
#             st.error("Please select at least one subject")
#             return
#
#         try:
#             # Configure model
#             model = configure_google_ai()
#
#             # Generate Q&A content
#             with st.spinner("Generating comprehensive Q&A..."):
#                 qa_text = generate_comprehensive_qa(
#                     model,
#                     main_topic,
#                     selected_subjects,
#                     num_questions
#                 )
#
#             # Parse Q&A into DataFrame
#             qa_df = parse_qa_content(qa_text)
#
#             # Display Q&A
#             st.subheader(f"Q&A Flashcards on {main_topic}")
#             st.dataframe(qa_df)
#
#             # Export options
#             if not qa_df.empty:
#                 # Detailed Text Export
#                 text_content = io.StringIO()
#                 text_content.write(f"Comprehensive Q&A Flashcards: {main_topic}\n")
#                 text_content.write(f"Subjects: {', '.join(selected_subjects)}\n\n")
#
#                 for idx, row in qa_df.iterrows():
#                     text_content.write(f"Flashcard {idx + 1}:\n")
#                     text_content.write(f"Question: {row['Question']}\n")
#                     text_content.write(f"Answer: {row['Answer']}\n")
#                     text_content.write(f"Subject: {row['Subject']}\n")
#                     text_content.write(f"Difficulty: {row['Difficulty']}\n\n")
#
#                 st.download_button(
#                     label="Download Flashcards (Text)",
#                     data=text_content.getvalue(),
#                     file_name=f"{main_topic.replace(' ', '_')}_flashcards.txt",
#                     mime="text/plain"
#                 )
#
#         except Exception as e:
#             st.error(f"An error occurred: {e}")
#
#     # Additional Information
#     st.sidebar.header("How to Use")
#     st.sidebar.markdown("""
#     1. Enter a main topic
#     2. Select relevant subjects
#     3. Choose number of flashcards
#     4. Click "Generate"
#     5. Review and download flashcards
#     """)
#
#     # Add footer with copyright
#     st.markdown(
#         """
#         <style>
#         .footer {
#             position: fixed;
#             bottom: 0;
#             left: 0;
#             right: 0;
#             background-color: #f1f1f1;
#             text-align: center;
#             padding: 10px 0;
#             font-size: 12px;
#         }
#         </style>
#         <div class="footer">
#             © Encounter Engineering 2024-25
#         </div>
#         """,
#         unsafe_allow_html=True
#     )
#
#
# if __name__ == "__main__":
#     main()
#
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