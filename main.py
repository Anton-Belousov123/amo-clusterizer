import time

from scripts import ggl, get_messages, gpt, create_alert, create_notification, change_status
from scripts.auth import get_token
from scripts.change_tag import get_lead_ids, change_tag
from scripts.get_messages import get_chat_history


def main():
    while True:
        try:
            # if True:
            lead_ids = get_lead_ids()

            rules, q1, q2 = ggl.get_rules()
            chats = get_messages.get_pipelines()
            print(len(chats))
            for chat_data in chats:
                chat_id, pipeline_id, stage = chat_data[0], chat_data[1], chat_data[2]
                if lead_ids[int(pipeline_id)] is False:
                    continue

                print(chat_id, pipeline_id, stage)
                # change_tag(int(pipeline_id))
                # continue  # TODO: Comment in future

                messages = get_chat_history(chat_id)
                client_id = ''
                if len(messages) > 0:
                    client_id = messages[-1]['author']['id']
                    messages = messages[:-1]
                text_length = len(rules)
                messages_amo = []

                for amo_message in messages:
                    if text_length + len(amo_message['text']) > 2500:
                        break
                    if client_id != amo_message['author']['id']:
                        continue
                    text_length += len(amo_message['text'])
                    messages_amo.append({"role": "user", "content": 'Сообщение клиента: ' + amo_message['text']})
                messages_amo.append({'role': 'system', 'content': rules})
                messages_amo.reverse()
                fl = False
                attempt = 0
                answer = ''
                while attempt < 5 and not fl:
                    attempt += 1
                    answer = gpt.get_answer([{'role': 'system', 'content': q1}] + messages_amo)
                    print([{'role': 'system', 'content': q1}] + messages_amo)
                    print(answer)
                    if 'yes' in answer.lower().strip():
                        fl = True
                        answer = 'Теплый лид'
                        break
                    if 'no' in answer.lower().strip():
                        fl = False
                        answer = 'Холодный лид'
                        break

                attempt = 0
                if answer == 'Холодный лид':
                    while attempt < 5:
                        attempt += 1
                        answer = gpt.get_answer([{'role': 'system', 'content': q2}] + messages_amo)
                        print(answer)
                        if 'yes' in answer.lower().strip():
                            fl = True
                            answer = 'Холодный лид'
                            break
                        if 'no' in answer.lower().strip():
                            fl = False
                            answer = 'Ледяной лид'
                            break

                print('new answer', answer)
                _, session = get_token()
                create_notification.start(pipeline_id, session, answer)
                change_tag(int(pipeline_id))
                if stage.lower() != answer.lower() and fl:
                    change_status.start(pipeline_id)

                print('Finished', pipeline_id)
        except Exception as e:
            time.sleep(3)
            print('Exception', e)


if __name__ == '__main__':
    main()
