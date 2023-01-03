#!/bin/bash
# The possible request methods
curl -I -s "$1" | grep Allow: | cut -d: -f2- | sed 's/^ *\(.*\).*/\1/'
