import speech_recognition as sr
import os

class AudioTranscriber:
    def __init__(self, audio_file, txt_file):
        self.audio_file = audio_file
        self.txt_file = txt_file
        self.recognizer = sr.Recognizer()

    def transcribe_audio(self):
        with sr.AudioFile(f"../data/{self.audio_file}") as source:
            audio_data = self.recognizer.record(source)
        return self.recognizer.recognize_google(audio_data, language="lt-LT")

    def save_transcription(self, text):
        with open(f"../transcriptions/{self.txt_file}", "w", encoding="utf-8") as f:
            f.write(text)
            print(f"File {self.txt_file} created successfully.")

    def process_audio(self):
        try:
            print(f"Audio {self.audio_file} in recognition process...")

            transcriptions_folder = "../transcriptions"
            if not os.path.exists(transcriptions_folder):
                os.makedirs(transcriptions_folder)
            
            text = self.transcribe_audio()
            if text:
                self.save_transcription(text)
            else:
                print("No text transcribed from audio.")
        except FileNotFoundError:
            print(f"Error: Audio file {self.audio_file} not found.")
        except sr.UnknownValueError:
            print("Error: Google Speech Recognition could not understand the audio.")
        except sr.RequestError as e:
            print(f"Error: Could not get results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")