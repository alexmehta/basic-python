import time
import asyncio
import urllib
import http
import io
import requests
from discord.ext import commands, tasks
import discord
import random
import csv
import pandas as pd
import asyncio
import cats
import os
import hashlib
from PIL import Image
import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import discord
import praw
import random
import urllib.request as req
import os
from googletrans import Translator


class Jokes( commands.Cog ):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def joke(self, ctx):
        with open( r'E:\the desktop\UglyBot(new)\databases\jokes.csv' ) as f:
            reader = csv.reader( f )
            for index, row in enumerate( reader ):
                if index == 0:
                    chosen_row = row
                else:
                    r = random.randint( 0, index )
                    if r == 0:
                        chosen_row = row
        await ctx.send( chosen_row )

    @commands.command()
    async def mock(self, ctx, *, a):
        await ctx.channel.trigger_typing()
        img = Image.open( r'F:\the desktop\UglyBot(new)\Mocking-Spongebob.jpg' )
        draw = ImageDraw.Draw( img )
        font = ImageFont.truetype( "impact.ttf", 100, )
        draw.text( (300, 388), a, (0, 255, 255), font=font, align="right", )
        img.save( 'mucking-Spongebob.jpg' )
        await ctx.send( a )
        await ctx.send( file=discord.File( 'mucking-Spongebob.jpg' ) )

    @commands.command()
    async def stonks(self, ctx):
        await ctx.channel.trigger_typing()
        avatar_url = str( ctx.author.avatar_url_as( format="png", size=256 ) )
        print( str( ctx.author.avatar_url_as( format="png", size=256 ) ) )
        connection = http.client.HTTPSConnection( "cdn.discordapp.com" )
        connection.request( "GET", avatar_url )
        avatar = Image.open( io.BytesIO( connection.getresponse().read() ) )
        avatar.save( "avatar.png" )
        im1 = Image.open( r'E:\the desktop\UglyBot(new)\2f0.png' )
        im2 = Image.open( 'avatar.png' )
        im1.paste( im2 )
        im1.save( r'E:\the desktop\UglyBot(new)\databases\2f00.png', quality=95 )
        await ctx.send( file=discord.File( r'E:\the desktop\UglyBot(new)\databases\2f00.png' ) )

    @commands.command()
    async def home(self, ctx):
        await ctx.channel.trigger_typing()
        avatar_url = str( ctx.author.avatar_url_as( format='png', size=256 ) )
        print( str( ctx.author.avatar_url_as( format="png", size=256 ) ) )
        connection = http.client.HTTPSConnection( "cdn.discordapp.com" )
        connection.request( "GET", avatar_url )
        avatar = Image.open( io.BytesIO( connection.getresponse().read() ) )
        avatar.save( r'E:\the desktop\UglyBot(new)\databases\athome.png' )
        im1 = Image.open( r'E:\the desktop\UglyBot(new)\databases\athometep.jpg' )
        im2 = Image.open( r'E:\the desktop\UglyBot(new)\databases\athome.png' )

    @commands.command()
    async def translate(self, ctx, a):
        await ctx.channel.trigger_typing()
        trans = Translator()
        t = trans.translate(
           a
        )

        await ctx.send( f'{t.origin} -> {t.text}' )

    @commands.command()
    async def minecraft(self, ctx, *,a):
        await ctx.channel.trigger_typing()
        im1=Image.open(r'F:\the desktop\UglyBot(new)\databases\minecraft.png')
        draw = ImageDraw.Draw(im1)
        font = ImageFont.truetype("courbd.ttf", 20, )
        draw.text( (80, 45), a, fill=(0, 0, 0), font=font, align="right", )
        im1.save( r'F:\the desktop\UglyBot(new)\databases\minecraftfinal.png', quality=100 )
        await ctx.send( file=discord.File( r'F:\the desktop\UglyBot(new)\databases\minecraftfinal.png' ) )


def setup(bot):
    bot.add_cog( Jokes( bot ) )
