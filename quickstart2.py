# import os.path
# import pickle
#
# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
# SCOPES = ["https://www.googleapis.com/auth/spreadsheets."]
#
# # The ID and range of a sample spreadsheet.
# SAMPLE_SPREADSHEET_ID = "1elrwsch2m95ygc0izoJUcjtRpedGmO2yMed_mmEAuTQ"
# SAMPLE_RANGE_NAME = "General"
#
# def main():
#   """Shows basic usage of the Sheets API.
#   Prints values from a sample spreadsheet.
#   """
#   creds = None
#   # The file token.json stores the user's access and refresh tokens, and is
#   # created automatically when the authorization flow completes for the first
#   # time.
#   if os.path.exists("token.json"):
#     creds = Credentials.from_authorized_user_file("token.json", SCOPES)
#   # If there are no (valid) credentials available, let the user log in.
#   if not creds or not creds.valid:
#     if creds and creds.expired and creds.refresh_token:
#       creds.refresh(Request())
#     else:
#       flow = InstalledAppFlow.from_client_secrets_file(
#           "credentials.json", SCOPES
#       )
#       creds = flow.run_local_server(port=0)
#     # Save the credentials for the next run
#     with open("token.json", "w") as token:
#       token.write(creds.to_json())
#
#   try:
#     service = build("sheets", "v4", credentials=creds)
#
#     # Call the Sheets API
#     sheet = service.spreadsheets()
#     result = (
#         sheet.values()
#         .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
#         .execute()
#     )
#     values = result.get("values", [])
#
#     if not values:
#       print("No data found.")
#       return
#
#     print("Name, Major:")
#     for row in values:
#       # Print columns A and E, which correspond to indices 0 and 4.
#       print(f"{row[0]}, {row[1]}")
#   except HttpError as err:
#     print(err)
#
#
# def main_Download():
#   gs = (main_Download)
#   test_range = 'General!E6:F8'
#   test_values = [
#     [16, 26],
#     [36, 46],
#     [56, 66]
#   ]
#   gs.updateRangeValues(test_range, test_values)
#
#
# if __name__ == "__main__":
#   main()


from __future__ import print_function

import os.path
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SAMPLE_RANGE_NAME = 'Test List!A2:E246'




class GoogleSheet:
  SPREADSHEET_ID = '1elrwsch2m95ygc0izoJUcjtRpedGmO2yMed_mmEAuTQ'
  SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
  service = None

  def __init__(self):
    creds = None

    if not creds or not creds.valid:
      if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
      else:
        print('flow')
        flow = InstalledAppFlow.from_client_secrets_file(
          'credentials.json', self.SCOPES)
        creds = flow.run_local_server(port=0)
      with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

    self.service = build('sheets', 'v4', credentials=creds)

  def updateRangeValues(self, range, values):
    data = [{
      'range': range,
      'values': values
    }]
    body = {
      'valueInputOption': 'USER_ENTERED',
      'data': data
    }
    result = self.service.spreadsheets().values().batchUpdate(spreadsheetId=self.SPREADSHEET_ID, body=body).execute()
    print('{0} cells updated.'.format(result.get('totalUpdatedCells')))


def main():
  gs = GoogleSheet()
  test_range = 'General!G2:H4'
  test_values = [
    [16, 26],
    [36, 46],
    [56, 66]
  ]
  gs.updateRangeValues(test_range, test_values)


if __name__ == '__main__':
  main()