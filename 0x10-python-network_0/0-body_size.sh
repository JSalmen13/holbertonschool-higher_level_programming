#!/bin/bash
# Body size of the response
curl -so /dev/null -w '%{size_download}\n' "$1"
