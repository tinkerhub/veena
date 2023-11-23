import os
from openai import OpenAI
from utils import (
    generate_text_with_prompt,
    load_pdf_file
)


def generate_and_save_transcript(pdf_file, prompt, client: OpenAI):
    # Load the PDF file
    document = load_pdf_file(pdf_file)

    # Generate the transcript
    transcript = generate_text_with_prompt(document, prompt, client)

    with open(os.path.join('..', 'transcripts', os.path.basename(pdf_file).replace('.pdf', '.txt')), 'w') as f:
        f.write(transcript)


def load_transcript(filename):
    # Construct the path to the transcript file
    transcript_file = os.path.join('..', 'transcripts', filename)

    # Open the transcript file in read mode
    with open(transcript_file, 'r') as file:
        # Read the contents of the file
        transcript = file.read()

    # Return the contents of the file
    return transcript