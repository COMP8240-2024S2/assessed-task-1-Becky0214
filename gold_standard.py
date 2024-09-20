import re

def create_gold_standard_auto(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    gold_standard = []
    
    for line in lines:
        cleaned_line = re.sub(r'[^\w\s/]', '', line)

        tokens = cleaned_line.split()
        for token in tokens:
            if '/' in token:
                parts = token.rsplit('/', 1)
                if len(parts) == 2:
                    word, label = parts  
                    if word.strip():
                        gold_standard.append(f"{word}\t{label}\n")
            else:
                if token.strip():
                    gold_standard.append(f"{token}\tO\n")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(gold_standard)
    
    print(f"Gold standard saved to {output_file}")

create_gold_standard_auto("stanford-fanwiki.txt", "fanwiki-gold.txt")

