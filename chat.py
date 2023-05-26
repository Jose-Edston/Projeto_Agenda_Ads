import openai

# API_KEY = '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'
API_KEY = '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'
modelo = 'text-davinci-003'
pergunta = 'Gere uma mensagem com 10 palavras sobre ${}'

openai.api_key = API_KEY

# responde = openai.Completion.create(
#     model=modelo,
#     prompt=pergunta,
#     max_tokens=1
# )

# print(responde.choices[0]['text'])

#Para gerar imagem utilizando o chatGPT
response = openai.Image.create(
    prompt='Gere uma bandeira',
    size='512x512',
    n=1
)

print(response)