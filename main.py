import discord
import asyncio
from discord.ext import commands
import os

import config

client = commands.Bot(command_prefix=config.PREFIX, case_insensitive=False)
client.remove_command('help')


async def change_status():
    await client.wait_until_ready()
    while client.is_ready():
        await client.change_presence(activity=discord.Game(name=f"{config.PREFIX}help", type=1))
        await asyncio.sleep(20)


@client.event
async def on_ready():
    print('Jederu Blackmarket bot op account: {0.user}'.format(client))


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        await ctx.send("Dit commando betaat niet.")

    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Je voert dit commando niet correct uit. Zie bm!help.")

    elif isinstance(error, discord.ext.commands.errors.MissingPermissions) or isinstance(error, discord.Forbidden):
        await ctx.send("Je hebt geen toegang tot dit commando.")

    else:
        await ctx.send(error)


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f"cogs.{filename[:-3]}")

client.loop.create_task(change_status())
client.run(config.TOKEN)
