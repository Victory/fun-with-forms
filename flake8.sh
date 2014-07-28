#!/bin/sh

flake8 --exclude="*pyc,*/migrations/*,db.sqlite3" \
    --max-complexity=5 \
    --statistics \
    funforms/*
RESULT=$?

exit $RESULT