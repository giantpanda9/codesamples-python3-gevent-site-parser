# codesamples-python3-gevent-site-parser
Gevent site parser
# Description
Site parser for news.ycombinator.com should parse main page and comments page - also includes allowed clicks option in order not to hammer the site with requests too much. Configuration script should be run once per 2 days - enough time for the domain to accumulate decent amount of items on each page
# Purposes
To demonstrate ability to work with Gevent and multithreading pn Python 3.x
# Requirements
1. Python 3.x
2. virtualenv gevent, lxml, requests, configparser, optparse and dependencies
3. Linux OS - tested on Ubuntu 18.04
4. news.ycombinator.com to be in healthy state
# Installation instructions (approximate, not the last ones to follow):
1. git clone this project
2. sudo pip3 install virtualenv
3. cd codesamples-python3-gevent-site-parser
4. pip install gevent
5. pip install lxml
6. pip install requests
7. pip install configparser
8. [optional] pip install optparse
9. Edit the config.ini, if needed, via ./codesamples-python3-gevent-site-parser/config 
# How to run?:
1. python run_parser.py -h - will provide help information
2. python run_parser.py -c - will configure parser in single thread mode
3. python run_parser.py -r - will crawl the site in gevent/multithread mode
4. there also additional options - only running alongside with the with the -r option:
5. python run_parser.py -r -v - view the results on screen (huge list so increase output limits in your Linux shell/PUTTY)
6. python run_parser.py -r -s - will store the results into ./codesamples-python3-gevent-site-parser/output/ separetelly for each site section
7. options in points 4,5,6 can be combined as follows: python run_parser.py -r -v -s so the script will be able to both display the results and store them
8. You also can use a BASH script included ./menu.sh to see some fucntions as part of menu

