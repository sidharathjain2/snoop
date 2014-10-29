import os, sys, re, time, gzip
import urllib, urllib2, httplib
from BeautifulSoup import BeautifulSoup
from urlparse import urlparse, urlsplit
import StringIO
import mimetypes, mimetools
from ConfigParser import ConfigParser
sys.path.append("../..")
from Crawler import Crawler
import random



class Shaadi(Crawler):
    """
    This class handles crawling and extraction of data from Shaadi.com, a popular site
    for finding and managing matrimonial aliances. It is derived from class Crawler.
    """
    def __init__(self):
        self.__class__.DEBUG = True
        super(Shaadi, self).__init__("../../conf/snoop.cnf", "https://www.shaadi.com/", "https://www.shaadi.com/")
        self.availableCreds = self.loadCredentials("shaadi")


    def doLogin(self, username="", password=""):
        pass


    def conductSearch(self, searchEntity):
        pass


    def buildGraph(self):
        pass


    def parseSearchHtml(self):
        """
        Parses the HTML content in the object's currentPageContent attribute and sets the
        object's 'searchResults' attribute with the resultant dict. Returns the number of
        matches found.
        """
        pass


if __name__ == "__main__":
    searchEntity = sys.argv[1]
    shd = Shaadi()
    pageContent = shd.doLogin()
    if pageContent:
        ff = open("../html/shaadilogin.html", "w")
        ff.write(pageContent)
        ff.close()
    if not shd.assertLogin("Sign Out"):
        print "Could not log in"
        sys.exit()
    else:
        print "Successfully logged in as %s\n"%shd.siteUsername
    shd.conductSearch(searchEntity)
    
