from openai import OpenAI
import time

def wait_on_run(run, thread, client: OpenAI):
    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id,
        )
        time.sleep(0.5)
    return run

def generate_text_with_prompt(text, prompt, client: OpenAI):
    
    # Create an assistant for custom text analysis based on the given prompt
    assistant = client.beta.assistants.create(
        name="Custom Text Analysis Assistant",
        instructions=prompt,
        tools=[],
        model="gpt-4-1106-preview"
    )

    # Create a new thread for the interaction
    thread = client.beta.threads.create()

    # Add the text as a message to the thread
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=text
    )

    # Run the assistant to process the text
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id
    )

    # Check the run status and retrieve the response
    run = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )

    run = wait_on_run(run, thread, client)

    # Extract and return the response from the assistant
    messages = client.beta.threads.messages.list(thread_id=thread.id)
    for msg in messages.data:
        if msg.role == "assistant":
            return msg.content.get("text").get("value")

    return None