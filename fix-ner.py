import re

# Read the text from the file

with open("stanford-wikipedia.txt", 'r', encoding='utf-8') as file:
    text = file.read()

def fix_ner_tags(text):
    # Use regular expressions to find punctuation tagged as /PERSON, /ORGANIZATION, or /LOCATION
    fixed_text = re.sub(r'(?<![a-zA-Z])([.,()])/(PERSON|ORGANIZATION|LOCATION)(?=\s|$)', r'\1/O', text)
    return fixed_text

# Fix the NER tags for punctuation
fixed_text = fix_ner_tags(text)

# Output the result
with open("fixed-wiki.txt", "w", encoding="utf-8") as file:
    file.write(fixed_text)
