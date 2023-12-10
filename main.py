import os

import discord
import requests

from const import *


def get_correct_sign(text: str, choice: str):
    choice = choice.lower()
    texts = text.split("\n \n")
    if choice in SIGNS:
        for text in texts:
            if text.startswith(SIGNS[choice]):
                return text
    return NO_SIGN


def get_goroscope(sign: str):
    try:
        response = requests.get(os.getenv("VK_URL")).json()
    except requests.RequestException:
        return VK_ERROR

    # mb add detect is a post is a goroscope?
    text = response["response"]["items"][1]["text"]
    result = get_correct_sign(text, sign)

    return result


class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if client.user.mentioned_in(message):
            print(f"User {message.author.name} texted '{message.content}'")
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
