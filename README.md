# Sample-Web-Scraper
#////////////////////////////////////////////////////////////////////////
#// AutobotStover.py - Web Scraper                                    //
#// Language: Python 2.7, VISUAL STUDIO 2015                         //
#// ver 1.0                                                         //
#// Author: Rajesh Ramesh, Summer Intern 2017                      //
#// Application: Analytics Project for Jivox                      //
#// Platform: Apple Macbook Pro 2015, Windows 10                 //
#/////////////////////////////////////////////////////////////////
#/*
# * Package Operations:
#  -------------------
# * This package initially scrapes URLs of articles based on the search term
#   and stores them in a csv file.
#
# * The website needs to be regularly visited to check if new pages/articles
#   are added. If changes in page numbers are observed, the necessary changes have 
#   to be made in line number - 73
#
# * Once all the articles URLs are scraped and stored in the csv file, each URL is 
#   accessed and the respective article is scraped and stored in a text file.
#
# * The text file must be finally fed into the Sentiment Analysis API for further processing.
#
# * Required Packages:
# * -------------------
# * csv, lxml, sleep, requests, urllib, urllib2, random, beautifulsoup
# *   
# * Maintenance History:
# * --------------------
# * ver 1.0 : 11 Aug 2017
# * - first release
#
# Tip: The program takes a very long time to run if page numbers are more than 500
#     It is recommended to scrape a set of pages and proceed accordingly
#
# Additional Note: The same code can be used for other websites with few modifications
#                 after studying the elements of the website.
#
