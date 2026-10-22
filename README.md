# Transcripto — Speech-to-Text Transcription System

Transcripto is a Python and Streamlit application that converts speech from uploaded audio files into editable text using OpenAI Whisper.

## Features

- Upload audio files and preview them in the app
- Speech-to-text transcription using Whisper
- Language auto-detection or a selection of common languages
- Choose a Whisper model (`tiny`, `base`, or `small`)
- Edit/copy the generated transcript
- Download the transcript as a `.txt` file
- No API key required
- Runs locally; the model is downloaded the first time it is used

## Technology stack

- Python
- Streamlit
- OpenAI Whisper
- FFmpeg

## Project structure

```text
Speech_to_Text_Transcription_System/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── LICENSE
├── sample_audio_notes/
│   └── README.md
└── tests/
    └── README.md
```

## Requirements

- Python 3.10–3.12 is recommended for compatibility with PyTorch and Whisper.
- FFmpeg must be installed and available on your system PATH.
- An internet connection is required for the first download of the selected Whisper model.
- The `tiny` model is recommended for initial testing. Larger models may be slower and need more RAM.

## Install FFmpeg

**Windows:** Install FFmpeg using a trusted package manager such as winget:

```powershell
winget install Gyan.FFmpeg
```

Close and reopen the terminal after installation, then check:

```powershell
ffmpeg -version
```

If `winget` is unavailable, install FFmpeg from its official download instructions and add its `bin` directory to PATH.

**macOS (Homebrew):**
```bash
brew install ffmpeg
```

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install ffmpeg
```

## Run locally

### 1. Clone the repository

Replace `YOUR-USERNAME` with your GitHub username.

```bash
git clone https://github.com/YOUR-USERNAME/Speech_to_Text_Transcription_System.git
cd Speech_to_Text_Transcription_System
```

Or download and extract the repository ZIP.

### 2. Create a virtual environment

**Windows:**
```powershell
py -3.12 -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Start the app

```bash
streamlit run app.py
```

Open the local URL Streamlit displays, usually `http://localhost:8501`.

## How to use

1. Upload an audio file in a supported format.
2. Choose a language or select Auto-detect.
3. Select a Whisper model. Start with `tiny`.
4. Click **Transcribe audio** and wait for processing.
5. Review the transcript and download it as a text file.

## GitHub upload

Create a new repository named `Speech_to_Text_Transcription_System`. If you upload through the browser, extract the ZIP and upload the files and folders inside the project directory.

Or use Git:

```bash
git init
git add .
git commit -m "Add Transcripto speech-to-text app"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/Speech_to_Text_Transcription_System.git
git push -u origin main
```

## Troubleshooting

- **`ffmpeg` not found:** install FFmpeg, add it to PATH, and restart the terminal.
- **Model download is slow:** the first run downloads model weights; use `tiny` for the smallest initial download.
- **Out of memory or slow processing:** use `tiny`, shorten the recording, or close other applications.
- **No speech detected:** try clearer audio and reduce background noise.
- **Installation errors:** use a fresh Python 3.10–3.12 virtual environment.

## Privacy note

The app processes the uploaded audio locally with the installed Whisper package. The first model download requires internet access. Avoid uploading sensitive recordings to public repositories; never commit private audio or transcripts.

## License

MIT License. See `LICENSE`.
