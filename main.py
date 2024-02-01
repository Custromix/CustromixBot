import settings
import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.all()
intents.members = True
intents.message_content = True


async def start_bot():
    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        print(bot.user)
        print(bot.user.id)
        print("-----------")

    await bot.load_extension('cogs.commands_cog')
    await bot.start(settings.DISCORD_API_SECRET)


def run():
    asyncio.run(start_bot())


if __name__ == "__main__":
    run()
