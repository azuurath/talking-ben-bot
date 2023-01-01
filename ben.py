import discord
from discord.ext import commands
import random
import time

client = commands.Bot(command_prefix="ben-", intents=discord.Intents.all())


@client.event
async def on_ready():
    print("online")


# HOURLY REMINDER
@client.event
async def hour(ctx):
    time.sleep(10000)
    await ctx.send("**Reminder! you can view the commands by doing ben-commands**")

    # doesnt work feel free to remove this stupid shit


# embeds

@client.command()
async def call(ctx):
    yes = discord.Embed(
        title="Ben Says...",
        description="Yes",
        colour=discord.Colour.gold(),

    )
    yes.set_image(url='https://media.tenor.com/R_itimARcLAAAAAd/talking-ben-yes.gif')

    no = discord.Embed(
        title="Ben Says...",
        description="No",
        color=discord.Colour.gold()
    )
    no.set_image(url='https://media.tenor.com/KB4ie5CjGG4AAAAd/phone-call.gif')

    ho = discord.Embed(
        title="Ben Says...",
        description="Ho ho ho!",
        colour=discord.Colour.gold()
    )
    ho.set_image(url='https://media.tenor.com/Cziub06OwxgAAAAC/ben.gif')

    augh = discord.Embed(
        title="Ben Says...",
        description="Auughh",
        colour=discord.Colour.gold()
    )
    augh.set_image(url='https://media.tenor.com/aomZLSiXCQ8AAAAC/ugh.gif')
    responses = [yes, no, ho, augh]

    await ctx.send(embed=random.choice(responses))


@client.command()
async def eat(ctx):
    beans = discord.Embed(
        title="Ben Says...",
        description="Yum!",
        colour=discord.Colour.gold()
    )
    beans.set_image(url='https://media.tenor.com/UZOcqAyMu4QAAAAd/talking-ben-eating.gif')

    await ctx.send(embed=beans)


@client.command()
async def drink(ctx):
    cider = discord.Embed(
        title="Ben says...",
        description="Tasty!",
        colour=discord.Colour.gold()
    )
    cider.set_image(url='https://media.tenor.com/hdPVLfpe81cAAAAC/talking-ben-drinking.gif')

    await ctx.send(embed=cider)


@client.command()
async def punch(ctx):
    beatup = discord.Embed(
        title="Ben says...",
        description="Ow!",
        colour=discord.Colour.gold()
    )
    beatup.set_image(url='https://media.tenor.com/G942SqnerBMAAAAC/talking-ben-ben.gif')

    await ctx.send(embed=beatup)


@client.command()
async def newspaper(ctx):
    paper = discord.Embed(
        title="Ben says...",
        description="Na na na!",
        colour=discord.Colour.gold()
    )
    paper.set_image(url='https://media.tenor.com/s5pxSHOEZ7kAAAAd/talking-ben-talking.gif')

    await ctx.send(embed=paper)


@client.command()
async def commands(ctx):
    cmds = discord.Embed(
        title="Talking Ben Commands",
        description="contact ub#4044 for any help \n\n"
                    " ben-commands \n"
                    " ben-call \n"
                    " ben-eat \n"
                    " ben-drink \n"
                    " ben-punch \n"
                    "ben-newspaper \n",
        colour=discord.Color.blue()

    )
    await ctx.send(embed=cmds)


@client.command()
async def repeat(ctx, *, arg):
    saywhatisaid = discord.Embed(
        title="Ben says...",
        description=arg,
        colour=discord.Colour.green()
    )
    saywhatisaid.set_footer(text="(this is a repeat message, not said by actual ben.)")
    saywhatisaid.set_image(url='https://media.tenor.com/wOGMBH-Pe9IAAAAC/ben-aheh.gif')
    await ctx.send(embed=saywhatisaid)


client.run('token')
