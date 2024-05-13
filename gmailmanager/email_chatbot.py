from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

# Define the scopes required for accessing Gmail API
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

# Set up authentication
flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
credentials = flow.run_local_server(port=0)

from googleapiclient.discovery import build

# Build the Gmail service
service = build('gmail', 'v1', credentials=credentials)

# Retrieve the list of email messages
results = service.users().messages().list(userId='me', labelIds=['INBOX']).execute()
messages = results.get('messages', [])

# Process the retrieved email messages
for message in messages:
    msg = service.users().messages().get(userId='me', id=message['id']).execute()
    # Perform desired actions with each email, such as organizing, categorizing, or extracting information
