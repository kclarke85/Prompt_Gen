import os
import streamlit as st
from dotenv import load_dotenv
import dropbox

# Load environment variables
load_dotenv()

# Try to get token from multiple sources
def get_dropbox_token():
    # First try to get from Streamlit secrets
    try:
        return st.secrets["DROPBOX_TOKEN"]
    except:
        # Then try environment variable
        return os.getenv('DROPBOX_TOKEN')

# Initialize Dropbox client more safely
def init_dropbox():
    token = get_dropbox_token()
    if not token:
        st.error("Dropbox token not found. Please configure it in Streamlit secrets or environment variables.")
        st.stop()
    return dropbox.Dropbox(token)

# Use in your app
try:
    dbx = init_dropbox()
    # Your existing code here
except Exception as e:
    st.error(f"Error connecting to Dropbox: {str(e)}")
    st.stop()
