#!/bin/bash
# sudo docker exec -T magellan-db psql -U postgres <<EOF
# drop schema public cascade;
# create schema public;
# EOF

# error: The input device is not a TTY


# cach nay phai truy vao postgres local vi cach tren 
# truy cap vao bash cua psql tren docker ko dc (TTY)
PGPASSWORD=postgres psql -h localhost -p 5422 -U postgres <<EOF
drop schema public cascade;
create schema public;
EOF
pipenv run app