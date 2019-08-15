
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

########################################################

# Required pre-defined packages                        #

########################################################
import csv
from lxml import html
import lxml
from time import sleep
import requests
from bs4 import BeautifulSoup
import urllib
import urllib2 
from random import randint

outputFile = open("All_linksDIGMAKTFULL.csv", 'wb')  # csv file that holds all the scraped article URLs
fileWriter = csv.writer(outputFile)

fileWriter.writerow(["Link"])
#fileWriter.writerow(["Sl. No.", "Page Number", "Link"])

url1 = 'https://www.marketingweek.com/page/'   #Basic URL
url2 = '/?s=digital+marketing'                 #Search term

sl_no = 1

#######################################################################################
# Approximately 12-15 articles on each page                                           #                                                                #
# DIGITAL MARKETING - 1098 PAGES                                                      #
# DIGITAL ADVERTISING - 534 PAGES                                                     #
# ARTIFICIAL INTELLIGENCE - 14 PAGES                                                  #                                                              #
# MACHINE LEARNING - 166 PAGES                                                        #
# DIGITAL MARKETING FUTURE - 261 PAGES                                                #
# DIGITAL ADVERTISING FUTURE - 144 PAGES                                              #
#######################################################################################

#iterating from 1st page through nth page
for i in xrange(1, 1098):                #Pg number varies for each topic

    #generating final url to be scraped using page number
    url = url1 + str(i) + url2

    #Fetching page
    response = requests.get(url)
    sleep(randint(3, 5))
    #using html parser
    htmlContent = html.fromstring(response.content)

    #Capturing all 'a' tags under h2 tag with class 'hentry-title entry-title'
    page_links = htmlContent.xpath('//div[@class = "archive-constraint"]//h2[@class = "hentry-title entry-title"]/a/@href')
    for page_link in page_links:
        print page_link
        fileWriter.writerow([page_link])
        sl_no += 1
########################################################################################

with open('All_linksDIGMAKTFULL.csv', 'rb') as f1:   #Each line in the csv file is read and the respective article is scraped
    reader = csv.reader(f1)
    next(reader)

    for line in reader:
        url = line[0]       
        soup = BeautifulSoup(urllib2.urlopen(url),"lxml")

        with open('LinksOutputDIGMAKTFULL.txt', 'a+') as f2:    #Scraped articles are stored in a text file
            for tag in soup.find_all('p'):
                f2.write(tag.text.encode('utf-8') + '\n')   
 
##########################################################################################      