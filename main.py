import os

import discord
import requests
from const import *


def get_goroscope(sign: str):
    try:
        response = requests.get(os.getenv("VK_URL")).json()
    except requests.RequestException:
        return VK_ERROR

    text = response["response"]["items"][1]["text"]
    texts = text.split("\n \n")
    response = []

    for text in texts:
        current_sign = text.split(": ")[0]
        if sign.upper() in current_sign.upper():
            response.append(text)
            break

    response = "\n".join(response)
    if not response:
        return NO_SIGN
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
            print(f"User {message.author.id} texted {message.content}")
            sign = message.content.split(" ")
            if len(sign) >= 2:
                await message.reply(get_goroscope(sign[1]))
            else:
                await message.reply(WRONG_MESSAGE)


if __name__ == "__main__":
    intents = discord.Intents.default()
    intents.message_content = True

    client = Client(intents=intents)

    client.run(os.getenv("DISCORD_TOKEN"))
