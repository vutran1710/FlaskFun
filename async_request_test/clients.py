import asyncio
import time
import requests
import aiohttp
import matplotlib.pyplot as plt

begin = time.time()
end_times = []
waiting_after_10s = 0

async def fetch(session, url, task_name):
    global begin
    global end_times
    global waiting_after_10s

    async with session.get(url) as response:
        await response.json()
        if time.time() - begin > 10:
            print("Over 10s")
            waiting_after_10s += 1
        end_times.append(time.time() - begin)


async def main(num):
    global begin
    my_url = 'http://192.168.0.103:5000/api/user/1'
    my_session = aiohttp.ClientSession()
    tasks = [fetch(my_session, my_url, 'task {}'.format(i+1)) for i in range(num)]
    for task in await asyncio.gather(*tasks):
        pass

    requests = [i for i in range (num)]

    fig = plt.figure()
    plt.plot(requests, end_times, marker="o", markersize=0.4)
    plt.xlabel("request")
    plt.ylabel("time")
    fig.savefig('async.png')
    
    global waiting_after_10s
    print(waiting_after_10s)

asyncio.run(main(1000))

