# # # import streamlit as st
# # # import random
# # # from datetime import datetime
# # # import re
# # #
# # # # Configure Streamlit with correct settings
# # # st.set_page_config(
# # #     page_title="StudyBot",
# # #     page_icon="📚",
# # #     layout="wide",
# # #     initial_sidebar_state="expanded",
# # #     menu_items={
# # #         'Get Help': 'https://github.com/your-repo/studybot',
# # #         'Report a bug': 'https://github.com/your-repo/studybot/issues',
# # #         'About': 'StudyBot - A learning assistant for middle school students'
# # #     }
# # # )
# # #
# # #
# # # class StudyBot:
# # #     def __init__(self):
# # #         self.topics = {
# # #             'math': {
# # #                 'algebra': [
# # #                     {
# # #                         'question': 'Solve for x: 3x - 7 = 20',
# # #                         'answer': '9',
# # #                         'explanation': '1. Add 7 to both sides: 3x = 27\n2. Divide both sides by 3: x = 9\n\nCheck: 3(9) - 7 = 27 - 7 = 20 ✓',
# # #                         'accepted_answers': ['9', 'x=9', 'x = 9', '9.0']
# # #                     }
# # #                 ]
# # #             }
# # #         }
# # #
# # #     def check_answer(self, user_answer, question_data):
# # #         cleaned_answer = re.sub(r'\s+', '', user_answer.lower().strip())
# # #         if 'accepted_answers' in question_data:
# # #             cleaned_accepted_answers = [re.sub(r'\s+', '', ans.lower()) for ans in question_data['accepted_answers']]
# # #             return cleaned_answer in cleaned_accepted_answers
# # #         cleaned_correct = re.sub(r'\s+', '', question_data['answer'].lower())
# # #         return cleaned_answer == cleaned_correct
# # #
# # #
# # # def initialize_session_state():
# # #     if 'bot' not in st.session_state:
# # #         st.session_state['bot'] = StudyBot()
# # #     if 'score' not in st.session_state:
# # #         st.session_state['score'] = 0
# # #     if 'total_questions' not in st.session_state:
# # #         st.session_state['total_questions'] = 0
# # #     if 'current_question' not in st.session_state:
# # #         st.session_state['current_question'] = None
# # #     if 'show_explanation' not in st.session_state:
# # #         st.session_state['show_explanation'] = False
# # #     if 'last_answer_correct' not in st.session_state:
# # #         st.session_state['last_answer_correct'] = None
# # #
# # #
# # # def main():
# # #     initialize_session_state()
# # #
# # #     # Custom CSS to style buttons
# # #     st.markdown("""
# # #         <style>
# # #         .stButton button {
# # #             background-color: #4CAF50; /* Green color */
# # #             color: white;
# # #             font-weight: bold;
# # #             padding: 0.5em 1.5em;
# # #             border: none;
# # #             border-radius: 8px;
# # #         }
# # #         .stButton button:hover {
# # #             background-color: #45a049;
# # #         }
# # #         </style>
# # #     """, unsafe_allow_html=True)
# # #
# # #     # Header Image
# # #     st.image(
# # #         "https://images.pexels.com/photos/313690/pexels-photo-313690.jpeg?auto=compress&cs=tinysrgb&w=1600",
# # #         use_column_width=True,
# # #         caption="Study with confidence!"
# # #     )
# # #
# # #     # Title
# # #     st.title("Master Math and Science with StudyBot")
# # #     st.subheader("For Middle Schoolers")
# # #
# # #     # Sidebar for subject and topic selection
# # #     with st.sidebar:
# # #         st.header("Study Options")
# # #         subject = st.selectbox("Select Subject", list(st.session_state.bot.topics.keys()), key='subject_select')
# # #         topics = list(st.session_state.bot.topics[subject].keys())
# # #         topic = st.selectbox("Select Topic", topics, key='topic_select')
# # #
# # #         st.markdown("---")
# # #         st.subheader("Your Progress")
# # #         if st.session_state.total_questions > 0:
# # #             percentage = (st.session_state.score / st.session_state.total_questions) * 100
# # #             st.metric("Score", f"{st.session_state.score}/{st.session_state.total_questions}", f"{percentage:.1f}%")
# # #             st.progress(percentage / 100)
# # #         else:
# # #             st.metric("Score", "0/0")
# # #             st.progress(0)
# # #
# # #     col1, col2 = st.columns([2, 1])
# # #
# # #     with col1:
# # #         col_new_question, col_clear_question = st.columns([1, 1])
# # #         if col_new_question.button("Get New Question", type="primary", key='new_question'):
# # #             st.session_state.current_question = random.choice(st.session_state.bot.topics[subject][topic])
# # #             st.session_state.show_explanation = False
# # #             st.session_state.last_answer_correct = None
# # #
# # #         if col_clear_question.button("Clear Question", key='clear_question'):
# # #             st.session_state.current_question = None
# # #             st.session_state.show_explanation = False
# # #             st.session_state.last_answer_correct = None
# # #
# # #         if st.session_state.current_question:
# # #             st.markdown("---")
# # #             st.markdown("### Question:")
# # #             st.markdown(st.session_state.current_question['question'])
# # #             user_answer = st.text_input("Your Answer:", key="user_answer")
# # #             st.caption("Enter your answer (e.g., '9' or 'x = 9')")
# # #
# # #             if st.button("Submit Answer", key='submit_answer'):
# # #                 st.session_state.total_questions += 1
# # #                 if st.session_state.bot.check_answer(user_answer, st.session_state.current_question):
# # #                     st.session_state.score += 1
# # #                     st.session_state.last_answer_correct = True
# # #                 else:
# # #                     st.session_state.last_answer_correct = False
# # #                 st.session_state.show_explanation = True
# # #
# # #             if st.session_state.show_explanation:
# # #                 st.markdown("---")
# # #                 if st.session_state.last_answer_correct:
# # #                     st.success("✓ Correct! Great job!")
# # #                 else:
# # #                     st.error("✗ Not quite right.")
# # #                     st.info("### Explanation:\n" + st.session_state.current_question['explanation'])
# # #
# # #     with col2:
# # #         st.markdown("### Study Tips")
# # #         tips = [
# # #             "🎯 Read each question carefully and identify what's being asked",
# # #             "📝 Show your work step by step to catch mistakes",
# # #             "🤔 Look for patterns and connections to previous problems",
# # #             "✅ Always check your answer makes sense",
# # #             "💡 Learn from explanations, even when you get it right!"
# # #         ]
# # #         for tip in tips:
# # #             st.markdown(tip)
# # #
# # #
# # # if __name__ == "__main__":
# # #     main()
# # import streamlit as st
# # import random
# # from datetime import datetime
# # import re
# #
# # # Configure Streamlit with correct settings
# # st.set_page_config(
# #     page_title="StudyBot",
# #     page_icon="📚",
# #     layout="wide",
# #     initial_sidebar_state="expanded",
# #     menu_items={
# #         'Get Help': 'https://github.com/your-repo/studybot',
# #         'Report a bug': 'https://github.com/your-repo/studybot/issues',
# #         'About': 'StudyBot - A learning assistant for middle school students'
# #     }
# # )
# #
# # class StudyBot:
# #     def __init__(self):
# #         # Define topics and sample questions for a more comprehensive tutor app
# #         self.topics = {
# #             'math': {
# #                 'algebra': [
# #                     {
# #                         'question': 'Solve for x: 5x + 10 = 30',
# #                         'answer': '4',
# #                         'explanation': '1. Subtract 10 from both sides: 5x = 20\n2. Divide by 5: x = 4\nCheck: 5(4) + 10 = 20 + 10 = 30 ✓',
# #                         'accepted_answers': ['4', 'x=4', 'x = 4', '4.0']
# #                     },
# #                     {
# #                         'question': 'Solve for y: 2y - 4 = 10',
# #                         'answer': '7',
# #                         'explanation': '1. Add 4 to both sides: 2y = 14\n2. Divide by 2: y = 7\nCheck: 2(7) - 4 = 14 - 4 = 10 ✓',
# #                         'accepted_answers': ['7', 'y=7', 'y = 7', '7.0']
# #                     }
# #                 ],
# #                 'geometry': [
# #                     {
# #                         'question': 'What is the area of a triangle with base 5 cm and height 10 cm?',
# #                         'answer': '25',
# #                         'explanation': 'The area of a triangle is (1/2) * base * height = (1/2) * 5 * 10 = 25 cm²',
# #                         'accepted_answers': ['25', '25 cm²', '25 square centimeters', '25.0']
# #                     }
# #                 ]
# #             },
# #             'science': {
# #                 'physics': [
# #                     {
# #                         'question': 'What is the formula for calculating speed?',
# #                         'answer': 'distance/time',
# #                         'explanation': 'Speed is calculated by dividing distance by time (speed = distance/time).',
# #                         'accepted_answers': ['distance/time', 'distance divided by time', 'd/t']
# #                     }
# #                 ],
# #                 'biology': [
# #                     {
# #                         'question': 'What is the process by which plants make their own food?',
# #                         'answer': 'photosynthesis',
# #                         'explanation': 'Plants use sunlight, water, and carbon dioxide to create food through photosynthesis.',
# #                         'accepted_answers': ['photosynthesis']
# #                     }
# #                 ]
# #             }
# #         }
# #
# #     def check_answer(self, user_answer, question_data):
# #         """
# #         Check if the user's answer is correct with flexible matching.
# #         """
# #         # Clean up user answer
# #         cleaned_answer = user_answer.lower().strip()
# #
# #         # Remove spaces and convert to lowercase for comparison
# #         cleaned_answer = re.sub(r'\s+', '', cleaned_answer)
# #
# #         # If question has accepted_answers list, use that
# #         if 'accepted_answers' in question_data:
# #             cleaned_accepted_answers = [re.sub(r'\s+', '', ans.lower())
# #                                         for ans in question_data['accepted_answers']]
# #             return cleaned_answer in cleaned_accepted_answers
# #
# #         # Otherwise, fall back to exact match with main answer
# #         cleaned_correct = re.sub(r'\s+', '', question_data['answer'].lower())
# #         return cleaned_answer == cleaned_correct
# #
# #
# # def initialize_session_state():
# #     """Initialize session state variables with default values."""
# #     if 'bot' not in st.session_state:
# #         st.session_state['bot'] = StudyBot()
# #     if 'score' not in st.session_state:
# #         st.session_state['score'] = 0
# #     if 'total_questions' not in st.session_state:
# #         st.session_state['total_questions'] = 0
# #     if 'current_question' not in st.session_state:
# #         st.session_state['current_question'] = None
# #     if 'show_explanation' not in st.session_state:
# #         st.session_state['show_explanation'] = False
# #     if 'last_answer_correct' not in st.session_state:
# #         st.session_state['last_answer_correct'] = None
# #
# #
# # def main():
# #     # Initialize session state
# #     initialize_session_state()
# #
# #     # Header Image with expanded width
# #     st.image(
# #         "https://images.pexels.com/photos/313690/pexels-photo-313690.jpeg?auto=compress&cs=tinysrgb&w=1600",
# #         use_column_width="always",
# #         caption="Study with confidence!"
# #     )
# #
# #     # Title
# #     st.title("Master Math and Science with StudyBot")
# #     st.subheader("For Middle Schoolers")
# #
# #     # Sidebar for subject and topic selection
# #     with st.sidebar:
# #         st.header("Study Options")
# #         subject = st.selectbox(
# #             "Select Subject",
# #             list(st.session_state.bot.topics.keys()),
# #             key='subject_select'
# #         )
# #         topics = list(st.session_state.bot.topics[subject].keys())
# #         topic = st.selectbox(
# #             "Select Topic",
# #             topics,
# #             key='topic_select'
# #         )
# #
# #         # Display current score
# #         st.markdown("---")
# #         st.subheader("Your Progress")
# #         if st.session_state.total_questions > 0:
# #             percentage = (st.session_state.score / st.session_state.total_questions) * 100
# #             st.metric(
# #                 "Score",
# #                 f"{st.session_state.score}/{st.session_state.total_questions}",
# #                 f"{percentage:.1f}%"
# #             )
# #             st.progress(percentage / 100)
# #         else:
# #             st.metric("Score", "0/0")
# #             st.progress(0)
# #
# #     # Main content area
# #     col1, col2 = st.columns([2, 1])
# #
# #     with col1:
# #         # Get new question and clear buttons
# #         if st.button("Get New Question", type="primary", key='new_question'):
# #             st.session_state.current_question = random.choice(
# #                 st.session_state.bot.topics[subject][topic]
# #             )
# #             st.session_state.show_explanation = False
# #             st.session_state.last_answer_correct = None
# #
# #         if st.button("Clear Question", type="primary", key='clear_question'):
# #             st.session_state.current_question = None
# #             st.session_state.show_explanation = False
# #
# #         # Display current question
# #         if st.session_state.current_question:
# #             st.markdown("---")
# #             st.markdown("### Question:")
# #             st.markdown(st.session_state.current_question['question'])
# #
# #             # Answer input
# #             user_answer = st.text_input("Your Answer:", key="user_answer")
# #             st.caption("Enter your answer (e.g., '9' or 'x = 9')")
# #
# #             if st.button("Submit Answer", key='submit_answer'):
# #                 st.session_state.total_questions += 1
# #                 if st.session_state.bot.check_answer(
# #                         user_answer,
# #                         st.session_state.current_question
# #                 ):
# #                     st.session_state.score += 1
# #                     st.session_state.last_answer_correct = True
# #                 else:
# #                     st.session_state.last_answer_correct = False
# #                 st.session_state.show_explanation = True
# #
# #             # Show result and explanation
# #             if st.session_state.show_explanation:
# #                 st.markdown("---")
# #                 if st.session_state.last_answer_correct:
# #                     st.success("✓ Correct! Great job!")
# #                 else:
# #                     st.error("✗ Not quite right.")
# #                     st.info("### Explanation:\n" + st.session_state.current_question['explanation'])
# #
# #     with col2:
# #         # Tips and motivation
# #         st.markdown("### Study Tips")
# #         tips = [
# #             "🎯 Read each question carefully and identify what's being asked",
# #             "📝 Show your work step by step to catch mistakes",
# #             "🤔 Look for patterns and connections to previous problems",
# #             "✅ Always check your answer makes sense",
# #             "💡 Learn from explanations, even when you get it right!"
# #         ]
# #         for tip in tips:
# #             st.markdown(tip)
# #
# # if __name__ == "__main__":
# # #     main()
import streamlit as st
import random
from datetime import datetime
import re

