import requests

def send_message(recipient_ids, message_text, access_token):
    api_endpoint = 'https://graph.facebook.com/v13.0/me/messages'

    for recipient_id in recipient_ids:
        payload = {
            'recipient': {
                'id': recipient_id
            },
            'message': {
                'text': message_text
            },
            'access_token': access_token
        }

        response = requests.post(api_endpoint, json=payload)
        if response.status_code == 200:
            print(f"Message sent to recipient {recipient_id}")
        else:
            print(f"Failed to send message to recipient {recipient_id}. Error: {response.text}")

# Usage example
recipient_ids = ['USER_ID_1', 'USER_ID_2', 'USER_ID_3']  # Replace with actual recipient IDs
message_text = 'Hello, this is a test message!'  # Replace with your desired message
access_token = 'YOUR_ACCESS_TOKEN'  # Replace with your Facebook Graph API access token

send_message(recipient_ids, message_text, access_token)
