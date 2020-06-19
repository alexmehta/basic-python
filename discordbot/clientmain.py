import datetime
import os
import sys
import time
import platform
import discord
from discord.ext import commands, tasks
import json

initial_extensions = ['cogs.help', 'cogs.general', 'cogs.levels', 'cogs.storage', 'cogs.flask', 'cogs.mod', 'cogs.logs']

bot = commands.Bot( command_prefix='$' )
bot.remove_command( "help" )

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension( extension )

currentDT = datetime.datetime.now()
print( str( currentDT ) )
import discord
import logging

logger = logging.getLogger( 'discord' )
logger.setLevel( logging.DEBUG )
handler = logging.FileHandler( filename='discord.log', encoding='utf-8', mode='w' )
handler.setFormatter( logging.Formatter( '%(asctime)s:%(levelname)s:%(name)s: %(message)s' ) )
logger.addHandler( handler )


@bot.event
async def on_ready():
    await bot.change_presence( activity=discord.Game( name='$help' ) )
    print( bot.latency )
    print( 'Logged in as' )
    print( bot.user.name )
    print( bot.user.id )
    print( '------' )
    print( bot.user.avatar_url )
    print( bot.user.relationships )
    print( bot.user.email )
    print( bot.user.locale )
    print( time )
    print( currentDT )
    print( commands )
    print( "BOT IS NOW RUNNING ON " + sys.version )
    print( os.name )
    print( "===========================================" )
    print( platform.machine() )
    print( platform.version() )
    print( platform.processor() )
    print( platform.uname() )
    print( platform.java_ver() )




bot.run( 'NjAzNzczMzk2ODY5NzA5ODYx.Xm-uFA.dACE8k9PHcvcFKNuT9GZYZCuEh0' )
