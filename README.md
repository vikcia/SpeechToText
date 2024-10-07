# Audio Transcription and Summarization using Python and LLM

## Overview
This project transcribes an audio recording of a news article and generates a summary using Python. I recorded myself reading an article, then used a SpeechRecognition library to convert the audio into text. Afterward, I implemented a Large Language Model (LLM) to summarize the transcribed text. The project includes a virtual environment and necessary dependencies listed in `requirements.txt`.

Article: https://www.tv3.lt/naujiena/zmones/petras-daunys-priciuptas-parduotuveje-bande-issinesti-lasisa-n1364711

## Running
- Run Bach file `run_app` inside SpeechToText folder.
- Or open the application using the Visual Studio Code or another editor:
   - install requirements.txt `pip install -r requirements.txt`
   - and run `main.py`
  
## Usage
1. **Start the Application:**
   - Launch the application by running Bach file `run_app` or `main.py` either through the terminal or an editor like Visual Studio Code.
2. **Transcription Process:**
   - The script transcribe.py will automatically read the audio file located in the data folder. The audio file is dynamically set in `main.py` with the following line: `audio_file = "data/daunysIrLasisa3.wav"`
   - If everything runs smoothly, `transcribe.py` will create a file named `transcription.txt` inside the transcriptions folder. This file contains the recognized speech converted into text.
3. **Summarization Process:**
   - Once `transcription.txt` is successfully created, the `summarize.py` script will be triggered to generate a summary.
   - The summary will be created from `transcription.txt` and saved as `summary.txt` in the summaries folder.
