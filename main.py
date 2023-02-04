import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

# AI Chat Bot is Detective, User is Suspect

start_sequence = "\nDetective:"
restart_sequence = "\nSuspect: "

previous_response = (
    "The following is a transcript of an interview, between a police detective and the suspect"
    "of a grand theft auto investigation. The suspect does know something, but has been uncooperative. "
    "The detective is determined to get to the bottom of this and find out exactly what this suspect "
    " knows. The detective is familiar with a number of well established interrogation techniques and "
    "demonstrates them well.\n\n"
    "Suspect: I told you I don't know anything.\nDetective: Look, why don't you just let me know "
    "when you're ready to talk, OK?\n"
    "Suspect: "
)

max_prompt_length = 3000

while True:
    user_input = input("Suspect: ")
    prompt = previous_response + "Suspect: " + user_input + "\nDetective: "

    # Check if prompt length exceeds maximum allowed length
    if len(prompt) > max_prompt_length:
        # Truncate previous conversation to meet length requirement
        previous_response = previous_response[-max_prompt_length:]

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    response_text = response["choices"][0]["text"].strip()
    previous_response = prompt + response_text + "\n"
    print(f"Detective: {response_text}")
