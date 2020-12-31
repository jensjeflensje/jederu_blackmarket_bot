from discord.ext import commands
from embeds import HELP


class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        await ctx.send(embed=HELP)


def setup(client):
    client.add_cog(Help(client))