#!/bin/bash
#takes url and sends POST req to display the response
curl -s "$1" -X POST -d "email=tests@gmail.com&subject=I will always be here for PLD"