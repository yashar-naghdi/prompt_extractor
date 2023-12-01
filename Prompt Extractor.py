import os
import sys


def extract_user_prompts(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    user_prompts = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line=="User":
            i += 1
            if i < len(lines):
                user_prompts.append(lines[i].strip())
        i += 1
    return user_prompts

def save_prompts_to_file(prompts, output_filename="user_prompts.txt"):
    with open(output_filename, 'w') as file:
        for prompt in prompts:
            file.write(prompt + '\n')

def extract_user_prompts_from_directory(directory_path):
    # List all files in the given directory
    files = os.listdir(directory_path)

    # Filter out files that contain the word "conversation" in their name
    conversation_files = [f for f in files if "conversation" in f.lower()]

    for convo_file in conversation_files:
        full_path = os.path.join(directory_path, convo_file)
        user_prompts = extract_user_prompts(full_path)
        
        # Save to a new file in the same directory
        # E.g., "conversation.txt" becomes "user_prompts_conversation.txt"
        output_filename = os.path.join(directory_path, "user_prompts_" + convo_file)
        save_prompts_to_file(user_prompts, output_filename)


if __name__ == "__main__":
    # Get the current working directory
    directory_path = os.getcwd()
    extract_user_prompts_from_directory(directory_path)