from discord.ext import commands


class CommandsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        aliases=['p'],
        help="caca",
        description="Répond avec un gros pong ta race !",
        brief="Repoànd juste pong !"
    )
    async def ping(self, ctx):
        await ctx.send('pong ta grand mère !')


async def setup(bot):
    await bot.add_cog(CommandsCog(bot))
