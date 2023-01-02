# https://developers.google.com/resources/api-libraries/documentation/tasks/v1/python/latest/tasks_v1.tasks.html
from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/tasks']


def main():
    """Shows basic usage of the Tasks API.
    Prints the title and ID of the first 10 task lists.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('tasks', 'v1', credentials=creds)

        # Call the Tasks API
        results = service.tasklists().list(maxResults=10).execute()
        tasklists = results.get('items', [])

        if not tasklists:
            print('No task lists found.')
            return

        for tasklist in tasklists:
            print(f"{tasklist['title']} - {tasklist['id']}")
            # for task in service.tasks().list(tasklist=tasklist['id']).execute().get('items', []):
            for task in service.tasks().list(tasklist=tasklist['id'], showCompleted=False).execute().get('items', []):
                print(f"  {task.get('title', '')} - {task['id']}")

        # task = service.tasks().get(tasklist="dURER2x6QzRMUUtCcDRldw", task="ejBzcGxFR0ZPalQ2ako3SA").execute()
        # task["status"] = "completed"
        # service.tasks().patch(tasklist="dURER2x6QzRMUUtCcDRldw", task="ejBzcGxFR0ZPalQ2ako3SA", body=task).execute()
        print(service.tasks().get(tasklist="dURER2x6QzRMUUtCcDRldw", task="ejBzcGxFR0ZPalQ2ako3SA").execute())
    except HttpError as err:
        print(err)


if __name__ == '__main__':
    main()
