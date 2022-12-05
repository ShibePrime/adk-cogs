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
                rawingredients = await response.text()
                soup = BeautifulSoup(rawingredients, "html.parser")
                cookies = soup.find_all('div', class_="bg-white p-5 pb-0 mb-2.5 rounded-lg")
                lines = [span.get_text() for span in cookies]
                await ctx.send(lines[0])
        except aiohttp.ClientError:
            await ctx.send("I was unable to get cookies.")
