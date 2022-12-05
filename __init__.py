from redbot.core.bot import Red

from .crumbl import crumbl


def setup(bot: Red):
    bot.add_cog(crumbl())
