import time

import openai
import os


def get_answer(messages: list):
    try:
        openai.api_key = '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'
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        if response['choices'][0]['message']['content'].count('?') > 1:
            return get_answer(messages)
        return response['choices'][0]['message']['content']

    except Exception as e:
        print('Ошибка', e)
        return get_answer(messages)
