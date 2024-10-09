import streamlit as st
import requests
from datetime import datetime


def get_weather_alerts():
    url = "https://api.weather.gov/alerts/active?status=actual&message_type=alert"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['features']
    else:
        return []


def main():
    st.title("US National Weather Alerts")

    # Layout with two columns: video on the left, alerts on the right
    col1, col2 = st.columns([1, 3])

    with col1:
        st.write("Watch current NOAA weather alerts:")
        video_url = "https://www.youtube.com/embed/-5z2YnhI6Ew"  # Embedded actual NOAA weather video URL
        st.video(video_url)

    with col2:
        if 'alerts' not in st.session_state:
            st.session_state.alerts = []

        if st.button("Get Latest Alerts"):  # Changed "Fetch" to "Get"
            st.session_state.alerts = get_weather_alerts()

        if st.session_state.alerts:
            for alert in st.session_state.alerts:
                properties = alert['properties']
                st.subheader(properties['event'])
                st.write(f"Affected area: {properties['areaDesc']}")
                st.write(f"Severity: {properties['severity']}")
                st.write(f"Urgency: {properties['urgency']}")
                st.write(f"Start: {datetime.fromisoformat(properties['effective']).strftime('%Y-%m-%d %H:%M:%S')}")
                st.write(f"End: {datetime.fromisoformat(properties['expires']).strftime('%Y-%m-%d %H:%M:%S')}")
                st.write(f"Description: {properties['description']}")
                st.write("---")
        else:
            st.write("No active weather alerts at the moment.")


if __name__ == "__main__":
    main()
