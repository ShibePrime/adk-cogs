
ADK COGS
========

A collection of cogs for the [Red Discord Bot](https://github.com/Cog-Creators/Red-DiscordBot).

crumbl cog
----------

The `crumbl` cog allows users to retrieve information about Crumbl Cookies through the Red Discord Bot. To use the cog, simply enter the `!crumbl` command in a Discord server where the bot has been invited. The bot will then scrape the nutrition information from the Crumbl Cookies website and send an embed with the name, description, and image of a randomly selected cookie variety. The footer of the embed will also display any allergens contained in the cookie.

To install the cog, add `https://github.com/adkcogs/crumbl` to the list of repositories in the Red Discord Bot's `cogs.txt` file. Then run the `!cog install crumbl` command in the Discord server.

Example usage:
--------------

Copy code

`User: !crumbl Bot: [Embed with information about a Crumbl Cookie]`

Dependencies
------------

*   [aiohttp](https://aiohttp.readthedocs.io/en/stable/)
*   [asyncio](https://docs.python.org/3/library/asyncio.html)
*   [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
*   [discord.py](https://discordpy.readthedocs.io/en/latest/)

Contributing
------------

If you have an idea for a cog that you would like to see included in ADK COGS, feel free to open a pull request or issue on the [GitHub repository](https://github.com/adkcogs/adkcogs).
