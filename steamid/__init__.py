from redbot.core.bot import Red

from .SteamID import SteamID


def setup(bot: Red):
    bot.add_cog(steamID())
