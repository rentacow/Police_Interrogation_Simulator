# almost certainly wont work, but a game state tracking implementation more or less
# also will need a check that the player didn't type the keyword, or something

import openai

def level_up(completion):
    # Define the keyword that indicates the player has leveled up
    keyword = "level up"

    # Check if the keyword appears in the completion
    if keyword in completion:
        # Split the completion into words
        words = completion.split()

        # Check if the keyword was not in the completion request
        request = openai.Completion.request
        if keyword not in request.split():
            # If the keyword was not in the request, the player has leveled up
            print("Level up!")
        else:
            print("Keyword was in the request, no level up.")
    else:
        print("Keyword not found, no level up.")

# Example usage
completion = openai.Completion.create(
    engine="text-davinci-002",
    prompt="How can I reach the next level in my game?",
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

level_up(completion.choices[0].text)
