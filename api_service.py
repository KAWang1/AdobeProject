import openai
openai.api_key = "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"


prompt = input("What would you like a color palette for?\n")

response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Recommend a color pallet for "+prompt+". Return only hex values.",
    temperature=0.75,
    max_tokens=70,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
)


text = response['choices'][0]['text']
usage = response['usage']['total_tokens']
print(text)
print("Total_Tokens: ", usage)
