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

## Setup

##### Backend
1. Clone the project & `cd` into it

2. Install depedencies
``` shell
$ pipenv install
```

3. Run app
``` shell
$ pipenv run dev
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


- [ ] Writing Error Handler and learning to handle different types of exception in different scenarios

```
1. Write BadRequest Handler
2. Write a Generic Exception Handler
3. Raise Exception instead of returning simple strings
4. Write Test (so I can save time running the development server and sending stupid requests)
5. Document API with text-based REST-Client
```

## Running
1. Build image by using Dockerfile content:
```
sudo docker build -t my-flask-postgres .
```
2. Create a container with name: `some-postgres`
```
sudo docker run --name some-postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d my-flask-postgres
```
3. Run app:
```
pipenv run dev
```
