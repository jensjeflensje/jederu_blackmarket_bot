from discord.ext import commands
import discord
import config
from action import execute_action_for_tokens


class RankName(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def rankname(self, ctx, name:str):
        if not ctx.guild:
            return
        await execute_action_for_tokens(ctx, self.client, execute, (ctx.guild, name), config.PRICES["rankname"])


async def execute(guild, name):
    role = guild.get_role(config.LEGEND_RANK)
    await role.edit(name=name)


def setup(client):
    client.add_cog(RankName(client))