import openai

def askgpt(text):
    openai.api_key = "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"
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = text,
        temparature = 0.6,
        max_tokens = 50,
    )
    return print(response.choices[0].text)

def main():
    while True:
        print('GPT: Ask me a question\n')
        myQn = input()
        askgpt(myQn)

main()
