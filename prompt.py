import streamlit as st
from pymongo import MongoClient
from datetime import datetime
import random
from PIL import Image
import pandas as pd
from textblob import TextBlob

# MongoDB Connection Setup
client = MongoClient(
    'mongodb+srv://doadmin:016P5a8HRn23es7h@Dolphin-439a4f33.mongo.ondigitalocean.com/admin?retryWrites=true&w=majority')
db = client["Aliyah"]
collection = db["Prompt_Power"]

# Display logo
try:
    st.image("123_1.png", width=100)
except FileNotFoundError:
    st.error("Logo not found. Please check the path.")

# Display image
image_path = "write.jpg"
try:
    image = Image.open(image_path)
    st.image(image, caption="Ten Professional Prompts", use_column_width=True)
except FileNotFoundError:
    st.error(f"Image file not found: {image_path}")
except Exception as e:
    st.error(f"Failed to load the image: {e}")

# Display custom header with Pacifico font, bold style, and centered
st.markdown(
    '<h1 style="font-family: Pacifico; font-size: 24px; font-weight: bold; text-align: center;">ENC Prompt Generator</h1>',
    unsafe_allow_html=True
)

# Function to analyze sentiment and categorize prompts
def analyze_sentiment_and_categorize(prompt):
    analysis = TextBlob(prompt)
    sentiment_score = analysis.sentiment.polarity  # Sentiment score between -1 and 1
    category = ""

    # Categorizing based on sentiment score
    if sentiment_score > 0.1:
        category = "Positive"
    elif sentiment_score < -0.1:
        category = "Negative"
    else:
        category = "Neutral"

    return category

# Function to generate varied professional prompts based on user input
def generate_professional_prompts(user_input, num_prompts=11):
    prompt_templates = [
        f"Draft a project proposal for: {user_input}. Include objectives and timelines.",
        f"Write a sales letter for: {user_input}. Persuade the reader to take action.",
        f"Outline a content strategy for: {user_input}. Focus on audience engagement.",
        f"Create a promotional email for: {user_input}. Engage your audience effectively.",
        f"Plan an event around: {user_input}. Include the agenda and key speakers.",
        f"Conduct a SWOT analysis for: {user_input}. Identify strengths, weaknesses, opportunities, and threats.",
        f"Develop a training program for: {user_input}. Outline learning objectives.",
        f"Generate a business case for: {user_input}. Justify the need for investment.",
        f"Draft a strategic marketing plan for: {user_input}. Include target market and tactics.",
        f"Create a customer journey map for: {user_input}. Visualize the user experience.",
    ]

    # Ensure we generate 11 unique prompts
    generated_prompts = random.sample(prompt_templates, min(num_prompts, len(prompt_templates)))

    return generated_prompts

# Display custom text with Georgia font and bold style
st.markdown(
    '<p style="font-family: Georgia; font-weight: bold;">'
    'Thank you for your purchase of the Prompt Generator. Enter a simple descriptive request and the generator will craft a listing of professional prompts that enhance your search.'
    '</p>',
    unsafe_allow_html=True
)

# Input for adding a new prompt
new_prompt = st.text_input("Enter your brief prompt request:")

# Initialize session state for prompts
if 'prompts' not in st.session_state:
    st.session_state.prompts = []

# Ensure the prompt is generated only once per session
if st.button("Submit"):
    if new_prompt:
        try:
            # Check for duplicates in the collection
            existing_prompt = collection.find_one({"expanded_comment": new_prompt})
            if existing_prompt:
                st.warning("This prompt already exists in the collection.")
            else:
                # Store the new prompt in MongoDB
                record = {
                    "expanded_comment": new_prompt,
                    "date": datetime.now()
                }
                collection.insert_one(record)
                st.success("New prompt added successfully!")

                # Generate varied professional prompts based on user input
                professional_prompts = generate_professional_prompts(new_prompt)

                # Store the generated prompts in MongoDB
                for prompt in professional_prompts:
                    collection.insert_one({"expanded_comment": prompt, "date": datetime.now()})

                # Store prompts in session state if not already generated
                st.session_state.prompts = professional_prompts

        except Exception as e:
            st.error(f"Failed to add new prompt: {e}")
    else:
        st.warning("Please enter a prompt before submitting.")

# Display the most recent prompts generated from the latest submission
if st.session_state.prompts:
    # Create a DataFrame without the index for display
    df = pd.DataFrame(st.session_state.prompts, columns=['Generated Prompts'])

    # Center the text in the DataFrame
    st.markdown("<style>.stDataFrame { text-align: center; }</style>", unsafe_allow_html=True)

    # Display the DataFrame as a scrollable table without the index
    st.dataframe(df.style.set_properties(**{'text-align': 'center'}), use_container_width=True, height=300)

    # Add CSV download button for generated prompts
    csv = df.to_csv(index=False)
    st.download_button(
        label="Download CSV file",
        data=csv,
        file_name="generated_prompts.csv",
        mime="text/csv"
    )
else:
    st.write("No prompts generated yet.")
