from redbot.core.bot import Red

from .steamid import steamid


def setup(bot: Red):
    bot.add_cog(steamid())
