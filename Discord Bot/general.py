import random
import os
import discord
from discord.ext import commands
import requests
import asyncio

class General(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def delete(self, ctx):
        await ctx.channel.purge(limit=5)

    @commands.command(alias='deletus')
    @commands.cooldown(10, per=1)
    async def clear(ctx, amount=5):
        await ctx.channel.purge(limit=5)

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = ['It is certain.',
                     'It is decidedly so.',
                     'Without a doubt.',
                     'Yes - definitely.',
                     'You may rely on it.',
                     'As I see it, yes.',
                     'Most likely.',
                     'Outlook good.',
                     'Yes.',
                     'Signs point to yes.',
                     'Reply hazy, try again.',
                     'Ask again later.',
                     'Better not tell you now.',
                     'Cannot predict now.',
                     'Concentrate and ask again.',
                     'Dont count on it.',
                     'My reply is no.',
                     'My sources say no.',
                     'Outlook not so good.',
                     'Very doubtful.',
                     'Why do you ask me? Use your Brain and think about it!']
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

    @commands.command()
    async def okay(self, ctx):
        await ctx.send("no, that's illegal, get out of my class")
        await ctx.send("okayyy")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'pong! {round(self.bot.latency * 1000)}ms')

    @commands.command()
    async def quiz(self, ctx):
        await ctx.send("plate TECTONICS quiz AGAIN")
        await ctx.send("https://media.giphy.com/media/kyrd72DC2Iwfu/giphy.mp4")

    @commands.command()
    async def test(self, ctx):
        await ctx.send("test")

    @commands.command()
    @commands.cooldown(per=1, rate=1)
    async def tribe(self, ctx):
        await ctx.send("The tribe has spoken :clock1:  :clock1:  :clock1: :clock1: ")
        await ctx.send("*very intense watch tapping... keeps intensifying*")
        await ctx.send("https://tinyurl.com/y5cyeaql")
        await ctx.send("https://tinyurl.com/y5cyeaql")
        await ctx.send("https://tinyurl.com/y5cyeaql")
        await ctx.send("https://tinyurl.com/y5cyeaql")
        await ctx.send("https://tinyurl.com/y5cyeaql")
        await ctx.send("https://tinyurl.com/y5cyeaql")
        await ctx.send("https://tinyurl.com/y5cyeaql")
        await ctx.send("https://tinyurl.com/y5cyeaql")
        await ctx.send("https://tinyurl.com/y5cyeaql")
        await ctx.send("https://tinyurl.com/y5cyeaql")
        await ctx.send("https://tinyurl.com/y5cyeaql")
        await ctx.send("https://tinyurl.com/y5cyeaql")
        await ctx.send("https://tinyurl.com/y5cyeaql")
        await ctx.send("https://tinyurl.com/y5cyeaql")
        await ctx.send("https://tinyurl.com/y5cyeaql")
        await ctx.send("https://tinyurl.com/y5cyeaql")
        await ctx.send("https://tinyurl.com/y5cyeaql")
        await ctx.send("https://tinyurl.com/y5cyeaql")
        await ctx.send("https://tinyurl.com/y5cyeaql")

    @commands.command()
    async def SciFri_Stonks(self, ctx):
        await ctx.send("https://imgur.com/a/MsIxdIX")

    @commands.command()
    async def add(self, ctx, a: int, b: int):
        await ctx.send(a + b)

    @commands.command()
    async def multiply(self, ctx, a: int, b: int):
        await ctx.send(a * b)

    @commands.command()
    async def divide(self, ctx, a: int, b: int):
        await ctx.send(a / b)

    @commands.command()
    async def spam(self, ctx):
        await ctx.send(
            "spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam  spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam  spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam !!")
        await ctx.send("https://media.giphy.com/media/l0IylR4JqKHLjaP60/giphy.gif")
        await ctx.send(
            "spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam  spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam  spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam spam !!")
        await ctx.send("https://media.giphy.com/media/l0IylR4JqKHLjaP60/giphy.gif")

    @commands.command()
    async def greet(self, ctx):
        await ctx.send(":smiley: :wave: Hello, there! Hope you have a good time!")

    @commands.command()
    async def dog(self, ctx):
        r = requests.get('https://some-random-api.ml/facts/dog')
        await ctx.send(r.text)

    @commands.command()
    async def panda(self,ctx):
        r = requests.get('https://some-random-api.ml/img/panda')
        await ctx.send(r.content)

    @commands.command()
    async def meme(self, ctx):
        path = r"E:\the desktop\UglyBot(new)\Bad mems"
        random_filename = random.choice( [
            x for x in os.listdir( path )
            if os.path.isfile( os.path.join( path, x ) )
        ] )
        await ctx.send(random_filename)

    @commands.command()
    async def cat(self, ctx):
        await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

    @commands.command()
    async def info(self, ctx):
        embed = discord.Embed(title="uglybot", description="its the lamest bot", color=0xeee657)

        embed.add_field(name="SyncVFX", value="<#5518>")

        embed.add_field(name="Server count", value=f"{len(commands.guilds)}")

        embed.add_field(name="Invite",
                        value="[Invite link](<https://discordapp.com/api/oauth2/authorize?client_id=603773396869709861&permissions=0&scope=bot>)")

        await ctx.send(embed=embed)



    @commands.command()
    async def bal(self,ctx):
        responses = ['imagine getting banned from a one server bot lmao',
                     'Better not tell you now, or you will start crying',
                     'maybe you should of not complained about plate techtonics quiz. You lost 600k and now have -100k',
                     'CB: 500k Old CB: 900k',
                     'looks like you have 100k in your balance and 200k safe in your old CB',
                     "you were blacklisted, looks like you can't gain any k until appealing your ban with <@372189580968853504>",
                     'My sources say you lost all your k when you got an F',
                     'oof, we cannot find your k, looks like you need to gain some',
                     'Go donate to me and get some k already',
                     'You tripped on someones backpack and died, you lost all your K!:grimacing: ']
        await ctx.send('{random.choice(responses)}')

    @commands.command()
    async def yt(self, ctx):
        await ctx.send("get a shoutout")
        await ctx.send("https://www.youtube.com/channel/UC7YS_w5DP_kWcQOM6aN_7WA")
        await ctx.send("https://www.youtube.com/channel/UCkzIPO0-cy-h2Kj8gJwTbYg")
        await ctx.send("https://www.youtube.com/channel/UCPxPB7X4nzbTajB0neWXnHA?view_as=subscriber")
        await ctx.send("https://www.youtube.com/channel/UC-XcK1J6s6BiTTxUxiucPGA")
        await ctx.send("https://www.youtube.com/channel/UC_71CnqXkknzGzKXN_VO-pQ")
        await ctx.send('https://www.youtube.com/channel/UCohRg4KUFAjMSgA_gVFgOEQ')

    @commands.has_role('Weird Flex Gang')
    async def command_name(self, ctx):
        @commands.command()
        async def kick(ctx, member: discord.Member, *, reason=None):
            await member.kick(reason=reason)

    @commands.command(allias='help big bucks')
    async def helpbigbucks(self, ctx):
        embed = discord.Embed(title="bigbux commands", description="sum currency commands that might be broken lol",
                              color=0xeee657)

        embed.add_field(name='bigbucks', value='gives u 100k')
        embed.add_field(name='balance', value='check ur balance')

    @commands.command()
    async def world(self, ctx):
        embed = discord.Embed(title="Charities", description="Here are some good charities to donate to. *Note: I am "
                                                             "not affiliated in any way * ", color=0xeee657)
        embed.add_field(name='https://donate.torproject.org/', value='Take the internet back with tor! Give today, '
                                                                     'and Mozilla will match your donation. Over '
                                                                     '500000 donated so far ', inline=False)
        embed.add_field(name='https://teamtrees.org/', value='Mr.Beast\'s charity he created in celebration of 20 '
                                                             'million subscribers. Over 20m donated and counting.')
        await ctx.send(embed=embed)

    @commands.command()
    async def rte(self,ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/381963689470984203/473174040916525077/unknown.png')

    @commands.command()
    async def ddos(self, ctx):
        await ctx.send('send IP with $sendip')
        await asyncio.sleep( 10 )
        await ctx.send('hacking')

    @commands.command()
    async def infect(self,ctx):
        await ctx.send('this will get someone banned from the server, remove my perms if you do not want this to happen')

    @commands.command()
    async def sendip(self,ctx,ip):
        await ctx.send('ip received')


def setup(bot):
    bot.add_cog(General(bot))
