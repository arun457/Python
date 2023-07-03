import requests

# Define the URL of the Microsoft Form
form_url = "https://forms.microsoft.com/r/Rs4R4pR9KZ"

# Define the data you want to submit
form_data = {
    "QuestionId_r7750d5f2273a4921a2b79ca4f20ad990": "No"  # Replace "Option 2" with the value of the radio button you want to select
}

# Send a POST request to submit the form
response = requests.post(form_url, data=form_data)

# Check the response status code to see if the form was submitted successfully
if response.status_code == 200:
    print("Form submitted successfully!")
else:
    print("Form submission failed. Status code:", response.status_code)
