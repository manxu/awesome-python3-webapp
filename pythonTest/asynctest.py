import asyncio

async def hello():
	for i in range(0,100):
		print('hello %s' % i)
	r=await asyncio.sleep(0.2)
	print('again')

async def no():
	for i in range(0,10000):
		print('no %s' % i)
	r=await asyncio.sleep(1)
	print('againno')
async def no1():
	for i in range(0,10000):
		print('no1 %s' % i)
	r=await asyncio.sleep(1)
loop=asyncio.get_event_loop()
tasks=[no1(),no(),hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()