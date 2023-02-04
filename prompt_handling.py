# maybe this will be useful


import string

# Define a template for the running prompt
template = string.Template("""
The current time is $time.
$character1 says: "$line1".
$character2 responds: "$line2".
""")

# Define the values to insert into the template
values = {
    "time": "12:00 PM",
    "character1": "Detective",
    "line1": "What do you know about the suspect?",
    "character2": "Suspect",
    "line2": "I don't know anything. I swear."
}

# Use the template and values to generate the final prompt
prompt = template.substitute(values)

print(prompt)
