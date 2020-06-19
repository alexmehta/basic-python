import discord
from discord.ext import tasks, commands
import time
import asyncio
import datetime


class logs( commands.Cog ):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: str):
        ts = time.time()
        st = datetime.datetime.fromtimestamp( ts ).strftime('%Y-%m-%d %H:%M:%S')
        with open( "stats.txt", "a" ) as text_file:
            print( f"<{st}> {message.content}", file=text_file )


def setup(bot):
    bot.add_cog( logs( bot ) )
