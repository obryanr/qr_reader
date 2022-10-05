"""Streamlit Web Builder"""

from qr_reader import VideoProcessor
from streamlit_webrtc import webrtc_streamer
import streamlit as st


def main():
    """QR Reader Web"""
    st.header("Live stream processing")

    qr_code_reader = "QR Code Live Detector"
    app_mode = st.sidebar.selectbox( "Choose the app mode",
        [
            qr_code_reader
        ],
    )

    st.subheader(app_mode)

    if app_mode == qr_code_reader:
        webrtc_streamer(
        key="opencv-filter",
        rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
        video_processor_factory=VideoProcessor,
        async_processing=True,
    )

main()
