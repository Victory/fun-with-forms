#!/bin/sh

flake8 --exclude="*pyc,*/migrations/*,db.sqlite3" \
    --max-complexity=5 \
    --statistics \
    slim/*
RESULT=$?

exit $RESULT