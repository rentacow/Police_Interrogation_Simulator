# might be useful

def handle_input(user_input):
    global prompt
    if '[' in user_input and ']' in user_input:
        command = user_input[user_input.find("[") + 1: user_input.find("]")]
        if command in commands:
            handle_command(command)
        else:
            user_input = user_input.replace("[", "").replace("]", "")
    prompt += user_input
    return prompt
