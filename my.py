#!/usr/local/bin/python3
# A Mini-web framework
# By Douglas Putnam
# File: my.py
# Date: Tue Sep  4 19:05:57 PDT 2012

""" 
Before operating this machinery, read the README.md file that came with the file.

"""
#############  my.py at work #################

import os
import cgi
import re
import cgitb
cgitb.enable()

params = cgi.FieldStorage()
base =  os.getcwd() + '/'

"""CONFIGURATION ---  ENTER YOUR CSMCIS2 USER NAME"""
username = 'YOUR USERID GOES HERE'
username = 'coolj'

"""CONFIGURATION ---  ENTER YOUR COURSE NAME """
coursename = 'YOUR COURSENAME GOES HERE'
coursename = 'cis127'


class ConfigurationException(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return(repr(self.value))

try: 
    if username is 'YOUR USERID GOES HERE':
        raise(ConfigurationException('You must configure your username before continuing.'))
    if coursename is 'YOUR COURSENAME GOES HERE':
        raise(ConfigurationException('You have to configure your coursename before continuing.'))
except Exception as e:
    print(e.value)
    os.sys.exit()


# Assets are the things your your web site provides:
# HTML, CSS, Javascript, etc.
# Assets are kept out of the web directory, but inside
# of your home directory in a folder names "assets"
assets = os.path.expanduser('~' + username) + '/assets/'

#DIRECTORIES
ASSETS          = assets
LAYOUTS         = ASSETS + 'layouts/'
HTML5           = ASSETS + 'cis127/'

#FILES
ERROR_404          = 'error404.html'
DEFAULT_CONTROLLER = 'default'
DEFAULT_PAGE       = 'index.html'
DEFAULT_LAYOUT     = 'default.html'

"""You need this directory structure """

dirstructures = """<pre>
$HOME/assets/
           :---layouts/
           :         :---default.html
           :
           :---default/
           :          :---index.html
           :          :---error404.html
           :          :---and any other HTML files you want
           :
           :---solutions/
                        :---index.html
                        :---week1.html
                        :---week2.html
                        :---weekn.html

</pre>
"""

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
        raise IOError('Missing default layout: ' + LAYOUT)
except IOError:
    print("Then, create the default layout: " + LAYOUT)
    os.sys.exit()

    
#################### This Part Does All The Work #######################

# Look for a special instruction in the URL.
# http://csmcis2.csmcis.com/~yourname/my.py/PAGE_name/layout_name
# Omit the .html

# default values for CONTROLLER, PAGE, template 
CONTROLLER = DEFAULT_CONTROLLER
LAYOUT     = DEFAULT_LAYOUT
PAGE       = DEFAULT_PAGE

message404 ="The PAGE you are looking for is not available."

if 'PATH_INFO' in os.environ.keys():
    parts = os.environ['PATH_INFO'].split('/')
    parts = [ i for i in parts if i != '']


    if parts:
        if len(parts) is 1:
            CONTROLLER = DEFAULT_CONTROLLER
            LAYOUT     = DEFAULT_LAYOUT
            PAGE       = parts[0]
        if len(parts) is 2:
            CONTROLLER = parts[0]
            PAGE = parts[1]
        elif len(parts) is 3:
            CONTROLLER = parts[0]
            PAGE       = parts[1]
            LAYOUT     = parts[2]


        if not os.path.isdir(os.path.join(ASSETS,CONTROLLER)):
            CONTROLLER = DEFAULT_CONTROLLER
            PAGE = ERROR_404
            layout_path = os.path.join(LAYOUTS, DEFAULT_LAYOUT)
        else:
            PAGE = cgi.escape(PAGE) + '.html'
            layout_path = os.path.join(LAYOUTS, LAYOUT)

            if PAGE == 'sitemap.html':
                files = os.listdir(os.path.join(ASSETS,CONTROLLER))
                names = []

                for file_name in files:
                    if os.path.isdir(os.path.join(ASSETS,CONTROLLER,file_name)): continue
                    names.append("<a href='/~{username}/my.py/{controller}/{filename1}'>{filename2}</a>".format(controller=CONTROLLER,username=username,filename1=file_name[:-5],filename2=file_name[:-5]))

                sitemap_links = "<ul><li>" + "</li><li>".join(names) + "</li></ul>"

            if not os.path.isfile(os.path.join(ASSETS,CONTROLLER,PAGE)):
                PAGE = ERROR_404

            if len(parts) > 1:
                layout_path = os.path.join(LAYOUTS,LAYOUT) + '.html'
                if not os.path.isfile(layout_path):
                    layout_path = os.path.join(LAYOUTS, DEFAULT_LAYOUT)

layout = open(layout_path,'r').read()
content = open(os.path.join(ASSETS,CONTROLLER,PAGE),'r').read()

# insert the Error Message
if PAGE == 'error404.html':
    content = content.format(content=message404)

# insert the sitemap links
if PAGE == 'sitemap.html':
    content = content.format(sitemap_links=sitemap_links)

# Extract the title from the HTML PAGE
res = re.search('<!--\s*title="([^"]*)"\s*-->',content)
title = PAGE[:-5]
if res:
    title = res.group(1)


#################### START OUTPUT #######################


# Must have a Content-type
print('Content-type: text/html\n')

print(layout.format(title=title,content=content,sitemap_link=CONTROLLER))

"""
<h2>
<a name="every-software-project-needs-a-license" class="anchor" href="#every-software-project-needs-a-license"><span class="mini-icon mini-icon-link"></span></a>EVERY SOFTWARE PROJECT NEEDS A LICENSE</h2>

<blockquote>
<p>LICENSE</p>

<p>Copyright (C) 2012 Douglas Putnam</p>

<p>This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.</p>

<p>This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.</p>

<p>You should have received a copy of the GNU General Public License
along with this program.  If not, see <a href="http://www.gnu.org/licenses/">http://www.gnu.org/licenses/</a>.    </p>
</blockquote>

<h2>
<a name="contact" class="anchor" href="#contact"><span class="mini-icon mini-icon-link"></span></a>CONTACT</h2>

<p><a href="mailto:putnamd@smccd.edu">putnamd@smccd.edu</a></p>
"""

