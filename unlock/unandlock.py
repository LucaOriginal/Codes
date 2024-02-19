import discord
from discord.ext import commands
from discord.commands import slash_command


class unlockch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @slash_command(description="sperre ein kanal")
    @discord.default_permissions(manage_channels=True)
    async def lock(self, ctx, channel: discord.TextChannel, grund: str, teamler: discord.Member):
            await ctx.respond("Hey, deine Aktion War Erfolgreich!", ephemeral=True)
            embed = discord.Embed(
                title=f'Dieser Kanal wurde Erfolgreich Gesperrt',
                description="\n"
                "**Channel:** "f"```{channel}```\n"
                "**Grund:** "f"```{grund}```\n"
                "**Teamler:** "f" {teamler.mention} \n",
                color=0x137901
            )
            embed.set_author(icon_url=self.bot.user.display_avatar.url, name=self.bot.user.name)
            embed.set_footer(icon_url=self.bot.user.display_avatar.url, text=self.bot.user.name)
            embed.set_image(url="")
            embed.timestamp = discord.utils.utcnow()
            channel = channel or ctx.channel
            overwrite = channel.overwrites_for(ctx.guild.get_role(1202311032916410388))
            overwrite.send_messages = False
            await channel.set_permissions(ctx.guild.get_role(1202311032916410388), overwrite=overwrite)
            await channel.send(embed=embed)


    @slash_command(description="entsperre ein kanal")
    @discord.default_permissions(manage_channels=True)
    async def unlock(self, ctx, channel: discord.TextChannel, grund: str, teamler: discord.Member):
        await ctx.respond("Hey, deine Aktion War Erfolgreich!", ephemeral=True)
        embed = discord.Embed(
            title=f'Dieser Kanal wurde Erfolgreich Entsperrt',
            description="\n"
                        "**Channel:** "f"```{channel}```\n"
                        "**Grund:** "f"```{grund}```\n"
                        "**Teamler:** "f" {teamler.mention} \n",
            color=0x137901
        )
        embed.set_author(icon_url=self.bot.user.display_avatar.url, name=self.bot.user.name)
        embed.set_footer(icon_url=self.bot.user.display_avatar.url, text=self.bot.user.name)
        embed.timestamp = discord.utils.utcnow()
        embed.set_image(url="")
        channel = channel or ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.get_role(1202311032916410388))
        overwrite.send_messages = True
        await channel.set_permissions(ctx.guild.get_role(1202311032916410388), overwrite=overwrite)
        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(unlockch(bot))
