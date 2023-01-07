import asyncio
from redbot.core import commands

class note(commands.Cog):
    """sets a note on Shibe's desk screen."""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


    def cog_unload(self) -> None:
        if self.__session:
            asyncio.get_event_loop().create_task(self.__session.close())

@commands.command()
async def note(self, ctx: commands.Context, subcommand: str, *, words: str = None) -> None:
    if subcommand == "set":
        with open(r"~\home\pi\notes.txt", "w") as f:
            f.write(words + "\n")
            await ctx.send("Notes have been set.")
    elif subcommand == "get":
        try:
            with open(r"~\home\pi\notes.txt", "r") as f:
                notes = f.read()
                if not notes:
                    await ctx.send("No notes have been set.")
                else:
                    await ctx.send(notes)
        except FileNotFoundError:
            await ctx.send("No notes have been set.")
    else:
        await ctx.send("Invalid subcommand. Use `set` or `get`.")