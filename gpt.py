import openai

class GPT:
    def __init__(self, api_key):
        openai.api_key = api_key

    def gpt_3(self, temp, prompt, max_tokens):
        return openai.Completion.create(
            model="text-davinci-002",
            prompt=prompt,
            temperature=temp,
            max_tokens=max_tokens,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        ).choices[0].text