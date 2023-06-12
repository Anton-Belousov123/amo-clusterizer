import gspread
from oauth2client.service_account import ServiceAccountCredentials


def get_rules():
    scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

    creds = ServiceAccountCredentials.from_json_keyfile_name('chat-384709-f24e97dc0a0b.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('ЧАТ').get_worksheet(2)
    return sheet.cell(1, 2).value, sheet.cell(2, 2).value, sheet.cell(3, 2).value
