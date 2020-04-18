import discord
from discord.ext import commands

bot=commands.Bot(command_prefix='d?')

@bot.event
async def on_ready():
    print('>>Bot is online<<')

@bot.command()
async def ping(ctx):
    await ctx.send(F'我現在的延遲有{int(bot.latency*1000)}毫秒')

bot.run('Njc4OTY3MDg5MDM3MzEyMDAx.Xpr4jA.ICg6U1VBlrcXIFdki48-jxw8UNY')