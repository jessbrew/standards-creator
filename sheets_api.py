import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def get_student_standards(spreadsheet_id):
  creds = None
  sheet_scopes = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
  # token.json stores the user's access and refresh tokens, and is created
  # automatically when the authorization flow completes for the first time
  if os.path.exists("sheets_token.json"):
    creds = Credentials.from_authorized_user_file("sheets_token.json", sheet_scopes)
  # if there are no (valid) credentials, let user log in
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", scopes=sheet_scopes
      )
      creds = flow.run_local_server(port=0)
    # save credentials for next run
    with open("sheets_token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("sheets", "v4", credentials=creds)

    # call Sheets API
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=spreadsheet_id, range="A2:Z")
        .execute()
    )
    values = result.get("values", [])

    # check if data was found
    if not values:
      print("No data found")
      return
    # put answers into dictionary, return that
    answers = {}
    for row in values:
      answers.update({row[1]: row[2]}) # name : standards
    return answers

  except HttpError as err:
    print(err)



student_standards = get_student_standards("1EmozOHR-QQGPJ6bn7PnuTBzbWDqNUDW_KA9hFfXAwcE")
