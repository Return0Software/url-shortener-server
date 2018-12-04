#!/usr/bin/env bash

. .env
FLASK_APP=src/url_shortener.py flask run
