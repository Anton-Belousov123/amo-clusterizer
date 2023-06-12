import requests

from scripts import auth
from scripts.auth import get_token, get_ref_acc_tokens


def start(pipka):
    url = 'https://turkeyre.amocrm.ru/ajax/leads/multiple/change_status/'
    data = {
        'parties[id][]': int(pipka),
        'close_tasks': 0,
        'STATUS_ID': 57562510,
        'PIPELINE_ID': 6821134,
        'LOSS_REASON_ID': 0
    }
    access_token, refresh_token, session, cookies, headers = get_ref_acc_tokens()
    response = session.post(url, data=data, headers=headers)
    print(response.text)

