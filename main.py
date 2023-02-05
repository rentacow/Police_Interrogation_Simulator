import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

# AI Chat Bot is Detective, User is Suspect

#   NOT IMPLEMENTED YET   #
# Level 1: easy (level up w/ free to go)
# level 2: hard (this version, level up w/ we're done OR lawyer arrives to dodge poly)
# level 3: polygraph examination (lol)
# level 4: bonus round. hearing w/ judge for dodging poly
# level 5: trial? lots of prompts needed for this... could get ugly
# level 6: in prison, chatting with your cellmate for the rest of your life

start_sequence = "\nDetective: "
restart_sequence = "\nSuspect: "

previous_response = (
    "The following is a transcript of an interview, between a police detective and the main suspect"
    "of a very serious investigation. The suspect does know something, but has been denying it. "
    "The detective is determined to get to the bottom of this and find out exactly what this suspect "
    " knows. The detective, may have a bit of a wild imagination. The detective is familiar with a "
    "number of well established interrogation techniques and "
    "demonstrates them well. The detective does have evidence, directly linking this suspect to the crime scene "
    "therefor the suspect is not free to go.\n\n"
    "Suspect: Wasn't me, must have been someone else.\nDetective: Look, why don't you let me know "
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
        temperature=0.9,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    response_text = response["choices"][0]["text"].strip()
    previous_response = prompt + response_text + "\n"
    print(f"Detective: {response_text}")
