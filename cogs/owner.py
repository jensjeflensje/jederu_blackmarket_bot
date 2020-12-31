from discord.ext import commands
import config
from action import execute_action_for_tokens
import asyncio


class Owner(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def owner(self, ctx):
        if not ctx.guild:
            return
        await execute_action_for_tokens(ctx, self.client, execute, (ctx.guild, ctx.author), config.PRICES["owner"])


async def execute(guild, member):
    role = guild.get_role(config.OWNER_RANK)
    await member.add_roles(role)
    await asyncio.sleep(3600)
    await member.remove_roles(role)


def setup(client):
    client.add_cog(Owner(client))