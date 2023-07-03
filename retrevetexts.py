def get_text_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        return text
    except IOError:
        print(f"Error: Failed to read file '{file_path}'")
        return None

# Provide the file path
file_path = 'https://arun457.github.io/Python/text.txt'

# Get the text from the file
text = get_text_from_file(file_path)

# Check if text retrieval was successful
if text is not None:
    print("Text contents:")
    print(text)
