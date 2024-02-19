import discord
from discord.ext import commands

class FixV_voicelogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        embed = None
        if before.channel is None and after.channel is not None:
            embed = discord.Embed(
                title="Ein Mitglied ist einem Discord Voice Channel beigetreten",
                description=f"{member.mention} ist soeben einem Discord Voice Channel namens: {after.channel.mention} beigetreten",
                color=discord.Color.green() 
            )
            action = "beigetreten"
        elif before.channel is not None and after.channel is not None and before.channel != after.channel:
            moved_from = before.channel
            moved_to = after.channel
            embed = discord.Embed(
                title="Ein Mitglied wurde in einen anderen Discord Voice Channel verschoben",
                description=f"{member.mention} wurde von {moved_from.mention} nach {moved_to.mention} verschoben",
                color=discord.Color.blue() 
            )
            action = "verschoben"
        elif before.channel is not None and after.channel is None:
            embed = discord.Embed(
                title="Ein Mitglied hat den Discord Voice Channel verlassen",
                description=f"{member.mention} hat den Discord Voice Channel {before.channel.mention} verlassen",
                color=discord.Color.red() 
            )
            action = "verlassen"
        if embed is not None:
            embed.set_footer(icon_url=self.bot.user.avatar.url, text=self.bot.user.name)
            embed.set_author(icon_url=self.bot.user.avatar.url, name=self.bot.user.name)
            channel = self.bot.get_channel(1206640084535746590)
            if channel:
                await channel.send(embed=embed)
                print(f"{member} ist soeben dem Discord Voice Channel {action}")
            else:
                print("Der Zielkanal wurde nicht gefunden. Stelle sicher, dass die Kanal-ID korrekt ist und der Bot Zugriff auf den Kanal hat.")

def setup(bot):
    bot.add_cog(FixV_voicelogs(bot))
