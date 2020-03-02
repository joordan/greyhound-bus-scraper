#!/bin/sh

while true
do

	clear
	/usr/bin/python3 /home/administrator/Documents/greyhound-displays/greyhound/greyhound-bus-scraper/scrape.py
	/usr/bin/python3 /home/administrator/Documents/greyhound-displays/greyhound/greyhound-bus-scraper/simplefilter.py

	sleep 300
done
