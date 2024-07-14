from twitchio.channel import Channel
from twitchio.ext import commands, pubsub
import os
from twitchio.user import User
import secret
import asyncio # `await asyncio.sleep(s: int)` lets other parts of the bot continue running while sleeping (better than time.sleep)
import game
import threading
import voice

with open("input.txt", "w") as f:
    f.write("")

with open("mic_volume.txt", "w") as f:
    f.write("0")

# ===== Bot Config =====
class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            token=secret.get_twitch_oauth_token(),
            client_id=secret.get_client_id(),
            nick='YOUR TWITCH USERNAME (i.e. thevaloix)',
            prefix='!',
            initial_channels=['THE CHANNEL TO LISTEN TO (where the bot can send messages)'],
        )

    async def event_ready(self):
        print(f"Logged in as {self.nick}")
        print(f"User ID: {self.user_id}")

    async def event_message(self, message):
        if message.echo:
            return
        print(f"{message.author.name}: {message.content}")
        #Since commands wont run because it gets overridden by the event_message, we need to tell the bot  to handle the commands.
        await self.handle_commands(message)

    # ===== Bot Commands =====
    @commands.command()
    # A test command just to make sure it works
    async def hello(self, message: commands.Context):
        await message.channel.send(f"Hello {message.author.name}!")
    
    @commands.command()
    # Rotates the thing
    async def rotate(self, message: commands.Context):
        command: str = message.message.content
        with open("input.txt", "w") as f:
            f.write("rotate")
        await asyncio.sleep(0.1)
        with open("input.txt", "w") as f:
            f.write("")
    
    @commands.command()
    # Shrink the Player
    async def shrink(self, message: commands.Context):
        command: str = message.message.content
        with open("input.txt", "w") as f:
            f.write("shrink")
        await asyncio.sleep(0.1)
        with open("input.txt", "w") as f:
            f.write("")


twitch_bot = Bot()
if __name__ == "__main__":
    game_thread = threading.Thread(target=game.run_game)
    game_thread.start()
    voice_thread = threading.Thread(target=voice.start_voice_client)
    voice_thread.start()
    twitch_bot.run()
