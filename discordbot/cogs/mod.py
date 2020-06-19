import discord
from discord.ext import tasks, commands
import flask
import os

class mod( commands.Cog ):
    def __init__(self, bot):
        self.bot = bot

        @commands.group( name="bank", pass_context=True )
        async def _bank(self, ctx):
            """Bank operations"""
            if ctx.invoked_subcommand is None:
                await send_cmd_help( ctx )

        @_bank.command( pass_context=True, no_pm=True )
        async def register(self, ctx):
            user = ctx.author
            """Registers an account at the biteki bank"""
            user_id = str( ctx.message.author.id )
            if user_id not in self.bank:
                self.bank[user_id] = {"name": user.name, "balance": 100}
                fileIO( "data/economy/bank.json", "save", self.bank )
                await ctx.send( "{} Account opened. Current balance: {}".format( user.mention, str(
                    self.check_balance( user_id ) ) ) )
            else:
                await ctx.send( "{} You already have an account at the Biteki bank.".format( user.mention ) )

        @_bank.command( pass_context=True )
        async def balance(self, ctx, user: discord.Member = None):
            author_id = str( ctx.message.author.id )
            author = ctx.message.author
            """Shows balance of user.
            Defaults to yours."""
            if not user:
                if self.account_check( author_id ):
                    await ctx.send(
                        "{} Your balance is: {}".format( author.mention, str( self.check_balance( author_id ) ) ) )
                else:
                    await ctx.send(
                        "{} You don't have an account at the Biteki bank. Type {}bank register to open one.".format(
                            author.mention, ctx.prefix ) )
            else:
                user_id = str( user.id )
                if self.account_check( user_id ):
                    balance = self.check_balance( user_id )
                    await ctx.send( "{}'s balance is {}".format( user.name, str( balance ) ) )
                else:
                    await ctx.send( "That user has no bank account." )

        @_bank.command( pass_context=True )
        async def transfer(self, ctx, user: discord.Member, sum: int):
            """Transfer credits to other users"""
            author = ctx.message.author
            id = str( ctx.message.author.id )
            id2 = str( user.id )
            if author == user:
                await ctx.send( "You can't transfer money to yourself." )
                return
            if sum < 1:
                await ctx.send( "You need to transfer at least 1 credit." )
                return
            if self.account_check( id2 ):
                if self.enough_money( id, sum ):
                    self.withdraw_money( id, sum )
                    self.add_money( id2, sum )
                    logger.info(
                        "{}({}) transferred {} credits to {}({})".format( author.name, id, str( sum ), user.name,
                                                                          id2 ) )
                    await ctx.send(
                        "{} credits have been transferred to {}'s account.".format( str( sum ), user.name ) )
                else:
                    await ctx.send( "You don't have that sum in your bank account." )
            else:
                await ctx.send( "That user has no bank account." )

        @_bank.command( name="set", pass_context=True )
        @commands.is_owner()
        async def _set(self, ctx, user: discord.Member, sum: int):
            """Sets money of user's bank account
            Admin/owner restricted."""
            author = ctx.message.author
            id = str( ctx.message.author.id )
            id2 = str( user.id )
            done = self.set_money( id2, sum )
            if done:
                logger.info( "{}({}) set {} credits to {} ({})".format( author.name, id, str( sum ), user.name, id2 ) )
                await ctx.send( "{}'s credits have been set to {}".format( user.name, str( sum ) ) )
            else:
                await ctx.send( "User has no bank account." )

        @commands.command()
        async def jobs(self, ctx):
            await ctx.send( "Current jobs:\nyoutuber\nfastfood worker" )

        @commands.group( name="job" )
        async def _job(self, ctx):
            """job operations"""
            if ctx.invoked_subcommand is None:
                await send_cmd_help( ctx )

        @_job.command( pass_context=True, no_pm=True )
        async def register(self, ctx, *, job=None):
            user = ctx.author
            """Registers a job"""
            user_id = str( ctx.message.author.id )
            if user_id in self.jobs:
                await ctx.send( "{} You already have a job.".format( user.mention ) )
                return
            if job == None:
                await ctx.send( "You for got to put a job" )
                return
            if job != "youtuber" and job != "fastfood worker":
                await ctx.send( "That's not a job, try doing k/jobs to see all the jobs." )
                return
            if job == "youtube" or "fastfood worker":
                self.jobs[user_id] = {"name": user.name, "job": job}
                fileIO( "data/economy/jobs.json", "save", self.jobs )
                await ctx.send( "{} has gotten a job, the job is {}".format( user.mention, job ) )
            else:
                await ctx.send( "something happened." )

        @_job.command()
        async def work(self, ctx):
            failed_randint = random.randint( 1, 50 )
            successful_randint = random.randint( 100, 150 )
            id = str( ctx.message.author.id )
            ytchoice = ["failed", "successful"]
            youtube = random.choice( ytchoice )
            if id not in self.job:
                await ctx.send(
                    "{} You don't have an account at the Biteki bank. Type {}bank register to open one.".format(
                        author.mention, ctx.prefix ) )
                return
            if self.check_job( id, "youtuber" ):
                if youtube == "failed":
                    ctx.send(
                        f"Yikes your video didn't do to well maybe make a better one next time, you received {failed_randint} coins." )
                    self.add_money( id, failed_randint )
                    return
                if youtube == "successful":
                    ctx.send( f"Your video did pretty well congratz, you received {successful_randint}" )
                    self.add_money( id, successful_randint )

        @commands.command( pass_context=True, no_pm=True )
        async def payday(self, ctx):
            """Get some free credits"""
            author = ctx.message.author
            id = str( ctx.message.author.id )
            if self.account_check( id ):
                if id in self.payday_register:
                    seconds = abs( self.payday_register[id] - int( time.perf_counter() ) )
                    if seconds >= self.settings["PAYDAY_TIME"]:
                        self.add_money( id, self.settings["PAYDAY_CREDITS"] )
                        self.payday_register[id] = int( time.perf_counter() )
                        await ctx.send( "{} Here, take some credits. Enjoy! (+{} credits!)".format( author.mention, str(
                            self.settings["PAYDAY_CREDITS"] ) ) )
                    else:
                        await ctx.send( "{} Too soon. For your next payday you have to wait {}.".format( author.mention,
                                                                                                         self.display_time(
                                                                                                             self.settings[
                                                                                                                 "PAYDAY_TIME"] - seconds ) ) )
                else:
                    self.payday_register[id] = int( time.perf_counter() )
                    self.add_money( id, self.settings["PAYDAY_CREDITS"] )
                    await ctx.send( "{} Here, take some credits. Enjoy! (+{} credits!)".format( author.mention, str(
                        self.settings["PAYDAY_CREDITS"] ) ) )
            else:
                await ctx.send( "{} You need an account to receive credits.".format( author.mention ) )

        @commands.command( pass_context=True, no_pm=True )
        async def payweek(self, ctx):
            """Get some free credits"""
            author = ctx.message.author
            id = str( ctx.message.author.id )
            if self.account_check( id ):
                if id in self.payweek_register:
                    seconds = abs( self.payweek_register[id] - int( time.perf_counter() ) )
                    if seconds >= self.settings["PAYWEEK_TIME"]:
                        self.add_money( id, self.settings["PAYWEEK_CREDITS"] )
                        self.payweek_register[id] = int( time.perf_counter() )
                        await ctx.send( "{} Here, take some credits. Enjoy! (+{} credits!)".format( author.mention, str(
                            self.settings["PAYWEEK_CREDITS"] ) ) )
                    else:
                        await ctx.send(
                            "{} Too soon. For your next payweek you have to wait {}.".format( author.mention,
                                                                                              self.display_time(
                                                                                                  self.settings[
                                                                                                      "PAYWEEK_TIME"] - seconds ) ) )
                else:
                    self.payweek_register[id] = int( time.perf_counter() )
                    self.add_money( id, self.settings["PAYWEEK_CREDITS"] )
                    await ctx.send( "{} Here, take some credits. Enjoy! (+{} credits!)".format( author.mention, str(
                        self.settings["PAYWEEK_CREDITS"] ) ) )
            else:
                await ctx.send( "{} You need an account to receive credits.".format( author.mention ) )

        @commands.command()
        @commands.cooldown( rate=1, per=30.0, type=commands.BucketType.user )
        async def beg(self, ctx):
            randint = random.randint( 1, 150 )
            author = ctx.message.author
            id = str( ctx.message.author.id )
            list = [f"**Jake paul** has donated {randint} coins to {author.mention}.",
                    f"**Thanos** has donated {randint} coins to {author.mention}."]
            donate = random.choice( list )
            self.add_money( id, randint )
            if self.account_check( id ):
                await ctx.send( f"{donate}" )
            else:
                await ctx.send(
                    "{} You don't have an account at the Biteki bank. Type {}bank register to open one.".format(
                        author.mention, ctx.prefix ) )

        @commands.command()
        @commands.cooldown( rate=1, per=10.0, type=commands.BucketType.user )
        async def rob(self, ctx, user: discord.Member):
            choice = ["failed", "successful", "caught"]
            chance = random.choice( choice )
            user_id = str( user.id )
            author = ctx.message.author
            id = str( ctx.message.author.id )
            if id not in self.bank:
                await ctx.send(
                    "{} You don't have an account at the Biteki bank. Type {}bank register to open one.".format(
                        author.mention, ctx.prefix ) )
            if user_id not in self.bank:
                await ctx.send( f"{user.mention} doesn't have an a account" )
                return
            if not self.enough_money( user_id, 500 ):
                await ctx.send( f"{user.mention} doesn't have over 500 coins." )
                return
            if not self.enough_money( id, 500 ):
                await ctx.send( f"You don't have over 100 coins." )
                return
            randint = random.randint( 500, (self.check_balance( user_id )) )
            if chance == "successful":
                if self.enough_money( user_id, 500 ):
                    await ctx.send( f"You robbed {user.mention} for **{randint}** amount of coins, congratz." )
                    self.add_money( id, randint )
                    self.withdraw_money( user_id, randint )
                    return
            if chance == "failed":
                if self.enough_money( id, 500 ):
                    await ctx.send( f"You failed to rob {user.mention}, and got nothing." )
                    return
            if chance == "caught":
                if self.enough_money( id, 100 ):
                    await ctx.send( f"You were caught by {user.mention}, and had to pay them **500 coins**" )
                    self.add_money( user_id, 500 )
                    self.withdraw_money( id, 500 )

        @commands.command()
        async def leaderboard(self, top: int = 10):
            """Prints out the leaderboard
            Defaults to top 10"""  # Originally coded by Airenkun - edited by irdumb
            if top < 1:
                top = 10
            bank_sorted = sorted( self.bank.items(), key=lambda x: x[1]["balance"], reverse=True )
            if len( bank_sorted ) < top:
                top = len( bank_sorted )
            topten = bank_sorted[:top]
            highscore = ""
            place = 1
            for id in topten:
                highscore += str( place ).ljust( len( str( top ) ) + 1 )
                highscore += (id[1]["name"] + " ").ljust( 23 - len( str( id[1]["balance"] ) ) )
                highscore += str( id[1]["balance"] ) + "\n"
                place += 1
            if highscore:
                if len( highscore ) < 1985:
                    await ctx.send( "```py\n" + highscore + "```" )
                else:
                    await ctx.send( "The leaderboard is too big to be displayed. Try with a lower <top> parameter." )
            else:
                await ctx.send( "There are no accounts in the bank." )

        @commands.command()
        async def payouts(self, ctx):
            """Shows slot machine payouts"""
            slot_payouts = """Slot machine payouts:
                :two: :two: :six: Bet * 5000
                :four_leaf_clover: :four_leaf_clover: :four_leaf_clover: +1000
                :cherries: :cherries: :cherries: +800
                :two: :six: Bet * 4
                :cherries: :cherries: Bet * 3
                Three symbols: +500
                Two symbols: Bet * 2"""
            await ctx.send( slot_payouts )

        @commands.command( pass_context=True, no_pm=True )
        async def slot(self, ctx, bid: int):
            """Play the slot machine"""
            author = ctx.message.author
            id = str( ctx.message.author.id )
            if self.enough_money( id, bid ):
                if bid >= self.settings["SLOT_MIN"] and bid <= self.settings["SLOT_MAX"]:
                    if id in self.slot_register:
                        if abs( self.slot_register[id] - int( time.perf_counter() ) ) >= self.settings["SLOT_TIME"]:
                            self.slot_register[id] = int( time.perf_counter() )
                            await self.slot_machine( ctx.message, bid )
                        else:
                            await ctx.send(
                                "Slot machine is still cooling off! Wait {} seconds between each pull".format(
                                    self.settings["SLOT_TIME"] ) )
                    else:
                        self.slot_register[id] = int( time.perf_counter() )
                        await self.slot_machine( ctx.message, bid )
                else:
                    await ctx.send(
                        "{0} Bid must be between {1} and {2}.".format( author.mention, self.settings["SLOT_MIN"],
                                                                       self.settings["SLOT_MAX"] ) )
            else:
                await ctx.send(
                    "{0} You need an account with enough funds to play the slot machine.".format( author.mention ) )

        async def slot_machine(self, message, bid):
            id = str( message.author.id )
            reel_pattern = [":cherries:", ":cookie:", ":two:", ":four_leaf_clover:", ":cyclone:", ":sunflower:",
                            ":six:", ":mushroom:", ":heart:", ":snowflake:"]
            padding_before = [":mushroom:", ":heart:", ":snowflake:"]  # padding prevents index errors
            padding_after = [":cherries:", ":cookie:", ":two:"]
            reel = padding_before + reel_pattern + padding_after
            reels = []
            for i in range( 0, 3 ):
                n = randint( 3, 12 )
                reels.append( [reel[n - 1], reel[n], reel[n + 1]] )
            line = [reels[0][1], reels[1][1], reels[2][1]]

            display_reels = "  " + reels[0][0] + " " + reels[1][0] + " " + reels[2][0] + "\n"
            display_reels += ">" + reels[0][1] + " " + reels[1][1] + " " + reels[2][1] + "\n"
            display_reels += "  " + reels[0][2] + " " + reels[1][2] + " " + reels[2][2] + "\n"

            if line[0] == ":two:" and line[1] == ":two:" and line[2] == ":six:":
                bid = bid * 5000
                await message.channel.send(
                    "{}{} 226! Your bet is multiplied * 5000! {}! ".format( display_reels, message.author.mention,
                                                                            str( bid ) ) )
            elif line[0] == ":four_leaf_clover:" and line[1] == ":four_leaf_clover:" and line[
                2] == ":four_leaf_clover:":
                bid += 1000
                await message.channel.send( "{}{} Three FLC! +1000! ".format( display_reels, message.author.mention ) )
            elif line[0] == ":cherries:" and line[1] == ":cherries:" and line[2] == ":cherries:":
                bid += 800
                await message.channel.send(
                    "{}{} Three cherries! +800! ".format( display_reels, message.author.mention ) )
            elif line[0] == line[1] == line[2]:
                bid += 500
                await message.channel.send(
                    "{}{} Three symbols! +500! ".format( display_reels, message.author.mention ) )
            elif line[0] == ":two:" and line[1] == ":six:" or line[1] == ":two:" and line[2] == ":six:":
                bid = bid * 4
                await message.channel.send(
                    "{}{} 26! Your bet is multiplied * 4! {}! ".format( display_reels, message.author.mention,
                                                                        str( bid ) ) )
            elif line[0] == ":cherries:" and line[1] == ":cherries:" or line[1] == ":cherries:" and line[
                2] == ":cherries:":
                bid = bid * 3
                await message.channel.send(
                    "{}{} Two cherries! Your bet is multiplied * 3! {}! ".format( display_reels, message.author.mention,
                                                                                  str( bid ) ) )
            elif line[0] == line[1] or line[1] == line[2]:
                bid = bid * 2
                await message.channel.send(
                    "{}{} Two symbols! Your bet is multiplied * 2! {}! ".format( display_reels, message.author.mention,
                                                                                 str( bid ) ) )
            else:
                await message.channel.send( "{}{} Nothing! Lost bet. ".format( display_reels, message.author.mention ) )
                self.withdraw_money( id, bid )
                await message.channel.send( "Credits left: {}".format( str( self.check_balance( id ) ) ) )
                return True
            self.add_money( id, bid )
            await message.channel.send( "Current credits: {}".format( str( self.check_balance( id ) ) ) )

        @commands.group( pass_context=True, no_pm=True )
        @commands.is_owner()
        async def economyset(self, ctx):
            """Changes economy module settings"""
            if ctx.invoked_subcommand is None:
                msg = "```"
                for k, v in self.settings.items():
                    msg += str( k ) + ": " + str( v ) + "\n"
                msg += "\nType {}help economyset to see the list of commands.```".format( ctx.prefix )
                await ctx.send( msg )

        @economyset.command()
        async def slotmin(self, ctx, bid: int):
            """Minimum slot machine bid"""
            self.settings["SLOT_MIN"] = bid
            await ctx.send( "Minimum bid is now " + str( bid ) + " credits." )
            fileIO( "data/economy/settings.json", "save", self.settings )

        @economyset.command()
        async def slotmax(self, ctx, bid: int):
            """Maximum slot machine bid"""
            self.settings["SLOT_MAX"] = bid
            await ctx.send( "Maximum bid is now " + str( bid ) + " credits." )
            fileIO( "data/economy/settings.json", "save", self.settings )

        @economyset.command()
        async def slottime(self, ctx, seconds: int):
            """Seconds between each slots use"""
            self.settings["SLOT_TIME"] = seconds
            await ctx.send( "Cooldown is now " + str( seconds ) + " seconds." )
            fileIO( "data/economy/settings.json", "save", self.settings )

        @economyset.command()
        async def paydaytime(self, ctx, seconds: int):
            """Seconds between each payday"""
            self.settings["PAYDAY_TIME"] = seconds
            await ctx.send( "Value modified. At least " + str( seconds ) + " seconds must pass between each payday." )
            fileIO( "data/economy/settings.json", "save", self.settings )

        @economyset.command()
        async def paydaycredits(self, ctx, credits: int):
            """Credits earned each payday"""
            self.settings["PAYDAY_CREDITS"] = credits
            await ctx.send( "Every payday will now give " + str( credits ) + " credits." )
            fileIO( "data/economy/settings.json", "save", self.settings )

        def job_check(self, id):
            if id in self.jobs:
                return True
            else:
                return False

        def hasjob_check(self, id, work):
            if self.account_check( id ):
                if self.jobs[id]["job"] >= str( work ):
                    return True
                else:
                    return False
            else:
                return False

        def canwork_check(self, id):
            if self.job_check( id ):
                return self.jobs[id]["job"]
            else:
                return False

        def account_check(self, id):
            if id in self.bank:
                return True
            else:
                return False

        def check_job(self, id):
            if self.account_check( id ):
                return self.bank[id]["job"]
            else:
                return False

        def check_balance(self, id):
            if self.account_check( id ):
                return self.bank[id]["balance"]
            else:
                return False

        def add_money(self, id, amount):
            if self.account_check( id ):
                self.bank[id]["balance"] = self.bank[id]["balance"] + int( amount )
                fileIO( "data/economy/bank.json", "save", self.bank )
            else:
                return False

        def withdraw_money(self, id, amount):
            if self.account_check( id ):
                if self.bank[id]["balance"] >= int( amount ):
                    self.bank[id]["balance"] = self.bank[id]["balance"] - int( amount )
                    fileIO( "data/economy/bank.json", "save", self.bank )
                else:
                    return False
            else:
                return False

        def enough_money(self, id, amount):
            if self.account_check( id ):
                if self.bank[id]["balance"] >= int( amount ):
                    return True
                else:
                    return False
            else:
                return False

        def set_money(self, id, amount):
            if self.account_check( id ):
                self.bank[id]["balance"] = amount
                fileIO( "data/economy/bank.json", "save", self.bank )
                return True
            else:
                return False

        def display_time(self, seconds, granularity=2):  # What would I ever do without stackoverflow?
            intervals = (  # Source: http://stackoverflow.com/a/24542445
                ('weeks', 604800),  # 60 * 60 * 24 * 7
                ('days', 86400),  # 60 * 60 * 24
                ('hours', 3600),  # 60 * 60
                ('minutes', 60),
                ('seconds', 1),
            )

            result = []

            for name, count in intervals:
                value = seconds // count
                if value:
                    seconds -= value * count
                    if value == 1:
                        name = name.rstrip( 's' )
                    result.append( "{} {}".format( value, name ) )
            return ', '.join( result[:granularity] )









def setup(bot):
    bot.add_cog( mod( bot ) )
