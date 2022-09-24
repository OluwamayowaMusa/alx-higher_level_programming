#!/bin/bash
# A request to the 0.0.0.0:5000/catch_me
curl -sL -X PUT -d "user_id=98" 0.0.0.0:5000/catch_me
