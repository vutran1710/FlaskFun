import asyncio
import time
import requests
import aiohttp
import matplotlib.pyplot as plt

begin = time.time()
start_times = []
end_times = []

async def fetch(session, url, task_name):
    global begin
    print( 'Start time of {} is: {}'.format(task_name, time.strftime("%X")))
    start_times.append(time.time() - begin)
    async with session.get(url) as response:
        return await response.json()

async def main(num):
    global begin
    my_url = 'http://192.168.0.103:5000/api/user/1'
    my_session = aiohttp.ClientSession()
    task_lists = [fetch(my_session, my_url, 'task {}'.format(i+1)) for i in range(num)]

    j = 0
    for task in await asyncio.gather(*task_lists):
        print( 'End time of task {} is '.format(j+1) + time.strftime("%X"))
        end_times.append(time.time() - begin)
        j+=1
    
    responses = [i for i in range (num)]

    fig, ax = plt.subplots()
    ax.scatter(responses, start_times, marker="o", s=0.4)
    ax.set_xlabel("response")
    ax.set_ylabel("time")
    ax.scatter(responses, end_times, marker="o", s=0.4)
    plt.show()


asyncio.run(main(1000))

