import json
import asyncio
import websockets
import random
import string
from websockets.exceptions import ConnectionClosedOK
from redbot.core import commands

server = "10.101.69.2"
port = "8080"


def generate_random_hash():
    letters = "abcdefghijklmnopqrstuvwxyz0123456789"
    return ''.join(random.choice(letters) for _ in range(9))


class ShibeAI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def shibeai(self, ctx, *, context: str):
        session = generate_random_hash()
        response = await self.process_message(context, session)
        if response:
            await ctx.send(response)
        else:
            await ctx.send("An error occurred while processing your request.")


    async def process_message(self, context, session):
        task1 = asyncio.ensure_future(self.send_message_to_fn12(context, session))
        task2 = asyncio.ensure_future(self.send_message_to_fn13(context, session))

        await asyncio.gather(task1, task2)

        return task2.result()

    async def send_message_to_fn12(self, context, session):
        async with websockets.connect(f"ws://{server}:{port}/queue/join") as websocket:
            while True:
                content = json.loads(await websocket.recv())

                if content["msg"] == "send_hash":
                    await websocket.send(json.dumps({"session_hash": session, "fn_index": 12}))
                elif content["msg"] == "send_data":
                    await websocket.send(json.dumps({"session_hash": session, "fn_index": 12, "data": [context]}))
                elif content["msg"] == "process_generating":
                    pass
                elif content["msg"] == "process_completed":
                    return True

    async def send_message_to_fn13(self, context, session):
        async with websockets.connect(f"ws://{server}:{port}/queue/join") as websocket:
            while True:
                try:
                    content = json.loads(await websocket.recv())
                except ConnectionClosedOK:
                    print("WebSocket connection closed gracefully")
                    break

                if content["msg"] == "send_hash":
                    await websocket.send(json.dumps({"session_hash": session, "fn_index": 13}))
                elif content["msg"] == "send_data":
                    await websocket.send(json.dumps({"session_hash": session, "fn_index": 13, "data": [
                        None, 200, True, 1.99, 0.18, 1, 1.15, 1, 30, 0, 0, 1, 0, 1, False, False, "User", "ShibeBot",
                        "ShibeBot is a helpful assistant that tries its best to help User. ShibeBot never gives any personal information except his name. If User asks for an Image, Picture or Painting of something ShibeBot replies with IMAGE: and the description of the image ALWAYS.",
                        False, 2048, 1,
                    ]}))
                elif content["msg"] == "process_generating":
                    pass
                elif content["msg"] == "process_completed":
                    data = content["output"]["data"]
                    if "choices" in data[0]:
                        chosen_model = data[0]["choices"][0]
                        continue

                    return data[0][-1][-1]