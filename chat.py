import openai

API_KEY = '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'
modelo = 'text-davinci-003'
pergunta = 'Gere uma mensagem com 10 palavras sobre ${}'

openai.api_key = API_KEY

responde = openai.Completion.create(
    model=modelo,
    prompt=pergunta,
    max_tokens=1
)

print(responde.choices[0]['text'])