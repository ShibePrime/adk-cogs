import aiohttp
import asyncio
from bs4 import BeautifulSoup
from redbot.core import commands

class SteamID(commands.Cog):
    """Gets a Steam ID from a Discord user."""

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
            response = await self.__session.get(self.__url + str(ctx))
            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')
            div = soup.find('div', class_='#content')
            if div:
                await ctx.send(div.text)
            else:
                await ctx.send("empty")
        except aiohttp.ClientError:
            await ctx.send("I was unable to get it")
