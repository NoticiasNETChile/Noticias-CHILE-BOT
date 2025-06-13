import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

def connect_sheet():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)
    return client.open(os.getenv('GOOGLE_SHEET_NAME')).sheet1

def exists_in_sheet(sheet, url):
    try: sheet.find(url); return True
    except: return False

def add_entry(sheet, t, s, url, pub, status):
    sheet.append_row([t, s, url, pub, status])