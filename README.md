# codesamples-python3-gevent-site-parser
Gevent site parser
# Description
1. Site parser for news.ycombinator.com should parse main page and comments page - also includes allowed clicks option in order not to hammer the site with requests too much. Configuration script should be run once per 2 days - enough time for the domain to accumulate decent amount of items on each page
2. Site news.ycombinator.com is a tough domain - actually second this harsh in my practice after non-esitent now Monarch Flights site - after 10-15 concurrent attempts to connect the site - it will send the given IP in ban and for several hours showing 403 - so potential clicks on "More" button are limited to 3 + 1 for start page
3. Main page of the news.ycombinator.com seem to be the same as news page of the site mentioned so used it as well in a form of news?p=1 to speed the development
4. Since from my end news.ycombinator.com only allows 10-15 connections/requests at the same and very small period of time - proxy usage implemented ina script and a standard proxies IPs were used, if connection to news.ycombinator.com is faster from your end and you have a better proxy in your disposal you can edit the config.ini file via ./codesamples-python3-gevent-site-parser/config/config.ini and change the value of clicksallowed from 3 to infinity, but also, please change proxylist to the list of better proxy servers in your disposal otherwise you may lost access to the news.ycombinator.com site with 403 error
5. During tests I safely changed clicksallowed value up to 10 with the proxylist mentioned in the file just limited it to 3 + 1 for starting page of each site section in order to be polite to the site community and not get 403 accidentally
6. Configuration of the crawler get the list of the pages for each site section (main, comments) based on athing class on the very first page (last commentary in current minute) or page 1 (for main/news page) in single thread mode, because Greelets can not communicate like Goroutines (threads in Golang) do - this means I am unable to pass the values between Greenlets on the fly(like in Go) and unable to finish them based on the results of each of them (for example if we reach the anticipated end with one Greenlet - this is possible on Python too (or at least the same results), but require more time for development which we need to skip due to urgency of the interview. Plus the cofiguration is actual only once in 2 days (with that speed pages of the news.ycombinator.com) being updated - for example to me the pages of the news.yocmbinator.com still contain almost the same items as for yesterday (January 22nd 2021 vs January 23rd 2021) and the last page is within the same boundaries.
7. Normal crawling for links is - according to the task description - is implemented using gevent module - and can display results on screen(all of them - huge amount) or to store them into json output
# Limitations
1. Single thread config - can be fixed in the future require some time to re-implement
2. Proxy module is used, but for better results Tor module should be used as this implementation provides better anonymity and random IPs for each request. Not implemented because it would include additional modules to deployment for at least sock5 support and Tor itself support and would require to restart Tor server each time on local machine where the script is going to run
3. Requests with Sessions could also be used to avoid the issue with limiting concurrenct connections and to use ability to log into news.ycombinator.com, which also may enable us to use more concurrent connections to the site in a given time period (registered users may have better access conditions to the news.ycombinator.com site)
4. Proxies with better connection speed may be used
5. One (n * n) loop can be re-implemented to threads-style loop, which is currently not part of the task
6. It is possible to make the Crawler a little more generic and scallable, however, at the moment you it seems possible to add new site sections to the config.ini, but for a single domain mentioned in the global section of the config.ini
# Possible modifications
1. Multi-thread'ed config mode - need to invent/find a way to communicate between Gevent Greenlets
2. (n * n) loop to multi threaded loop
3. Proxy requests to Tor-styled requests
4. Enable possibility for the Crawler to be scalable on a terms of how many pages/site it can crawl - all of those should be changed/added in config.ini
# Please kindly note that modifications were not initially mentioned in the task description (see below) and due to urgency of the interview were not implemented to safe time of development
# Terms
1. Pages - part of pagination "More" menu at the bottom of main page and comments page on news.ycombinator.com
2. Site sections - aforementioned main page and comments page on news.ycombinator.com
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
9. [optiona] edit the config.ini, if needed, via ./codesamples-python3-gevent-site-parser/config/config.ini
10. [optional] deactivate
# How to run?:
1. python run_parser.py -h - will provide help information
2. python run_parser.py -c - will configure parser in single thread mode
3. python run_parser.py -r - will crawl the site in gevent/multithread mode
4. there also additional options - only running alongside with the with the -r option:
5. python run_parser.py -r -v - view the results on screen (huge list so increase output limits in your Linux shell/PUTTY)
6. python run_parser.py -r -s - will store the results into ./codesamples-python3-gevent-site-parser/output/ separetelly for each site section
7. options in points 4,5,6 can be combined as follows: python run_parser.py -r -v -s so the script will be able to both display the results and store them
8. You also can use a BASH script included ./menu.sh to see some fucntions organized in a menu
# Task Description
Write a webcrawler using python that crawls a single domain. For example,
given the URL 'news.ycombinator.com', it should crawl the main page and the
comments, but not any external links. After finishing crawling the program
it should print the links between pages.

The goal is to make the crawler work as fast as possible by using `gevent`.
