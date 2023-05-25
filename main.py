import time

from scripts import ggl, get_messages, gpt, create_alert, create_notification
from scripts.auth import get_token
from scripts.change_tag import get_lead_ids, change_tag
from scripts.get_messages import get_chat_history


def main():
    while True:
        try:
            lead_ids = get_lead_ids()

            rules = ggl.get_rules()
            chats = get_messages.get_pipelines()
            for chat_data in chats:
                chat_id, pipeline_id, stage = chat_data[0], chat_data[1], chat_data[2]
                if lead_ids[int(pipeline_id)] is False:
                    continue
                messages = get_chat_history(chat_id)

                text_length = len(rules)
                messages_amo = []
                for amo_message in messages:
                    if text_length + len(amo_message['text']) > 2500:
                        break
                    text_length += len(amo_message['text'])
                    messages_amo.append({"role": "user", "content": amo_message['text']})
                messages_amo.append({'role': 'system', 'content': rules})
                messages_amo.reverse()
                answer = gpt.get_answer(messages_amo)
                _, session = get_token()
                create_notification.start(pipeline_id, session, answer)
                change_tag(int(pipeline_id))
                print('Finished', pipeline_id)
        except:
            time.time(3)
            print('Exception')

if __name__ == '__main__':
    main()
