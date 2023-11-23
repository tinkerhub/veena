import os
from openai import OpenAI
from utils import (
    generate_text_with_prompt,
    load_pdf_file
)


def generate_transcript(document, client: OpenAI):
    prompt = "Generate a full transcript for an event. \
        The transcript should start with a greeting and welcome to the event message. \
            Then, introduce each speaker and invite them to the stage. \
                Write each speaker welcome as separate paragraph. \
                    The speaker details are as follows:\n\n"

    transcript = generate_text_with_prompt(document, prompt, client)
    return transcript


def generate_and_save_transcript(pdf_file, client: OpenAI):
    # Load the PDF file
    document = load_pdf_file(pdf_file)

    # Generate the transcript
    transcript = generate_transcript(document, client)

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


def generate_thank_you_message(speech, client: OpenAI):
    prompt = "Generate a thank you message quoting the speaker's speech given below:\n\n"
    return generate_text_with_prompt(speech, prompt, client)
