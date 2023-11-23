import argparse
import ai
import os
import audio
import dotenv
from openai import OpenAI

dotenv.load_dotenv("ops/.env")

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def main():
    parser = argparse.ArgumentParser(description='AI Event Host')
    parser.add_argument('command', help='Command to execute')
    parser.add_argument('pdf_file', help='PDF file with speaker details')
    args = parser.parse_args()

    if args.command == 'generate':
        ai.generate_and_save_transcript(args.pdf_file, client)
    elif args.command == 'start':
        transcript = ai.load_transcript(args.pdf_file)
        for dialogue in transcript.split('\n\n'):
            audio.speak(dialogue, client)
            speech = audio.record_speech()
            text = audio.speech_to_text(speech, client)
            thank_you_message = ai.generate_thank_you_message(text, client)
            audio.speak(thank_you_message, client)

if __name__ == '__main__':
    main()