import os
import re

def clean_vtt_content(content):
    # Remove timestamps and metadata
    cleaned_lines = []
    for line in content:
        # Skip lines with timestamps
        if re.match(r'^\d{2}:\d{2}:\d{2}\.\d{3}', line):
            continue
        # Skip lines with metadata (UUIDs)
        if re.match(r'^[0-9a-fA-F-]{36}', line):
            continue
        cleaned_lines.append(line.strip())
    return cleaned_lines

def remove_unnecessary_spaces(lines):
    # Join lines into a single string and remove unnecessary spaces
    text = " ".join(lines)
    # Remove multiple spaces
    text = re.sub(r'\s+', ' ', text)
    return text

def process_vtt_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".vtt"):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.readlines()
            
            cleaned_lines = clean_vtt_content(content)
            cleaned_content = remove_unnecessary_spaces(cleaned_lines)
            
            new_filename = filename.replace(".vtt", ".txt")
            new_file_path = os.path.join(directory, new_filename)
            
            with open(new_file_path, 'w', encoding='utf-8') as new_file:
                new_file.write(cleaned_content)

if __name__ == "__main__":
    directory = "."  # Set your directory path here
    process_vtt_files(directory)
