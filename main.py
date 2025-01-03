import os

from groq import Groq

client = Groq(
    api_key= '',
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "who is the owner of the tesla ",
        }
    ],
    model="llama3-70b-8192",
)

print(chat_completion.choices[0].message.content)
