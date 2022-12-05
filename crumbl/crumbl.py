import aiohttp
import asyncio
from bs4 import BeautifulSoup
from redbot.core import commands
import discord

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
                for b in cookies:
                    titles = b.find_all("b", {"class": "text-lg"})
                    desc = b.find_all("p", {"class": "text-sm"})
                    contains = b.find_all("span", {"class": "flex items-center justify-center"})
                    thumb_url = b.find_all('img', {"class": "object-contain"})
                    for b in titles:
                        embed = discord.Embed(title=b.text)
                        for b in desc:
                            embed.add_field(name='Description', value=b.text, inline=False)
                            for b in contains:
                                embed.set_footer(text=b.text.split("\n"))
                                for b in thumb_url:
                                    thumb_url="https://crumbl.video/cdn-cgi/image/width=1920,quality=80/https://crumbl.video/a5f42017-e326-401d-a892-2b683b399345_SeaSaltToffee_Aerial_Tech.png"
                                    embed.set_thumbnail(url=thumb_url)
                                    await ctx.send(embed=embed)

        except aiohttp.ClientError:
            await ctx.send("I was unable to get cookies.")
