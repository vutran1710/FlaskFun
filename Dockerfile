FROM postgres:alpine

MAINTAINER SonNguyen<n.vanson.2201@gmail.com>

WORKDIR /

RUN pipenv install

RUN sudo docker run --name postgres -0 POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres:alpine

RUN pipenv run dev

EXPOSE 5432


