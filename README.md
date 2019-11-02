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
$ STAGE=test pipenv run test
# should fix this: no need inject stage manually, test code should inject the STAGE automatically
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

## Running
- Firstly, You need to create a `.env` file at root path. And then add `APP_CONFIG_DEV_FILE` and `APP_CONFIG_TEST_FILE` as 2  environment variables.
```
APP_CONFIG_DEV_FILE = /home/.../magellan/config/development.py
APP_CONFIG_TEST_FILE = /home/.../magellan/config/staging.py
```
- And then edit 3 following lines in the file `instance/config.py` by your own email address and password.
```
MAIL_USERNAME = 'your-email'
MAIL_PASSWORD = 'your-password'
MAIL_DEFAULT_SENDER = 'your-email'
```

After that run following commands to run the app:
1. Build docker-compose
```
sudo docker-compose up -d
```
2. Run test:
```
pipenv run test
```
3. Run app:
```
pipenv run dev
```
