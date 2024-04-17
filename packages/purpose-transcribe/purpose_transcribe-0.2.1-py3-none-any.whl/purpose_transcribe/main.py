# src/main.py
import click
from pathlib import Path
from .utils import  extract_zip
from .transcription import transcribe_audio_files
import tempfile

@click.command()
@click.argument('file_name')
def process_audio(file_name):
    """Processes an audio file from the current directory, transcribes it, and outputs a CSV in the same directory."""
    cwd = Path.cwd()
    zip_file = cwd / file_name

    if not zip_file.exists():
        click.echo(f"Error: File '{file_name}' not found in the current directory.")
        return

    temp_dir = tempfile.mkdtemp()
    extract_zip(zip_file, temp_dir)
    csv_path = cwd / 'transcriptions.csv'
    transcribe_audio_files(temp_dir, csv_path)

    click.echo(f"Transcription complete. CSV file is saved at {csv_path}")

if __name__ == '__main__':
    process_audio()