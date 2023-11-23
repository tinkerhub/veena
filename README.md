# V.E.E.N.A (IN PROGRESS)
Virtual Event Engagement and Networking Anchor


## What is this ?

An AI anchor for hosting events using openai's assistant API, whisper and TTS APIs

## Workflow

```
User: We are going to do a generative AI conference on 25th Novemeber at Tinkerspace!
Assistant: Awesome :) I am thrilled to host the event. Do you have more details ?
User: yes. Let me upload the event plan document with speakers list and all
<Uploading document>
Assistant: Okay got it
<Assistant generating script for hosting the event using RAG>
Assistant: Here is my script for hosting the event. Go through it and feel free to suggest changes
<Display script>
User: This looks good
Assistant: Let me know when you want me to start hosting the event. 
User: Lets start now!
Assistant: Ladies and gents welcome to TInkerhub AI conference 2023, today is all about generative AI...
<Assistant calling first speaker and enable listen mode using whisper>
<On detect speaker stopped summerize speaker content>
Assistant : Thank you <speaker> your thoughts on <summarized> was spot on!
<Assistant calling next speaker and activate listen mode>
...
```

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/tinkerhub/veena.git
    ```
2. Navigate to the project directory:
    ```
    cd veena
    ```
3. Install the required packages:
    ```
    pip install -r requirements.txt
    ```
4. Create a `.env` file in the `ops` directory and add your OpenAI API key:
    ```
    OPENAI_API_KEY=yourapikey
    ```


## Usage

To generate and save a transcript, run the following command:

```bash
python main.py generate yourpdffile
```


To start an event, run the following command:

```bash
python main.py start yourpdffile
```

Replace `yourpdffile` with the filename of PDF in `/pdfs` directory. This pdf should contain event details and speaker details.