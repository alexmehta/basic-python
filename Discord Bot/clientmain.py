import datetime
import os
import sys
import time
import platform
import discord
from discord.ext import commands, tasks
import json

initial_extensions = ['cogs.help', 'cogs.general', 'cogs.levels', 'cogs.storage', 'cogs.flask','cogs.mod','cogs.logs']

bot = commands.Bot( command_prefix='$' )
bot.remove_command( "help" )

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension( extension )

currentDT = datetime.datetime.now()
print( str( currentDT ) )
import discord
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

@bot.event
async def on_ready():
    await bot.change_presence( activity=discord.Game( name='$help' ) )
    print( bot.latency )
    members.start()
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
    print(platform.java_ver())



online = 0
idle = 0
offline = 0


@tasks.loop( seconds=10 )
async def members():
    online = 0
    idle = 0
    offline = 0
    while not bot.is_closed():
        for server in bot.server():
            for member in server.members:
                if str( member.status ) == 'online':
                    online += 1
                elif str( member.status ) == 'idle':
                    idle += 1
                await bot.close()

                totalUsers = online + idle
                updateJson( 'app-cache/discordusers.json', totalUsers )

            def returnCount(total):
                print( 'Total is {}'.format( str( total ) ) )
                updateJson( 'app-cache/discordusers.json', total )
                return str( total )

            def updateJson(path, new_id):
                newPath = ensureAbsPath( path )
                with open( newPath, 'r' ) as f:
                    data = json.load( f )  # Load json data into the buffer

                tmp = data['users']
                data['users'] = new_id

                with open( newPath, 'w+' ) as f:
                    f.write( json.dumps( data ) )  # Write the new user count to the cache

            def ensureAbsPath(path):
                botRootDir = os.path.dirname( os.path.abspath( sys.argv[0] ) ) + '/'
                return path if os.path.isabs( path ) else botRootDir + path



bot.run( 'NjAzNzczMzk2ODY5NzA5ODYx.XhI9kg.I3ETbK2cOpOM4-Z0LgVV0irAGcM' )
