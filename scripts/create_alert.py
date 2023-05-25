import requests
from scripts import auth

# Constants
status = 57562510
main_user = 9630882
pipeline_id = 6821134


def start(text):
    data = {
        'lead[NAME]': text,
        'lead[PIPELINE_ID]': pipeline_id,
        'lead[STATUS]': status,
        'lead[MAIN_USER]': main_user,
        'leadFromCont': 0,
        'PRICE': ''
    }
    _, _, session, cookies, _ = auth.get_ref_acc_tokens()
    resp = session.post('https://turkeyre.amocrm.ru/ajax/leads/detail/', headers=cookies, data=data)