import streamlit as st

def hide_streamlit_header_footer():
    """
    Function to hide the Streamlit header and footer in the app.
    """
    hide_st_style = """
        <style>
        /* Hide Streamlit header */
        header {visibility: hidden;}
        
        /* Hide Streamlit footer */
        footer {visibility: hidden;}
        </style>
    """
    st.markdown(hide_st_style, unsafe_allow_html=True)

# Call the function to apply the CSS
hide_streamlit_header_footer()

# Rest of your Streamlit app
st.title("My Streamlit App")
st.write("This is the main content of the app.")



# Configure Streamlit with correct settings
st.set_page_config(
    page_title="StudyBot",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/your-repo/studybot',
        'Report a bug': 'https://github.com/your-repo/studybot/issues',
        'About': 'StudyBot - A learning assistant for middle school students'
    }
)

class StudyBot:
    def __init__(self):
        # Define topics and sample questions for a more comprehensive tutor app
        self.topics = {
            'math': {
                'algebra': [
                    {
                        'question': 'Solve for x: 5x + 10 = 30',
                        'answer': '4',
                        'explanation': '1. Subtract 10 from both sides: 5x = 20\n2. Divide by 5: x = 4\nCheck: 5(4) + 10 = 20 + 10 = 30 ✓',
                        'accepted_answers': ['4', 'x=4', 'x = 4', '4.0']
                    },
                    {
                        'question': 'Solve for y: 2y - 4 = 10',
                        'answer': '7',
                        'explanation': '1. Add 4 to both sides: 2y = 14\n2. Divide by 2: y = 7\nCheck: 2(7) - 4 = 14 - 4 = 10 ✓',
                        'accepted_answers': ['7', 'y=7', 'y = 7', '7.0']
                    }
                ],
                'geometry': [
                    {
                        'question': 'What is the area of a triangle with base 5 cm and height 10 cm?',
                        'answer': '25',
                        'explanation': 'The area of a triangle is (1/2) * base * height = (1/2) * 5 * 10 = 25 cm²',
                        'accepted_answers': ['25', '25 cm²', '25 square centimeters', '25.0']
                    }
                ]
            },
            'science': {
                'physics': [
                    {
                        'question': 'What is the formula for calculating speed?',
                        'answer': 'distance/time',
                        'explanation': 'Speed is calculated by dividing distance by time (speed = distance/time).',
                        'accepted_answers': ['distance/time', 'distance divided by time', 'd/t']
                    }
                ],
                'biology': [
                    {
                        'question': 'What is the process by which plants make their own food?',
                        'answer': 'photosynthesis',
                        'explanation': 'Plants use sunlight, water, and carbon dioxide to create food through photosynthesis.',
                        'accepted_answers': ['photosynthesis']
                    }
                ]
            }
        }

    def check_answer(self, user_answer, question_data):
        """
        Check if the user's answer is correct with flexible matching.
        """
        # Clean up user answer
        cleaned_answer = user_answer.lower().strip()

        # Remove spaces and convert to lowercase for comparison
        cleaned_answer = re.sub(r'\s+', '', cleaned_answer)

        # If question has accepted_answers list, use that
        if 'accepted_answers' in question_data:
            cleaned_accepted_answers = [re.sub(r'\s+', '', ans.lower())
                                        for ans in question_data['accepted_answers']]
            return cleaned_answer in cleaned_accepted_answers

        # Otherwise, fall back to exact match with main answer
        cleaned_correct = re.sub(r'\s+', '', question_data['answer'].lower())
        return cleaned_answer == cleaned_correct


