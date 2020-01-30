from redbot.core import commands
import discord


class CDT(commands.Cog):

    COLLECTOR_ICON = 'https://raw.githubusercontent.com/CollectorDevTeam/assets/master/data/cdt_icon.png'
    # def _init__(self):
    #     pass

    def cdt_embed(self, ctx=None):
        """Discord Embed constructor with CollectorDevTeam defaults."""
        emfooter_icon_url = CDT.COLLECTOR_ICON
        if ctx is not None:
            emcolor = ctx.message.author.color
            emfooter = "Requested by {}".format(ctx.message.author.nick)
            if ctx.message.author.avatar is not None:
                emfooter_icon_url = ctx.message.author.avatar
        else:
            emcolor = discord.Color.gold()
            emfooter = "CollectorDevTeam"

        embed = discord.Embed(title="Test Embed | Title Field", color=emcolor,
                              description="CollectorDevTeam | description text",
                              url="https://discordpy.readthedocs.io/en/v1.3.1/api.html#discord.Embed")
        embed.set_author(name="CollectorDevTeam", url="https://patreon.com/collectordevteam", icon_url=CDT.COLLECTOR_ICON)

        embed.set_footer(text=emfooter, icon_url=emfooter_icon_url)
        embed.set_thumbnail(
            url="https://raw.githubusercontent.com/CollectorDevTeam/assets/master/data/images/featured/collector.png")
        embed.set_image(
            url="https://media.discordapp.net/attachments/398210253923024902/672232058818658354/MCoC_CharacterPose-TheCollector-Current_4.png?width=441&height=676")

        return embed