import discord
from discord import app_commands
from scrap_stockx import search
from colors import colors
from intents import bot 
from datetime import datetime






JORDAN = 1064295389773176994
DUNK = 1064295405661208667
DUNK_SB = 1064299732551344138
COLLABS = 1064295448514412645
YEEZY = 1064296344354836480
NEWBALANCE = 1064296394006986762
OTHERS = 1064296432418443354

class WantToBuy(app_commands.Group):
    

    @bot.tree.command(name="wtb", description="Make an offer")
    @app_commands.describe(sku = "Write SKU of the shoe", payout = "choose payout", currency = "choose currency", sizes = "choose sizes", location = "choose location")
    @app_commands.choices(
    # category = [
    #     app_commands.Choice(name="jordan", value="jordan"),
    #     app_commands.Choice(name="dunk", value="dunk"),
    #     app_commands.Choice(name="dunk_sb", value="dunk_sb"),
    #     app_commands.Choice(name="yeezy", value="yeezy"),
    #     app_commands.Choice(name="newbalance", value="newbalance"),
    #     app_commands.Choice(name="collabs", value="collabs"),
    #     app_commands.Choice(name="others", value="others")
    # ],
   
     sizes = [ 
        app_commands.Choice(name="all", value="all"),
        app_commands.Choice(name="6 US / 40 EU", value="6 US / 40 EU"),
        app_commands.Choice(name="6.5 US / 40.5 EU", value="6.5 US / 40.5 EU"),
        app_commands.Choice(name="7 US / 41 EU", value="7 US / 41 EU"),
        app_commands.Choice(name="7.5 US / 41.5 EU", value="7.5 US / 41.5 EU"),
        app_commands.Choice(name="8 US / 42 EU", value="8 US / 42 EU"),
        app_commands.Choice(name="8.5 US / 42.5 EU", value="8.5 US / 42.5 EU"),
        app_commands.Choice(name="9 US / 43 EU", value="9 US / 43 EU"),
        app_commands.Choice(name="9.5 US / 43.5 EU", value="9.5 US / 43.5 EU"),
        app_commands.Choice(name="10 US / 44 EU", value="10 US / 44 EU"),
        app_commands.Choice(name="10.5 US / 44.5 EU", value="10.5 US / 44.5 EU"),
        app_commands.Choice(name="11 US / 45 EU", value="11 US / 45 EU"),
        app_commands.Choice(name="11.5 US / 45.5 EU", value="8.5 US / 45.5 EU"),
        app_commands.Choice(name="12 US / 46 EU", value="12 US / 46 EU"),
        app_commands.Choice(name="12.5 US / 46.5 EU", value="12.5 US / 46.5 EU"),
        app_commands.Choice(name="13 US / 47 EU", value="13 US / 47 EU"),
        app_commands.Choice(name="14 US / 48 EU", value="14 US / 48 EU"),
        app_commands.Choice(name="15 US / 49 EU", value="15 US / 49 EU")
    ],

     location = [
        app_commands.Choice(name="Italy", value="**Italy :flag_it:**"),
        app_commands.Choice(name="Germany ", value="Germany :flag_de:"),
        app_commands.Choice(name="France", value="France :flag_fr:"),
        app_commands.Choice(name="Poland", value="Poland :flag_pl:"),
        app_commands.Choice(name="Spain", value="Spain :flag_es:"),
        app_commands.Choice(name="Greece", value="Greece :flag_gr:"),
        app_commands.Choice(name="Czech Republic", value="Czech Republic :flag_cr:"),
        app_commands.Choice(name="Hungary", value="Hungary :flag_hu:"),
        app_commands.Choice(name="Slovakia", value="Slovakia :flag_sk:"),
        app_commands.Choice(name="Portugal", value="Portugal :flag_pt:"),
        app_commands.Choice(name="Netherlands", value="Netherlands :flag_nl:"),
        app_commands.Choice(name="Belgium", value="Belgium :flag_be:"),
        app_commands.Choice(name="Austria", value="Austria :flag_at:"),
        app_commands.Choice(name="Denmark", value="Denmark :flag_dk:"),
    ],
    
    currency = [
        app_commands.Choice(name="€", value="€"),
        app_commands.Choice(name="$", value="$"),
        app_commands.Choice(name="£", value="£"),
        app_commands.Choice(name="PLN", value="PLN"),
    ]
    
    )
    
  

    async def wtb(self, interaction :discord.Interaction, sku : str, payout : int, currency : app_commands.Choice[str], sizes : app_commands.Choice[str], location : app_commands.Choice[str]):
       
        item = search(f"{sku}")
        title = item['title'].split()
        
        channel1 = bot.get_channel(JORDAN)
        channel2 = bot.get_channel(NEWBALANCE)
        channel3 = bot.get_channel(DUNK)
        channel4 = bot.get_channel(YEEZY)

       
        
        # await interaction.response.send_message(embed=embed)
        
        if channel1 == JORDAN:
            if "jordan" or "Jordan" in item['brand']:
                embed = discord.Embed(title = "🛍️ **WTB** 🛍️", color=colors.chilly)
                embed.add_field(name='`MODEL`', value=item['title'], inline=False)
                embed.add_field(name='`SKU`', value=f"{sku}", inline=False)
                embed.add_field(name='`PAYOUT`', value=f"{payout}  {currency.value}", inline=False)
                embed.add_field(name='`SIZES`', value=sizes.value, inline=False)
                embed.add_field(name='`LOCATED`', value=location.value, inline=False)
                embed.set_image(url=item['media']['imageUrl'])
                embed.timestamp = datetime.utcnow()
                embed.set_footer(text="Chilly's bot", icon_url="https://cdn.discordapp.com/attachments/1060933751091249203/1064355713507393546/marketplace.png")
                await interaction.response.send_message(embed=embed)
            else:
                await interaction.response.send_message("Man... This is not this category, try teh exact one", ephemeral=True)
            
        elif channel2 == NEWBALANCE:
            if "new balance" or "New Balance" or "New balance" in item['brand']:
                embed = discord.Embed(title = "🛍️ **WTB** 🛍️", color=colors.chilly)
                embed.add_field(name='`MODEL`', value=item['title'], inline=False)
                embed.add_field(name='`SKU`', value=f"{sku}", inline=False)
                embed.add_field(name='`PAYOUT`', value=f"{payout}  {currency.value}", inline=False)
                embed.add_field(name='`SIZES`', value=sizes.value, inline=False)
                embed.add_field(name='`LOCATED`', value=location.value, inline=False)
                embed.set_image(url=item['media']['imageUrl'])
                embed.timestamp = datetime.utcnow()
                embed.set_footer(text="Chilly's bot", icon_url="https://cdn.discordapp.com/attachments/1060933751091249203/1064355713507393546/marketplace.png")
                await interaction.response.send_message(embed=embed)
            else:
                await interaction.response.send_message("Man... This is not this category, try teh exact one", ephemeral=True)
            
        elif channel3 == DUNK:
            if "dunk" or "Dunk" in item['brand']:
                embed = discord.Embed(title = "🛍️ **WTB** 🛍️", color=colors.chilly)
                embed.add_field(name='`MODEL`', value=item['title'], inline=False)
                embed.add_field(name='`SKU`', value=f"{sku}", inline=False)
                embed.add_field(name='`PAYOUT`', value=f"{payout}  {currency.value}", inline=False)
                embed.add_field(name='`SIZES`', value=sizes.value, inline=False)
                embed.add_field(name='`LOCATED`', value=location.value, inline=False)
                embed.set_image(url=item['media']['imageUrl'])
                embed.timestamp = datetime.utcnow()
                embed.set_footer(text="Chilly's bot", icon_url="https://cdn.discordapp.com/attachments/1060933751091249203/1064355713507393546/marketplace.png")
                await interaction.response.send_message(embed=embed)
            else:
                await interaction.response.send_message("Man... This is not this category, try teh exact one", ephemeral=True)
            
        elif channel4 == YEEZY:
            if "yeezy" or "Yeezy" in item['brand']:
                embed = discord.Embed(title = "🛍️ **WTB** 🛍️", color=colors.chilly)
                embed.add_field(name='`MODEL`', value=item['title'], inline=False)
                embed.add_field(name='`SKU`', value=f"{sku}", inline=False)
                embed.add_field(name='`PAYOUT`', value=f"{payout}  {currency.value}", inline=False)
                embed.add_field(name='`SIZES`', value=sizes.value, inline=False)
                embed.add_field(name='`LOCATED`', value=location.value, inline=False)
                embed.set_image(url=item['media']['imageUrl'])
                embed.timestamp = datetime.utcnow()
                embed.set_footer(text="Chilly's bot", icon_url="https://cdn.discordapp.com/attachments/1060933751091249203/1064355713507393546/marketplace.png")
                await interaction.response.send_message(embed=embed)
            
            
            else:
                await interaction.response.send_message("Man... This is not this category, try teh exact one", ephemeral=True)
            
    
            
        # embed = discord.Embed(title = "🛍️ **WTB** 🛍️", color=colors.chilly)
        # embed.add_field(name='`MODEL`', value=item['title'], inline=False)
        # embed.add_field(name='Category', value=item['category'], inline=False)
        # embed.add_field(name='`SKU`', value=f"{sku}", inline=False)
        # embed.add_field(name='`PAYOUT`', value=f"{payout}  {currency.value}", inline=False)
        # embed.add_field(name='`SIZES`', value=sizes.value, inline=False)
        # embed.add_field(name='`LOCATED`', value=location.value, inline=False)
        # embed.set_image(url=item['media']['imageUrl'])
        # embed.timestamp = datetime.utcnow()
        # embed.set_footer(text="Chilly's bot", icon_url="https://cdn.discordapp.com/attachments/1060933751091249203/1064355713507393546/marketplace.png")
    


    
async def setup(bot):
    bot.tree.add_command(WantToBuy(bot))
    
    
    
    # type = [
    #     app_commands.Choice(name="Sneakers", value="Sneakers"),
    #     app_commands.Choice(name="Clothing", value="Clothing"),
    #     app_commands.Choice(name="Accesories", value="Accesories")

    # ]?
    
    
    
   
