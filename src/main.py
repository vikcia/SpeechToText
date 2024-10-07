from transcribe import AudioTranscriber
from summarize import TextSummarizer

def main():
    audio_file = "daunysIrLasisa3.wav"
    transcription_txt = "transcription.txt"
    summary_txt = "summary.txt"

    transcriber = AudioTranscriber(audio_file, transcription_txt)
    transcriber.process_audio()

    summarizer = TextSummarizer()
    summarizer.process_text(transcription_txt, summary_txt)

if __name__ == "__main__":
    main()