import openai
import time
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]
assistant_id = st.secrets["ASSISTANT_ID"]

def create_thread():
    thread = openai.beta.threads.create()
    return thread.id

def send_message(thread_id, content):
    openai.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=content
    )

def run_assistant(thread_id):
    run = openai.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id
    )
    return run.id


def get_response(thread_id, run_id):
    while True:
        run = openai.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)
        if run.status == "completed":
            messages = openai.beta.threads.messages.list(thread_id=thread_id)
            return messages.data[0].content[0].text.value
        elif run.status == "failed":
            return "❌ Error al ejecutar el asistente."
        time.sleep(1)


