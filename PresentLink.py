import streamlit as st
import requests
from moviepy.editor import *
from gtts import gTTS
import math
import os
import tempfile


def create_video(video_url, presentation_text, voice_gender, voice_tone, progress_bar):
    try:
        # Create temporary directory for working files
        with tempfile.TemporaryDirectory() as temp_dir:
            # Step 1: Download the video
            local_video_path = os.path.join(temp_dir, "downloaded_video.mp4")
            progress_bar.progress(0.1)
            st.text("Downloading video...")

            response = requests.get(video_url, stream=True)
            if response.status_code == 200:
                with open(local_video_path, 'wb') as file:
                    for chunk in response.iter_content(chunk_size=1024):
                        file.write(chunk)
            else:
                st.error(f"Failed to download video. Status code: {response.status_code}")
                return None

            progress_bar.progress(0.3)
            st.text("Generating voiceover...")

            # Step 2: Generate voiceover with gTTS
            voiceover_path = os.path.join(temp_dir, "voiceover.mp3")

            # Map voice gender to different English accents
            tld_mapping = {
                "Male": {
                    "Professional": "com",  # US English
                    "Casual": "ca",  # Canadian English
                    "Energetic": "com.au"  # Australian English
                },
                "Female": {
                    "Professional": "co.uk",  # British English
                    "Casual": "ie",  # Irish English
                    "Energetic": "co.in"  # Indian English
                }
            }

            # Get the appropriate TLD for the voice combination
            tld = tld_mapping[voice_gender][voice_tone]

            # Create TTS with selected voice options
            tts = gTTS(text=presentation_text, lang='en', tld=tld)
            tts.save(voiceover_path)

            progress_bar.progress(0.5)
            st.text("Processing video...")

            # Step 3: Load video and audio
            video = VideoFileClip(local_video_path)
            audio = AudioFileClip(voiceover_path)

            # Step 4: Handle video duration
            if audio.duration > video.duration:
                loop_count = math.ceil(audio.duration / video.duration)
                extended_video = concatenate_videoclips([video] * loop_count)
            else:
                extended_video = video

            progress_bar.progress(0.7)
            st.text("Combining audio and video...")

            # Step 5: Create final video
            final_video = extended_video.subclip(0, audio.duration).set_audio(audio)

            # Step 6: Save final video
            output_path = os.path.join(temp_dir, "final_presentation.mp4")
            final_video.write_videofile(
                output_path,
                codec='libx264',
                audio_codec='aac',
                temp_audiofile=os.path.join(temp_dir, "temp-audio.m4a"),
                remove_temp=True,
                fps=24
            )

            progress_bar.progress(1.0)
            st.text("Video creation complete!")

            # Read the final video file
            with open(output_path, 'rb') as file:
                video_bytes = file.read()

            return video_bytes
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None


def main():
    st.set_page_config(page_title="PresentLink", page_icon="🎥")

    # Header
    st.title("🎥 PresentLink")
    st.markdown("""
    Transform your media into engaging presentation videos instantly!
    """)

    # Input form
    with st.form("video_form"):
        # Video URL input
        video_url = st.text_input(
            "Enter video URL",
            placeholder="https://example.com/video.mp4",
            help="Enter the URL of the background video you want to use"
        )

        # Text input
        presentation_text = st.text_area(
            "Enter your presentation text",
            placeholder="Enter the text for your presentation...",
            help="This text will be converted to voiceover",
            height=200
        )

        # Voice customization options
        col1, col2 = st.columns(2)

        with col1:
            voice_gender = st.selectbox(
                "Select Voice Gender",
                options=["Male", "Female"],
                help="Choose the gender of the voiceover (approximated using different accents)"
            )

        with col2:
            voice_tone = st.selectbox(
                "Select Voice Tone",
                options=["Professional", "Casual", "Energetic"],
                help="Choose the tone of the voiceover (achieved through different regional accents)"
            )

        # Information about voice options
        st.info("""
        Voice Options:
        - Male Professional: US English
        - Male Casual: Canadian English
        - Male Energetic: Australian English
        - Female Professional: British English
        - Female Casual: Irish English
        - Female Energetic: Indian English
        """)

        # Submit button
        submitted = st.form_submit_button("Create Video")

    if submitted:
        if not video_url or not presentation_text:
            st.warning("Please provide both a video URL and presentation text.")
            return

        # Create progress bar
        progress_bar = st.progress(0)

        # Create video
        video_bytes = create_video(
            video_url,
            presentation_text,
            voice_gender,
            voice_tone,
            progress_bar
        )

        if video_bytes:
            # Display success message
            st.success("🎉 Your video has been created successfully!")

            # Display video
            st.video(video_bytes)

            # Download button
            st.download_button(
                label="Download Video",
                data=video_bytes,
                file_name="presentlink_video.mp4",
                mime="video/mp4"
            )


if __name__ == "__main__":
    main()