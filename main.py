import os

import discord
import requests

SIGNS = [
    "Овен", "Телец", "Близнецы", "Рак", "Лев", "Дева", "Весы",
    "Скорпион", "Стрелец", "Козерог", "Водолей", "Рыбы"
]


def get_goroscope(sign: str):
    response = requests.get(os.getenv("VK_URL")).json()
    text = response["response"]["items"][1]["text"]
    texts = text.split("\n \n")
    response = []

    for text in texts:
        if sign.upper() in text.upper():
            response.append(text)
            break

    response = "\n".join(response)
    if not response:
        return "Что за знаки, что они значат?"
    return response


class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if client.user.mentioned_in(message):
            sign = message.content.split(" ")[1]
            await message.reply(get_goroscope(sign))


if __name__ == "__main__":
    intents = discord.Intents.default()
    intents.message_content = True

    client = Client(intents=intents)

    client.run(os.getenv("DISCORD_TOKEN"))
