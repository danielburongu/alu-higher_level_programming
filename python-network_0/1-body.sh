#!/bin/bash

#Bash script that sends a GET request to the URL, and displays the body of the response
curl -s "$1" -X GET -L 