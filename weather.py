import streamlit as st
import pyttsx3
import feedparser

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Fetch the weather alerts using a region-specific NOAA RSS feed
def get_weather_alerts():
    # Replace with a region-specific feed if necessary
    feed_url = "https://alerts.weather.gov/cap/fl.php?x=0"  # Example for Florida
    feed = feedparser.parse(feed_url)
    entries = feed.entries
    if entries:
        return entries[0].title, entries[0].summary
    else:
        return None, None

# Speak out the weather alert
def speak_alert(alert_text):
    engine.say(alert_text)
    engine.runAndWait()

# Streamlit App UI
st.title("National Weather Alerts (US)")

# Create a two-column layout: the first column will hold the button
col1, col2 = st.columns([1, 4])

# Add button in the first (left) column
with col1:
    if st.button("Speak Alert"):
        title, summary = get_weather_alerts()
        if summary:
            speak_alert(summary)

# Display the alert in the main section
title, summary = get_weather_alerts()

if title and summary:
    st.subheader(f"Alert: {title}")
    st.write(summary)
else:
    st.write("No weather alerts at the moment.")
