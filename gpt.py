import openai


class Gpt:
    def __init__(self, api_key):
        openai.api_key = api_key

    def gpt_3(self, temp, prompt):
        return openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            temperature=temp,
            max_tokens=256
        ).choices[0].text