import requests

def get_text_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if request was not successful

        text = response.text
        return text
    except requests.exceptions.RequestException as e:
        print(f"Error: Failed to fetch text from URL '{url}': {e}")
        return None

# Provide the URL of the text file
url = 'https://arun457.github.io/Python/text.txt'

# Get the text from the URL
text = get_text_from_url(url)

# Check if text retrieval was successful
if text is not None:
    print("Text contents:")
    print(text)
