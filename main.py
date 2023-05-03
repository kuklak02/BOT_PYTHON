import os 
import discord
from dotenv import load_dotenv
from discord.ext import commands
from intents import bot
import settings

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

logger = settings.logging.getLogger("bot")

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

def run():



    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")
        logger.info(f"Guild ID: {bot.guilds[0].id}")
        
        # wanttobuy = WantToBuy(name="wtb", description="Make an offer")
        # bot.tree.add_command(wanttobuy)
        for slashcmd_file in settings.SLASHCMDS_DIR.glob("*.py"):
            if slashcmd_file.name != "__init__.py":
                    await bot.load_extension(f"slashcmds.{slashcmd_file.name[:-3]}")
        bot.tree.copy_global_to(guild=settings.GUILDS_ID)

        # for cog_file in settings.COGS_DIR.glob("*.py"):
        #     if cog_file.name != "__init__.py":
        #         await bot.load_extension(f"cogs.{cog_file.name[:-3]}")

        # await bot.tree.sync(guild=settings.GUILDS_ID)


        
    bot.run(TOKEN, root_logger=True)

if __name__ == "__main__":
    run()