def initialize_session_state():
    """Initialize session state variables with default values."""
    if 'bot' not in st.session_state:
        st.session_state['bot'] = StudyBot()
    if 'score' not in st.session_state:
        st.session_state['score'] = 0
    if 'total_questions' not in st.session_state:
        st.session_state['total_questions'] = 0
    if 'current_question' not in st.session_state:
        st.session_state['current_question'] = None
    if 'show_explanation' not in st.session_state:
        st.session_state['show_explanation'] = False
    if 'last_answer_correct' not in st.session_state:
        st.session_state['last_answer_correct'] = None


def main():
    # Initialize session state
    initialize_session_state()

    # Header Image with expanded width
    st.image(
        "https://img.freepik.com/premium-photo/serious-young-student-woman-listening_1040878-3381.jpg?ga=GA1.1.1085812100.1727977254&semt=ais_hybrid",
        use_column_width="always",
        caption="Study with confidence!"
    )

    # Title
    st.title("Master Math and Science with StudyBot")
    st.subheader("For Middle Schoolers")

    # Sidebar for subject and topic selection
    with st.sidebar:
        st.header("Study Options")
        subject = st.selectbox(
            "Select Subject",
            list(st.session_state.bot.topics.keys()),
            key='subject_select'
        )
        topics = list(st.session_state.bot.topics[subject].keys())
        topic = st.selectbox(
            "Select Topic",
            topics,
            key='topic_select'
        )

        # Display current score
        st.markdown("---")
        st.subheader("Your Progress")
        if st.session_state.total_questions > 0:
            percentage = (st.session_state.score / st.session_state.total_questions) * 100
            st.metric(
                "Score",
                f"{st.session_state.score}/{st.session_state.total_questions}",
                f"{percentage:.1f}%"
            )
            st.progress(percentage / 100)
        else:
            st.metric("Score", "0/0")
            st.progress(0)

    # Main content area
    col1, col2 = st.columns([2, 1])

    with col1:
        # Display the question button and clear button next to each other
        button_col1, button_col2 = st.columns([1, 1])
        with button_col1:
            if st.button("Get New Question", key='new_question', help="Get a new question"):
                st.session_state.current_question = random.choice(
                    st.session_state.bot.topics[subject][topic]
                )
                st.session_state.show_explanation = False
                st.session_state.last_answer_correct = None
        with button_col2:
            if st.button("Clear Question", key='clear_question', help="Clear the current question"):
                st.session_state.current_question = None
                st.session_state.show_explanation = False

        # Display current question
        if st.session_state.current_question:
            st.markdown("---")
            st.markdown("### Question:")
            st.markdown(st.session_state.current_question['question'])

            # Answer input
            user_answer = st.text_input("Your Answer:", key="user_answer")
            st.caption("Enter your answer (e.g., '9' or 'x = 9')")

            if st.button("Submit Answer", key='submit_answer'):
                st.session_state.total_questions += 1
                if st.session_state.bot.check_answer(
                        user_answer,
                        st.session_state.current_question
                ):
                    st.session_state.score += 1
                    st.session_state.last_answer_correct = True
                else:
                    st.session_state.last_answer_correct = False
                st.session_state.show_explanation = True

            # Show result and explanation
            if st.session_state.show_explanation:
                st.markdown("---")
                if st.session_state.last_answer_correct:
                    st.success("✓ Correct! Great job!")
                else:
                    st.error("✗ Not quite right.")
                    st.info("### Explanation:\n" + st.session_state.current_question['explanation'])

    with col2:
        # Tips and motivation
        st.markdown("### Study Tips")
        tips = [
            "🎯 Read each question carefully and identify what's being asked",
            "📝 Show your work step by step to catch mistakes",
            "🤔 Look for patterns and connections to previous problems",
            "✅ Always check your answer makes sense",
            "💡 Learn from explanations, even when you get it right!"
        ]
        for tip in tips:
            st.markdown(tip)

if __name__ == "__main__":
    main()
