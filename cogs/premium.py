from discord.ext import commands
import discord
import config
from action import execute_action_for_tokens


class Premium(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def premium(self, ctx):
        if not ctx.guild:
            return
        await execute_action_for_tokens(ctx, self.client, execute, (ctx.guild, ctx.author), config.PRICES["premium"])


async def execute(guild, member):
    role = guild.get_role(config.LEGEND_RANK)
    await member.add_roles(role)


def setup(client):
    client.add_cog(Premium(client))