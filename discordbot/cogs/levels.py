import asyncio
import random

import discord
import praw
from discord.ext import commands

reddit = praw.Reddit(client_id='AMh4NBVTeUUtyw',
                     client_secret='0aTuonsEI1l0fPCLt1vy',
                     user_agent='uglybot')


class Memes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rate(self, ctx):
        a = random.randrange(1, 100)

        embed = discord.Embed(title='Rate', description=a + '%')

    @commands.command()
    async def hack(self, ctx):
        msg = await ctx.send('ok hacking')
        await ctx.send(msg)
        await asyncio.sleep(2)
        await ctx.edit_message(msg, "hacking the API")
        await asyncio.sleep(2)
        await ctx.edit_message(msg, "indexing api key")
        await asyncio.sleep(2)
        await ctx.edit_message(msg, 'infecting user api')
        await asyncio.sleep(2)
        await ctx.edit_message(msg, 'USER API FOUND')
        await asyncio.sleep(2)
        await ctx.edit_message(msg, 'INJECTING')
        await asyncio.sleep(2)
        await ctx.edit_message(msg, 'done, API key injected')

    @commands.command()
    async def reddit(self, ctx):
        await ctx.send('indexing.')
        await asyncio.sleep(1)
        await ctx.send('indexing..')
        await asyncio.sleep(1)
        await ctx.send('indexing...')
        memes = random.choice(open('memes.txt').readlines())
        await ctx.send(memes)

    @commands.command()
    async def AyyMD(self, ctx):
        line = random.choice(open('WordsForGames.txt').readlines())
        await ctx.send(line)

    @commands.command()
    async def memez(self, ctx):
        memes_submissions = reddit.subreddit('memes').hot()
        post_to_pick = random.randint(1, 25)
        for i in range(1, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)
        await ctx.send(submission.url)

    @commands.command()
    async def random(self, ctx, a,*, b):
        com = random.randrange(a, b)
        await ctx.send(com)

    @commands.command()
    @commands.cooldown(per=1,rate=100)
    async def guess(self, ctx):
        a = random.randrange(1, 10)
        await ctx.send('the number is between 1-10')
        asyncio.sleep(2)
        await ctx.send('guess by doing $guess1')

        async def guess1(self, ctx, b):
            if a == b:
                await ctx.send('Correct')
            if a > b:
                await ctx.send('your # is too small, try again next time')
            if a < b:
                await ctx.send('your # is too big')

    @commands.command()
    async def warn(self, ctx, *,member):
        member.send(f"you have been warned, you are breaking the rules, be careful")




def setup(bot):
    bot.add_cog(Memes(bot))
