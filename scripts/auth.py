import time

import requests


def get_ref_acc_tokens():
    session = requests.Session()
    response = session.get('https://turkeyre.amocrm.ru/')
    session_id = response.cookies.get('session_id')
    csrf_token = response.cookies.get('csrf_token')
    headers = {
        'Accept': 'application/json',
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie': f'session_id={session_id}; '
                  f'csrf_token={csrf_token};'
                  f'last_login=od.pashchenko@gmail.com',
        'Host': 'turkeyre.amocrm.ru',
        'Origin': 'https://turkeyre.amocrm.ru',
        'Referer': 'https://turkeyre.amocrm.ru/leads/pipeline/6821134/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
    }
    payload = {
        'csrf_token': csrf_token,
        'password': "test2023",
        'temporary_auth': "N",
        'username': "od.pashchenko@gmail.com"}
    response = session.post('https://turkeyre.amocrm.ru/oauth2/authorize', headers=headers, data=payload)
    access_token = response.cookies.get('access_token')
    refresh_token = response.cookies.get('refresh_token')
    headers['access_token'] = access_token
    headers['refresh_token'] = refresh_token
    return access_token, refresh_token, session, response.cookies, headers


def get_token():
    _, _, s, _, h = get_ref_acc_tokens()
    payload = {'request[chats][session][action]': 'create'}
    response = s.post('https://turkeyre.amocrm.ru/ajax/v1/chats/session', headers=h, data=payload)
    return response.json()['response']['chats']['session']['access_token'], s
