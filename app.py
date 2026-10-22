import io
import os
import tempfile
from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="Transcripto | Speech-to-Text",
    page_icon="🎙️",
    layout="wide",
)

st.markdown("""
<style>
.main-title {font-size:2.3rem;font-weight:750;margin-bottom:.1rem}
.subtitle {color:#6b7280;margin-bottom:1.2rem}
.info-card {border:1px solid rgba(128,128,128,.25);border-radius:14px;padding:1rem}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🎙️ Transcripto</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Turn spoken English into editable text with an AI speech recognition model.</div>',
    unsafe_allow_html=True,
)

st.info(
    "Audio is transcribed using Whisper. The first run may take time because the model needs to be downloaded. "
    "This app runs locally; model download requires an internet connection the first time."
)

with st.sidebar:
    st.header("Settings")
    model_name = st.selectbox(
        "Whisper model",
        options=["tiny", "base", "small"],
        index=0,
        help="Tiny is fastest. Base/small may be more accurate but need more memory and time.",
    )
    language_option = st.selectbox(
        "Audio language",
        options=["Auto-detect", "English", "Tamil", "Hindi", "Malayalam", "Telugu", "French", "Spanish"],
        index=0,
    )
    st.divider()
    st.markdown("### Supported formats")
    st.write("WAV, MP3, M4A, MP4, MPEG, MPGA, WEBM, OGG, FLAC")
    st.caption("Large or long files can take longer to process.")
    st.markdown("### Technology")
    st.caption("Python · Streamlit · OpenAI Whisper · FFmpeg")

st.subheader("Upload an audio file")
uploaded_file = st.file_uploader(
    "Choose an audio recording",
    type=["wav", "mp3", "m4a", "mp4", "mpeg", "mpga", "webm", "ogg", "flac"],
)

st.caption("Tip: Use a clear recording with minimal background noise for better results.")

language_codes = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "Malayalam": "ml",
    "Telugu": "te",
    "French": "fr",
    "Spanish": "es",
}

@st.cache_resource(show_spinner="Loading Whisper model… this can take a while the first time.")
def load_model(name: str):
    import whisper
    return whisper.load_model(name)

if uploaded_file is not None:
    st.success(f"Selected file: {uploaded_file.name} ({uploaded_file.size / 1024:.1f} KB)")
    st.audio(uploaded_file)

    if st.button("Transcribe audio", type="primary", use_container_width=True):
        if uploaded_file.size == 0:
            st.error("The uploaded file is empty. Please choose another audio file.")
            st.stop()

        suffix = Path(uploaded_file.name).suffix or ".audio"
        temp_path = None

        try:
            with st.spinner("Preparing audio and loading the speech recognition model…"):
                with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:
                    temp_file.write(uploaded_file.getvalue())
                    temp_path = temp_file.name
                model = load_model(model_name)

            selected_language = language_codes.get(language_option)
            transcribe_options = {"fp16": False}
            if selected_language:
                transcribe_options["language"] = selected_language

            with st.spinner("Transcribing audio. Longer recordings take more time…"):
                result = model.transcribe(temp_path, **transcribe_options)

            transcript = result.get("text", "").strip()
            detected_language = result.get("language", "unknown")

            st.divider()
            st.subheader("Transcript")
            if transcript:
                st.text_area("Edit or copy the transcript", value=transcript, height=250)
                st.download_button(
                    "Download transcript (.txt)",
                    data=transcript,
                    file_name=f"{Path(uploaded_file.name).stem}_transcript.txt",
                    mime="text/plain",
                    use_container_width=True,
                )
                st.caption(f"Detected language code: {detected_language}")
                st.metric("Transcript characters", len(transcript))
                st.metric("Transcript words", len(transcript.split()))
            else:
                st.warning("No speech was detected. Try a clearer or longer recording.")

        except ImportError:
            st.error("Whisper is not installed. Run `pip install -r requirements.txt` and try again.")
        except Exception as exc:
            st.error("Transcription failed. Check that FFmpeg is installed and the audio file is valid.")
            with st.expander("Technical details"):
                st.code(str(exc))
        finally:
            if temp_path and os.path.exists(temp_path):
                os.remove(temp_path)
else:
    st.markdown(
        '<div class="info-card"><b>How to use</b><ol>'
        '<li>Upload an audio file.</li><li>Select the language or leave Auto-detect.</li>'
        '<li>Click <b>Transcribe audio</b>.</li><li>Review the transcript and download it as a text file.</li>'
        '</ol></div>',
        unsafe_allow_html=True,
    )

st.divider()
st.markdown(
    "<div style='text-align:center;color:#6b7280;font-size:.85rem;'>"
    "Transcripto · Speech-to-text educational project</div>",
    unsafe_allow_html=True,
)
