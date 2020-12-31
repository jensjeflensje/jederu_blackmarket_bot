from discord.ext import commands
import discord
import config
from action import execute_action_for_tokens


class RankColor(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def rankcolor(self, ctx, r:int, g:int, b:int):
        if not ctx.guild:
            return
        color = (r, g, b)
        await execute_action_for_tokens(ctx, self.client, execute, (ctx.guild, color), config.PRICES["rankcolor"])


async def execute(guild, color):
    role = guild.get_role(config.LEGEND_RANK)
    await role.edit(colour=discord.Colour.from_rgb(*color))


def setup(client):
    client.add_cog(RankColor(client))