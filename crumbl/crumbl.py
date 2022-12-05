import aiohttp
import asyncio
from bs4 import BeautifulSoup
from redbot.core import commands

class crumbl(commands.Cog):
    """Gets all the cookies"""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.__url: str = "https://crumblcookies.com/nutrition"
        self.__session = aiohttp.ClientSession()

    def cog_unload(self) -> None:
        if self.__session:
            asyncio.get_event_loop().create_task(self.__session.close())

    @commands.command()
    async def crumbl(self, ctx: commands.Context) -> None:
        """Gets all the cookies"""

        await ctx.trigger_typing()

        try:
            async with self.__session.get(self.__url) as response:
                rawingredients = await response.html()
                soup = BeautifulSoup(rawingredients, "html.parser")
                cookies = soup.select('#nutrition-info-page > div > div > div._mobile-page-1 > div > div.bg-lightGray.sm\:-mt-2\.5 > div > div:nth-child(2) > div.flex.pb-5.pr-5 > div.sm\:pt-5 > b')
                await ctx.send(cookies)
        except aiohttp.ClientError:
            await ctx.send("I was unable to get cookies.")
