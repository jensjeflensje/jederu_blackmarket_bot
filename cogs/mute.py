from discord.ext import commands
import discord
import config
from action import execute_action_for_tokens
import asyncio


class Mute(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def mute(self, ctx, member:discord.Member):
        if not ctx.guild:
            return
        await execute_action_for_tokens(ctx, self.client, execute, (ctx.guild, member), config.PRICES["mute"])


async def execute(guild, member):
    role = guild.get_role(config.MUTED_ROLE)
    await member.add_roles(role)
    await asyncio.sleep(120)
    await member.remove_roles(role)


def setup(client):
    client.add_cog(Mute(client))