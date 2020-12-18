#!/bin/bash
# script that takes in a URL and displays all HTTP methods the server will accept
curl -sI "$1" | grep 'Allow: ' | awk '{$1=""; sub(/^[ \t ]+/, ""); print $0}'
