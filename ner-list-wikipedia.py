import re

input_file_path = "stanford-wikipedia.txt"


# Read the text from the file

with open(input_file_path, 'r', encoding='utf-8') as file:
    text = file.read()

pattern = r'\b(\w+)/(PERSON|ORGANIZATION|LOCATION)\b'

# Find all matches and capture the word part without the /PERSON, /ORGANIZATION, or /LOCATION
matches = re.findall(pattern, text)

# Extract just the word without the suffix
filtered_words = [match[0] for match in matches]

# Write the filtered words (without the suffixes) to a new file, each on a new line
with open('ner-list-wikipedia.txt', 'w') as file:
    for word in filtered_words:
        file.write(word + '\n')

print("Filtered words without tags written to 'ner-list-wikipedia.txt'")
