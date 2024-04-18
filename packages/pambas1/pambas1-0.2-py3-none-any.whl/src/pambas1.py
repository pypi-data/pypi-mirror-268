import pyperclip as pc
from g4f.client import Client
def g4(question) :
    client = Client()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "you are just smart scientist"},
                {"role": "user", "content": f"Answer for the following message: {question}"}
        ]
     )
    return pc.copy(response.choices[0].message.content)