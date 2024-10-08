import streamlit as st
import requests
import pyttsx3
import tempfile
import os

# Initialize TTS engine
engine = pyttsx3.init()

# Session state to control the TTS engine
if 'engine_running' not in st.session_state:
    st.session_state.engine_running = False

# Configure the Streamlit app
st.title("Weather Radio - Active Major Weather Alerts")
st.write("Tune into live weather alerts across the U.S., including hurricanes.")

# NWS API URL for active weather alerts
nws_url = 'https://api.weather.gov/alerts/active'

# Fetch active weather alerts
response = requests.get(nws_url)
data = response.json()

# If there are active alerts, display them and read them out loud
if 'features' in data and len(data['features']) > 0:
    st.header("Active Major Weather Alerts")

    hurricane_found = False

    for alert in data['features']:
        alert_info = alert['properties']
        event = alert_info['event']
        description = alert_info['description']
        headline = alert_info['headline']

        # Focus on Hurricane-related alerts
        if "Hurricane" in event or "Tropical" in event:
            hurricane_found = True
            st.subheader(f"Alert: {event}")
            st.write(f"**Headline**: {headline}")
            st.write(f"**Description**: {description}")

            # Check if the TTS engine should be running
            if not st.session_state.engine_running:
                st.session_state.engine_running = True
                full_text = f"{event}: {headline}. {description}"

                # Use TTS to read the alert
                engine.say(full_text)
                engine.runAndWait()

                # Save the TTS audio output to a temporary file for Streamlit playback
                with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio_file:
                    temp_audio_path = temp_audio_file.name
                    engine.save_to_file(full_text, temp_audio_path)
                    engine.runAndWait()

                # Stream the audio file in the Streamlit app
                st.audio(temp_audio_path)

                # Remove the temporary file after playing
                os.remove(temp_audio_path)

    if not hurricane_found:
        st.success("No active hurricane alerts at the moment.")
else:
    st.success("No active major weather alerts at the moment.")
