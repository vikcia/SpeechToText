from deep_translator import GoogleTranslator
from transformers import pipeline
import os

class TextSummarizer:
    def __init__(self, source_lang="lt", target_lang="en", model="facebook/bart-large-cnn"):
        self.source_lang = source_lang
        self.target_lang = target_lang
        self.summarizer = pipeline("summarization", model=model, clean_up_tokenization_spaces=True)

    def translate(self, text, source_lang=None, target_lang=None):
        source = source_lang if source_lang else self.source_lang
        target = target_lang if target_lang else self.target_lang
        return GoogleTranslator(source=source, target=target).translate(text)

    def summarize(self, text):
        summary = self.summarizer(text, max_length=130, min_length=30, do_sample=False)
        return summary[0]['summary_text']

    def process_text(self, transcription_txt, summary_txt):
        try:
            print(f"File {transcription_txt} summarizing...")

            summaries_folder = "../summaries"
            if not os.path.exists(summaries_folder):
                os.makedirs(summaries_folder)
            
            with open(f"../transcriptions/{transcription_txt}", "r", encoding="utf-8") as source:
                text = source.read().strip()

            translated_text = self.translate(text)
            summary = self.summarize(translated_text)
            translated_summary = self.translate(summary, source_lang=self.target_lang, target_lang=self.source_lang)

            with open(f"../summaries/{summary_txt}", "w", encoding="utf-8") as output_file:
                output_file.write(translated_summary)
                print(f"File {summary_txt} created successfully.")

        except FileNotFoundError as NotFound:
            print(f"File not found: {NotFound}")        

        except Exception as e:
            print(f"An error occurred: {e}")