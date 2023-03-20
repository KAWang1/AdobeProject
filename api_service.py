import ast
import os
import openai
from visual import display_color_palette


def get_palette(prompt, number):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Recommend a color pallet with "+number+" colors for "+prompt+". Return only hex values in the from of an string array.",
        temperature=0.75,
        max_tokens=70,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    text = response['choices'][0]['text']
    usage = response['usage']['total_tokens']
    text_list = ast.literal_eval(text)
    print(text)
    print("Total_Tokens: ", usage)
    display_color_palette(text_list)
