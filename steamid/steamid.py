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
        response = await self.__session.get(self.__url + str(ctx.))

        # Get the response's HTML as a string
        html = await response.text()

        # Parse the HTML with Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')

        # Find all div elements with the class '#content > dl'
        div = soup.find('div', class_='#content')

        # Check if the div exists
        if div:
            # If the div exists, send its text to the Discord channel
            await ctx.send(div.text)
        else:
            # If the div doesn't exist, send a different message
            await ctx.send("empty")
    except aiohttp.ClientError:
        # Handle ClientError exceptions
        await ctx.send("I was unable to get it")