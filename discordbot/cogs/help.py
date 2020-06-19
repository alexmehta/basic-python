import discord
from discord.ext import commands


class MyCog(commands.Cog):

    # The constructor method
    def __init__(self, bot):
        self.bot = bot

    # These are the equivalent of the @bot.command() decorator
    @commands.command()
    # You must from now on pass self as an argument in all your methods(functions)
    async def hello(self, ctx):
        await ctx.send('hello!!!')

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="uglybot", description="A Very Nice bot. List of commands are:", color=0xeee657)
        embed.add_field(name="8ball", value="answers a question, do $8ball (question)", inline=False)
        embed.add_field(name="$add X Y", value="Gives the addition of **X** and **Y**", inline=False)
        embed.add_field(name="$multiply X Y", value="Gives the multiplication of **X** and **Y**", inline=False)
        embed.add_field(name="$greet", value="Gives a nice greet message", inline=False)
        embed.add_field(name="$cat", value="Gives a cute cat gif to lighten up the mood.", inline=False)
        embed.add_field(name="$info", value="Gives a little info about the bot", inline=False)
        embed.add_field(name="$help", value="Gives this message", inline=False)
        embed.add_field(name="$dog", value="Gives a nice fact", inline=False)
        embed.add_field(name="$spam", value="spams spam", inline=False)
        embed.add_field(name="$ping", value="gives u ur ping", inline=False)
        embed.add_field(name="$bigbucks", value="gives u +100k", inline=False)
        embed.add_field(name='$pandas',value='Random Panda pic')
        embed.add_field(name="$tribe", value="oh no", inline=False)
        embed.add_field(name="$okay", value="okay", inline=False)
        embed.add_field(name="$youtube", value="pls sub", inline=False)
        embed.add_field(name="$rand", value="random number", inline=False)
        embed.add_field(name="$idea(put idea in here)", value="will ping me so i can implement idea", inline=False)
        embed.add_field(name='$hello', value='will say hello back', inline=False)
        embed.add_field(name="website", value="coming soon....", inline=False)
        embed.add_field(name='$clear', value='if you give bot perms, it will delete messages for you', inline=False)
        embed.add_field(name='$yt', value='just some good channels', inline=False)
        embed.add_field(name='$world', value='places to donate to to better the world', inline=False)
        embed.add_field(name='8ball', value='its a 8ball', inline=False)
        embed.add_field(name='$AyyMD', value='flex on all those shintel haters amd for the win', inline=False)
        embed.add_field(name='$mock',value='mock img command, requires text after $mock', inline=False)
        embed.add_field(name= '$stonks',value='stonks yourself', inline=False)
        embed.add_field(name='$rte', value='only for noob coders',inline= False)
        embed.add_field(name='$modhelp', value='if your looking for something else, it is probably here', inline=False)
        embed.set_footer(text="UglyBot", icon_url='https://images-na.ssl-images-amazon.com/images/I/41yN3Kewg2L.jpg')
        await ctx.send(embed=embed)

        await ctx.send('API COMMANDS'
                       )
        await ctx.send('Joke, Panda, Dog'
                       )

    @commands.command()
    async def helpimg(self,ctx):
        embed = discord.Embed(title="IMG commands", description="Here are img commands", color=0xeee657)
        embed.add_field(name='mock',value='mocks')
        embed.set_footer(text="UglyBot", icon_url='https://images-na.ssl-images-amazon.com/images/I/41yN3Kewg2L.jpg')
        await ctx.send(embed=embed)

    # These are the equivalent of the @bot.event decorator
    @commands.Cog.listener()
    # Example of an event
    async def on_member_join(self, member):
        print(1)
    @commands.command()
    async def modhelp(self,ctx):
        embed = discord.Embed( title="uglybot", description="A Very Nice bot. List of commands are:", color=0xeee657 )
        embed.add_field( name='$nickchange', value='changes your nickname', inline=False )
        embed.set_footer( text="UglyBot", icon_url='https://images-na.ssl-images-amazon.com/images/I/41yN3Kewg2L.jpg' )
        await ctx.send( embed=embed )

# Do stuff


# Then when you finish working with your cog(class), remember to set it up
def setup(bot):
    bot.add_cog(MyCog(bot))
