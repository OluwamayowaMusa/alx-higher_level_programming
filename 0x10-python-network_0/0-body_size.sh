#!/bin/bash
# Send request to URL and display the body size
curl -s "$1" | wc -c
