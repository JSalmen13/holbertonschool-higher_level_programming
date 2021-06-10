#!/bin/bash
# Display HTTP methods that the server will accept
curl -sI -X ALLOW "$1" | sed -n 's/^Allow: //p'
