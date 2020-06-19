import discord
from discord.ext import tasks, commands
import flask
import os

class flask( commands.Cog ):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def graph(self,ctx,a):
        import matplotlib.pyplot as plt
        import numpy as np
        x = np.linspace( -5, 5, 100 )
        y = a
        plt.plot( x, y, '-r', label=a )
        plt.title( 'Graph of y=2x+1' )
        plt.xlabel( 'x', color='#1C2833' )
        plt.ylabel( 'y', color='#1C2833' )
        plt.legend( loc='upper left' )
        plt.grid()
        plt.savefig('plot.png')
        await ctx.send( file=discord.File('plot.png' ) )

    @commands.command(pass_context = True)
    async def nickchange(self, ctx, a):
        b = ctx.message.author.name
        await ctx.send(f'changing {b} nickname on server to {a}')
        await ctx.message.author.edit( nick=a )

    @commands.command()
    async def randomsentence(self,ctx):
        await ctx.send('A bot will make a sentence using grammar, it will not make sense, but works in a grammar sense')
        await ctx.send('more info: read book https://www.amazon.com/Language-Instinct-Creates-Perennial-Classics/dp/0061336467/ref=tmm_pap_swatch_0?_encoding=UTF8&qid=&sr=')



        import random, words

        # all regular and singular, for now
        C_CONJ = ["and", "but", "for", "or", "so", "yet"]  # Coordinating conjunctions
        DETERMINERS = ["the", "this", "that", "my", "your", "his", "her", "its", "our", "their", "one", "each", "every",
                       "another"]  # https://www.ef.com/ca/english-resources/english-grammar/determiners/

        class Phrase( object ):
            """docstring for Phrase."""

            def __init__(self):
                super( Phrase, self ).__init__()
                self.words = []

            def __repr__(self):
                return " ".join( self.words )

            def populate(self):
                raise NotImplementedError

        class NounPhrase( Phrase ):
            """docstring for NounPhrase."""

            def __init__(self):
                super( NounPhrase, self ).__init__()
                self.num_adjectives = random.randrange( 0, 4 )  # arbitary 4?
                self.num_adverbs = random.randrange( 0, 2 ) if self.num_adjectives else 0
                self.noun = str( words.Noun() )
                self.populate()

            def generate_adjectives(self):
                self.adjectives = [str( words.Adjective() ) for i in range( self.num_adjectives )]
                self.words = self.adjectives + self.words

            def generate_adverbs(self):
                self.adverbs = [str( words.Adverb() ) for i in range( self.num_adverbs )]
                self.words = self.adverbs + self.words

            def generate_determiner(self):
                if random.random() < 0.5:
                    return None
                else:
                    self.determiner = random.choice( DETERMINERS )
                    self.words = [self.determiner] + self.words

            def populate(self):
                self.words = [self.noun]
                self.generate_adjectives()
                self.generate_adverbs()
                self.generate_determiner()

        class VerbPhrase( Phrase ):
            """docstring for VerbPhrase."""

            def __init__(self):
                super( VerbPhrase, self ).__init__()
                self.verb = str( words.Verb() )
                self.num_adverbs = random.randrange( 0, 2 )
                self.noun_phrase = str( NounPhrase() )
                self.populate()

            def generate_adverbs(self):
                self.adverbs = [str( words.Adverb() ) for i in range( self.num_adverbs )]
                self.words += self.adverbs

            def populate(self):
                self.words.append( self.verb )
                if random.random() < 0.5:
                    self.words.append( self.noun_phrase )
                self.generate_adverbs()

        class Sentence( Phrase ):
            """docstring for Sentence."""

            def __init__(self):
                super( Sentence, self ).__init__()
                self.noun_phrase = NounPhrase()
                self.verb_phrase = VerbPhrase()
                self.populate()

            def populate(self):
                self.words = self.noun_phrase.words + self.verb_phrase.words
                # Coordinating conjunction
                if random.random() < 0.25:
                    new_clause = Sentence()
                    conjunction = random.choice( C_CONJ )
                    self.words.append( conjunction )
                    self.words += new_clause.words

            def __repr__(self):
                content = " ".join( self.words ) + "."
                return content.capitalize()


        n = Sentence()
        print( n )
        await ctx.send(n)


def setup(bot):
    bot.add_cog( flask( bot ) )
