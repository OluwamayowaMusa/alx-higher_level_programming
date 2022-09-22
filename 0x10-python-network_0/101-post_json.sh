#!/bin/bash
# Post data to a server using JSON file
curl -H "Content-Type: application/json" --data @"$2" "$1"
