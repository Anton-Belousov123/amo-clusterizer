import time

import openai
import os


def get_answer(messages: list):
    try:
    #if True:
        openai.api_key = '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'
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0
        )
        print(response)
        if response['choices'][0]['message']['content'].count('?') > 1:
            return get_answer(messages)
        return response['choices'][0]['message']['content']

    except Exception as e:
        print('Ошибка', e)
        return get_answer(messages)
