#!/usr/local/bin/python3
# A Mini-web framework
# By Douglas Putnam
# File: my.py
# Date: Tue Sep  4 19:05:57 PDT 2012

""" 

Before operating this machinery, read the README.md file.


"""
#############  my.py at work #################
import os
import cgi
import re
import cgitb

class MyError(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return(repr(self.value))


"""CONFIGURATION ---  ENTER YOUR CSMCIS2 USER NAME"""
username = 'YOUR USERID GOES HERE'
username = 'coolj'

"""CONFIGURATION ---  ENTER YOUR COURSE NAME """
coursename = 'YOUR COURSENAME GOES HERE'
coursename = 'cis127'

try: 
    if username is 'YOUR USERID GOES HERE':
        raise(MyError('You must configure your username before continuing.'))
    if coursename is 'YOUR COURSENAME GOES HERE':
        raise(MyError('You have to configure your coursename before continuing.'))
except Exception as e:
    print(e.value)
    os.sys.exit()


    
cgitb.enable()

params = cgi.FieldStorage()

base =  os.getcwd() + '/'

# Assets are the things your your web site provides:
# HTML, CSS, Javascript, etc.
# Assets are kept out of the web directory, but inside
# of your home directory in a folder names "assets"

assets = os.path.expanduser('~' + username) + '/assets/'

#DIRECTORIES
ASSETS          = assets + coursename + '/'
LAYOUTS         = ASSETS + 'layouts/'
HTML5           = ASSETS + 'html5/'

#FILES
DEFAULT_LAYOUT  = 'default.html'
ERROR_404       = 'error404.html'
DEFAULT_PAGE    = 'index.html'

layout_path = os.path.join(LAYOUTS, DEFAULT_LAYOUT)

try:
    if not os.path.isdir(LAYOUTS):
        raise IOError('Missing directory')
except IOError:
    print("Cannot open the layouts directory: " + LAYOUTS)
    print("Create the layouts directory: " + LAYOUTS + " and try again.")
    print("Then, create the default directory: " + DEFAULT_LAYOUT)
    print("Log in to the server and run this command: mkdir -p ~/assets/" + coursename + """/{layouts,html5}""")
    os.sys.exit()

try:
    if not os.path.isfile(layout_path):
        raise IOError('Missing default layout: ' + DEFAULT_LAYOUT)
except IOError:
    print("Then, create the default layout: " + DEFAULT_LAYOUT)
    os.sys.exit()

    
#################### END OF SETUP #######################


# Is there some special instruction in the URL?
# http://csmcis2.csmcis.com/~yourname/my.py/page_name/layout_name
# Omit the .html

page = DEFAULT_PAGE

message404 ="The page you are looking for is not available."

if 'PATH_INFO' in os.environ.keys():
    parts = os.environ['PATH_INFO'].split('/')
    parts = [ i for i in parts if i != '']
    if parts:
        page = cgi.escape(parts[0]) + '.html'
        if page == 'sitemap.html':
            page="error404.html"
            message404 = 'The sitemap is not available.'

        if not os.path.isfile(HTML5 + page):
            page = ERROR_404

        if len(parts) > 1:
            layout_path = os.path.join(LAYOUTS,cgi.escape(parts[1])) + '.html'
            if not os.path.isfile(layout_path):
                layout_path = os.path.join(LAYOUTS, DEFAULT_LAYOUT)

layout = open(layout_path,'r').read()
content = open(HTML5 + page,'r').read()
if page == 'error404.html':
    content = content.format(content=message404)

res = re.search('<!--\s*title="?([^"]*)"?\s*-->',content)
title = page
if res:
    title = res.group(1)


#################### START OUTPUT #######################


# Must have a Content-type
print('Content-type: text/html\n')

print(layout.format(title=title,content=content))
