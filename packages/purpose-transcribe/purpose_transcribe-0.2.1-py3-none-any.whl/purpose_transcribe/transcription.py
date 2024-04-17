# src/transcription.py
import os
import whisper
import logging
import csv

def transcribe_audio_files(dir_path, output_path):
    """Transcribes audio files found in a directory and writes outputs to a CSV file."""
    model = whisper.load_model("base")
    transcription_data = []

    for file_name in os.listdir(dir_path):
        if not file_name.lower().endswith((".mp3", ".m4a")):
            continue
        file_path = os.path.join(dir_path, file_name)
        result = model.transcribe(file_path)
        transcription_text = result['text']
        transcription_data.append({'File': file_name, 'Transcription': transcription_text})

    with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['File', 'Transcription']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(transcription_data)