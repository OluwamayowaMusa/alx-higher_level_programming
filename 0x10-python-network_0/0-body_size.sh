#!/bin/bash
# Send request to URL and display the body size
curl -s 0.0.0.0:5000 | wc -c
