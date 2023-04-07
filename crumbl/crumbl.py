import aiohttp as E,asyncio as B
from bs4 import BeautifulSoup as F
from redbot.core import commands as A
import discord as G
class crumbl(A.Cog):
	def __init__(A,*B,**C):super().__init__(*B,**C);A.__url='https://crumblcookies.com/nutrition';A.__session=E.ClientSession()
	def cog_unload(self):
		if self.__session:
			B.get_event_loop().create_task(self.__session.close())
	@A.command()
	async def crumbl(self,ctx):
		D='class';C=ctx;await C.trigger_typing()
		try:
			async with self.__session.get(self.__url)as H:
				I=await H.text();J=F(I,'html.parser');K=J.find_all('div',class_='bg-white p-5 pb-0 mb-2.5 rounded-lg')
				for A in K:
					L=A.find_all('b',{D:'text-lg'});M=A.find_all('p',{D:'text-sm'});N=A.find_all('img',{D:'object-contain'});O=A.find_all('span',{D:'flex items-center justify-center'})
					for A in L:
						B=G.Embed(title=A.text)
						for A in M:
							B.add_field(name='Description',value=A.text,inline=False)
							for A in N:
								B.set_thumbnail(url=A['src'])
								for A in O:B.set_footer(text='Contains '+A.get_text(separator=' '));await C.send(embed=B)
		except E.ClientError:await C.send('I was unable to get cookies.')