#!/usr/local/bin/python3
# A Mini-web framework
# By Douglas Putnam
# File: my.py
# Date: Tue Sep  4 19:05:57 PDT 2012

""" 
The my.py framework 

Use this mini web framework to reduce some of the repetitive and non-productive
aspects of working with HTML. This little script does one thing to make your
life better: it creates a simple templating system that allows you to use the 
same HTML template for many pages. 

    1) You create the HTML templates.
    2) my.py inserts the dynamic content into the template.
    3) You can have multiple templates and specify them in the URL.
    4) Templates and dynamic pages are kept out of the web directory and are
       not directly accessible via a browser.

TYPICAL URL:

    http://csmcis2.csmcis.com/~YOURNAME/my.py/lab2.1

  How It Works -

    1) my.py parses the URL and sees that you want to display lab2.1.html 
       (notice the .html was omitted for prettiness)
    2) my.py finds lab2.1.html and inserts it into a "template" which you
       can use with all of your HTML pages.
    3) By using a template, you can change the look of all of your pages by
       simply changing the HTML in the template, and all of your pages will
       inherit the changes.

TYPICAL URL WITH SPECIFIC TEMPLATE:

    http://cmscis2.csmcis.com/~YOURNAME/my.py/lab2.1/gothic

  How It Works -

    1) my.py sees that you want to insert the contents of lab2.1.html into the 
       your special goth template that you think is cool.
    2) This means that you have a template named gothic.html in the layouts
       directory.

OTHER FEATURES:

    1) If you request a non-existent layout, you get the default layout.
    2) If you request a non-existent HTML page, you get your customized error404.html page.
    3) No one can view any of your pages directly: everything goes through my.py
    4) All requests are sanitized so that no one can mess with you.

REQUIREMENTS:

    To make this all work, you need to create some directories and some default
    files:

        DIRECTORIES:

          /home/students/YOURNAME/assets/cis127/layouts/
          /home/students/YOURNAME/assets/cis127/html5/

        FILES: 

          /home/students/YOURNAME/assets/cis127/layouts/default.html
          /home/students/YOURNAME/assets/cis127/html5/index.html
          /home/students/YOURNAME/assets/cis127/html5/error404.html

EXAMPLE MINIMAL default.html LAYOUT:

    You can make your layouts as elaborate as you wish, or as simple.

    1) {title} will be filled in automatically
    2) {content} will be the HTML page in the URL

        <!doctype html>
        <html lang=en>
        <head>
          <meta charset="utf-8">
          <title>%s</title> 
        </head>
        {content}

       
EXAMPLE MINIMAL HTML PAGE
    The title in the comment will be inserted into the HEAD tag. 
    
        <!-- title="My Beautiful Web Page" -->
        <h1>Hello, world</h1>

KNOWN ISSUES

    my.py is written in Python3. If you want to print "{}"" characters,
    as in an embedded stylesheet, you have to double up the braces, or
    you will have fatal errors:

        BAD: p {background-color:blue}
        
        GOOD: p {{background-color:blue}}

Keep hacking...

Doug Putnam

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

message ="The page you are looking for is not available."

if 'PATH_INFO' in os.environ.keys():
    parts = os.environ['PATH_INFO'].split('/')
    parts = [ i for i in parts if i != '']
    if parts:
        page = cgi.escape(parts[0]) + '.html'
        if page == 'sitemap.html':
            page="error404.html"
            message = 'The sitemap is not available.'

        if not os.path.isfile(HTML5 + page):
            page = ERROR_404

        if len(parts) > 1:
            layout_path = os.path.join(LAYOUTS,cgi.escape(parts[1])) + '.html'
            if not os.path.isfile(layout_path):
                layout_path = os.path.join(LAYOUTS, DEFAULT_LAYOUT)

layout = open(layout_path,'r').read()
content = open(HTML5 + page,'r').read()
if page == 'error404.html':
    content = content.format(content=message)

res = re.search('<!--\s*title="?([^"]*)"?\s*-->',content)
title = page
if res:
    title = res.group(1)


#################### START OUTPUT #######################


# Must have a Content-type
print('Content-type: text/html\n')

print(layout.format(title=title,content=content))
