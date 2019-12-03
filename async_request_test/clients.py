import asyncio
import time
import requests
import aiohttp
import matplotlib.pyplot as plt

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()

async def main(num):
    my_url = 'http://192.168.0.103:5000/api/user/1'
    my_session = aiohttp.ClientSession()
    submits = []
    time_start = []
    consume_time = []
    list_tasks = [fetch(my_session, my_url) for i in range(num)]
    for i in range(num):
        task = asyncio.create_task(list_tasks[i])
        time_start.append(time.time())
        submits.append(task)

    for i in range(num):
      await submits[i]
      print('done task ' + str(i+1) + ' at')
      print(time.time() - time_start[i])
      consume_time.append(time.time() - time_start[i])

    response = [i for i in range(num)]
    plt.plot(consume_time, response)
    plt.show()

asyncio.run(main(440))

