# Training Week 1
- Basic Web Development
- Setup
- Basic API Development

# Training Week 2
- Code Quality
- HTTP Status & Error Handling
- Testing
- API Documentation
- Docker experience and setting up Database

# Training Week 3
- Higher-Order Function and Decorator
- Registration and Mailer
- Authentication with JWT

--

## Setup

##### Backend
1. Clone the project & `cd` into it

2. Install depedencies
``` shell
$ pipenv install
```

3. Run app
``` shell
$ pipenv run app
```

 Note: on production, run `STAGE=production pipenv run app`, or staging using same format with different STAGE

4. Run test

``` shell
pipenv run test
```

## Tasks

- [x] Writing simple `Stateful Backend` that has APIs to support multiple methods `GET, PUT, POST, DELETE`
```
1. Declare a `global` dict namely RESULT
2. Write a GET api with query-param as one of RESULT's keys to return its corresponding value in plain text-format
3. Write a PUT api to add more key to RESULT with default value being an empty string
4. Write a POST api to add more than one keys and values to the RESULT dict
5. Write a DELETE api to delete a single key of RESULT dict
6. Write a PATCH api to update a specific key of RESULT dict
```


- [x] Writing Error Handler and learning to handle different types of exception in different scenarios

```
1. Write BadRequest Handler
2. Write a Generic Exception Handler
3. Raise Exception instead of returning simple strings
4. Write Test (so I can save time running the development server and sending stupid requests)
5. Document API with text-based REST-Client
```

- [ ] Registration & Authentication Strategy

```
1. Re-design User Schema
2. Write Public API for User Registration
3. Send email to newly registered user for Activation Request
4. Write Public API for User Login, authenticated using JWT
```

# Experiment
## Purpose
## Theoretical Basis
## Preparing
We could use an another computer or a virtual machine (PC2)

### gunicorn

Gunicorn takes care of everything which happens in-between the web server and your web application. This way, when coding up your a Django application you don’t need to find your own solutions for:

- communicating with multiple web servers
- reacting to lots of web requests at once and distributing the load
- keeping multiple processes of the web application running

```console
pipenv run gunicorn --worker-class=gevent --worker-connections=1000 --workers=9 --bind=192.168.0.103:5000  app:app

```
## Process

To conduct this experiment by the following way:
- Send 1000 request from PC1 to PC2 (where the app located; using the script at PC2:
```python
import asyncio
import time
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

```
- So we need import :
    - aiohttp: to create a session for a client to make requests and responses become coroutines
    - asyncio: to help manipulate coroutines, the coroutines are automatically scheduled to run soon with `asyncio.create_task() `
    - matplotlib: to plot (requests, time)
## Result
## Conclusion
## Future Improvments