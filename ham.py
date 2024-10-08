import streamlit as st
import pyaudio
import wave
import os

# Function to record audio
def record_audio(filename, duration=5):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    frames = []

    st.write("Recording...")
    for i in range(0, int(RATE / CHUNK * duration)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    st.success("Recording complete!")

# Function to play audio
def play_audio(filename):
    CHUNK = 1024

    wf = wave.open(filename, 'rb')
    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(CHUNK)

    while data:
        stream.write(data)
        data = wf.readframes(CHUNK)

    stream.stop_stream()
    stream.close()
    p.terminate()

# Main app function
def main():
    st.title("Speak and Listen App")
    st.write("Connect and communicate with your friends!")

    username = st.text_input("Enter your name or callsign:")

    if username:
        st.write(f"Welcome, {username}!")

        tab1, tab2 = st.tabs(["Speak", "Listen"])

        with tab1:
            st.header("Speak")
            if st.button("Start Recording"):
                record_audio(f"{username}_audio.wav", duration=5)

        with tab2:
            st.header("Listen")
            received_files = [f for f in os.listdir() if f.endswith("_audio.wav") and not f.startswith(username)]

            if received_files:
                selected_file = st.selectbox("Select an audio file to play:", received_files)
                if st.button("Play Audio"):
                    st.audio(selected_file)
            else:
                st.write("No audio files available.")

        if st.button("Refresh"):
            st.experimental_rerun()

if __name__ == "__main__":
    main()
