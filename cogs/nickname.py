from discord.ext import commands
import discord
import config
from action import execute_action_for_tokens


class Nickname(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def nickname(self, ctx, member:discord.Member, nick:str):
        if not ctx.guild:
            return
        if len(nick) >= 32:
            ctx.send("Je nickname is te lang.")
            return
        await execute_action_for_tokens(ctx, self.client, execute, (member, nick), config.PRICES["nickname"])


async def execute(member, nickname):
    await member.edit(nick=nickname)


def setup(client):
    client.add_cog(Nickname(client))