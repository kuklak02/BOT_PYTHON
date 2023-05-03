# import discord
# from discord.ext import commands
# from colors import colors 
# from scrap_stockx import search
# from datetime import datetime
# import discord
# from discord.ext import commands
# from discord import app_commands

# intents = discord.Intents.default()
# intents.members = True
# intents.guilds = True
# intents.messages = True

# bot = commands.Bot(command_prefix="!", intents=intents)

# JORDAN = 1064295389773176994
# DUNK = 1064295405661208667
# DUNK_SB = 1064299732551344138
# COLLABS = 1064295448514412645
# YEEZY = 1064296344354836480
# NEWBALANCE = 1064296394006986762
# OTHERS = 1064296432418443354

# class WantToBuy(commands.Cog):
#     def __init__(self, bot):
#         self.bot = bot

#     @bot.app_commands(name="wtb", description="Want to buy command")
#     async def wtb(self, inter: discord.Interaction):
#         sku = inter.options.get("sku").value
#         payout = inter.options.get("payout").value
#         currency = inter.options.get("currency").value
#         size = inter.options.get("size").value
#         location = inter.options.get("location").value

#         currency_choices = [
#             discord.OptionChoice(name="USD", value="USD"),
#             discord.OptionChoice(name="EUR", value="EUR"),
#             discord.OptionChoice(name="GBP", value="GBP"),
#         ]
#         size_choices = [
#             discord.OptionChoice(name="XS", value="XS"),
#             discord.OptionChoice(name="S", value="S"),
#             discord.OptionChoice(name="M", value="M"),
#             discord.OptionChoice(name="L", value="L"),
#             discord.OptionChoice(name="XL", value="XL"),
#         ]
#         location_choices = [
#             discord.OptionChoice(name="USA", value="USA"),
#             discord.OptionChoice(name="UK", value="UK"),
#             discord.OptionChoice(name="Canada", value="Canada"),
#         ]

#         embed = discord.Embed(title="🛍️ **WTB** 🛍️", color=0x00ff00)
#         embed.add_field(name="`SKU`", value=f"{sku}", inline=False)
#         embed.add_field(name="`PAYOUT`", value=f"{payout}  {currency}", inline=False)
#         embed.add_field(name="`SIZES`", value=size, inline=False)
#         embed.add_field(name="`LOCATED`", value=location, inline=False)
#         embed.set_footer(text="Chilly's bot" , icon_url="https://cdn.discordapp.com/attachments/1060933751091249203/1064355713507393546/marketplace.png")

#         await inter.response.send_message(embed=embed)

#     @wtb.error
#     async def wtb_error(self, ctx, error):
#         if isinstance(error, commands.errors.CommandInvokeError):
#             await ctx.send("Error: Something went wrong.")

# async def setup(bot):
#     bot.add_cog(WantToBuy(bot))