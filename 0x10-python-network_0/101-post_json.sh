#!/bin/bash
# script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response
curk -d "@$2" -H 'Content-Type: application/json' "$1"
