import discord
from discord.ext import tasks, commands
import flask
import os

class mod( commands.Cog ):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def karma(self,ctx):
        async def on_message(message):
            guild = message.guild
            if guild:
                path = "chatlogs/{}.txt".format( guild.id )
                with open( path, 'a+' ) as f:
                    print( "{0.timestamp} : {0.author.name} : {0.content}".format( message ), file=f )
            await self.bot.process_commands( message )



def setup(bot):
    bot.add_cog( mod( bot ) )
