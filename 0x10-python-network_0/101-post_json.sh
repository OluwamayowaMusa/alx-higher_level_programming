#!/bin/bash
# Post data to a server using JSON file
curl -s -H "Content-Type: application/json" --data @"$2" "$1"
