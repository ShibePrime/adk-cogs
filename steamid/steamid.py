import aiohttp
import asyncio
from bs4 import BeautifulSoup

from redbot.core import commands


class steamid(commands.Cog):
    """Gets a random fact."""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.__url: str = "https://steamid.io/lookup/"
        self.__session = aiohttp.ClientSession()

    def cog_unload(self) -> None:
        if self.__session:
            asyncio.get_event_loop().create_task(self.__session.close())

    @commands.command()
    async def steamid(self, ctx: commands.Context) -> None:
        await ctx.trigger_typing()

        try:
            # Get the response from the URL
            response = await self.__session.get(self.__url + str(ctx))

            # Get the response's HTML as a string
            html = await response.text()

            # Parse the HTML with Beautiful Soup
            soup = BeautifulSoup(html, 'html.parser')

            # Find all div elements with the class '#content > dl'
            div = soup.find_all('div', class_='#content')

            # Loop through the divs and send their text to the Discord channel
            await ctx.send(div)
        except aiohttp.ClientError:
            await ctx.send("I was unable to get it")
