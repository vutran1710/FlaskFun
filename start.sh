#!/bin/bash
ps aux | grep magellan | awk '{print $2}' | xargs sudo kill -9
pipenv run app