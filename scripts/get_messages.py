from scripts.auth import get_token
import bs4
import requests


def get_pipelines():
    token, session = get_token()
    url = 'https://turkeyre.amocrm.ru/leads/pipeline/6821134/?skip_filter=Y'

    response = session.get(url, timeout=15)
    soup = bs4.BeautifulSoup(response.text, features='html.parser')
    answer = []
    for i in soup.find_all('div', {'class': 'pipeline_leads__item'}):
        try:
            stage = i.findPrevious('div', {'class': 'pipeline_status__head_title'}).get('title')
            url = f'https://turkeyre.amocrm.ru/ajax/leads/detail/{i.get("data-id")}?'
            resp = session.get(url)
            chat_id = resp.text.split('data-chat-id="')[1].split('"')[0]

            answer.append([chat_id, i.get('data-id'), stage])

        except:
            pass
    return answer


def get_chat_history(receiver_id: str):
    token, session = get_token()
    headers = {'X-Auth-Token': token}
    ttk = '01a00c20-4938-4881-b68c-8dbeb9aee5c8'
    url = f'https://amojo.amocrm.ru/messages/{ttk}/merge?stand=v15' \
          f'&offset=0&limit=100&chat_id%5B%5D={receiver_id}&get_tags=true&lang=ru'
    message_list = requests.get(url, headers=headers).json()
    return message_list['message_list']
