import gspread
from oauth2client.service_account import ServiceAccountCredentials


def get_rules():
    scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

    creds = ServiceAccountCredentials.from_json_keyfile_name('chat-384709-f24e97dc0a0b.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('ЧАТ').get_worksheet(2)
    index = 0
    rules = ''
    while True:
        index += 1
        if sheet.cell(index, 2) is not None:
            if sheet.cell(index, 2).value is None:
                break
            rules += sheet.cell(index, 2).value + '\n'
    return rules