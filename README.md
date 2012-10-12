# README

## my.py, a simple web framework

The my.py framework is a mini web framework that aspires to eliminate 
some of the drudgery of working with the many HTML files we will create
throughout the semester. This little script tries to one simple thing 
to make your life better: it creates a simple templating system that 
allows you to use a single HTML template for an infinite number of pages.
Ideally you would put your DOCTYPE, HEAD element, including links to
CSS and Javascript in this One Template to rule them all. When you have
a particular piece of content, my.py would simply insert that content
into your masterfully conceived HTML template. 

__To make this work__

1. You have to follow the rules of the fremework.
2. You have to create the some HTML templates yourself. 
3. my.py will insert the dynamic content the user requests into the template.
4. You can have multiple templates and specify them in the URL.
5. For security's sake templates and dynamic pages are kept out of 
       the web directory and are not directly accessible via a browser.

      
## A TYPICAL my.py URL:

This URL fetches a single html file named lab2.1.html and inserts it into
the One Template

    http://csmcis2.csmcis.com/~YOURNAME/my.py/lab2.1

__How It Works__

1. my.py parses the URL and sees that you want to display lab2.1.html 
       (notice the .html was omitted in the URL for prettiness)
2. my.py finds lab2.1.html and inserts it into a "template" which you
       can use with all of your HTML pages.
3. If lab2.1.htm doesn't exist, my.py show an Error 404 page, which you
       have created just for this occasion.


## TYPICAL URL WITH SPECIFIC TEMPLATE:

my.py can work with multiple templates. You can change the look of all of 
your pages by including the template name in the URL, like this:

### THE TEMPLATE
                                                       |
    http://cmscis2.csmcis.com/~YOURNAME/my.py/lab2.1/gothic

__How It Works__

1. my.py sees that you want to use a template named gothic.html. (Note how we 
       cleverly omitted the .html to keep the URL pretty?)
2. my.py sees that you want to insert the contents of lab2.1.html into the
       your special gothic template that you think is so cool.
3. This means that you have a template named gothic.html in the layouts
       directory.
4. If the URL asks for a template that doesn't exist, my.py uses the
       default.htm template

## OTHER FEATURES:

1. If you request a non-existent layout, you get the default layout.
2. If you request a non-existent HTML page, you get your customized error404.html page.
3. No one can view any of your pages directly: everything goes through my.py
4. All requests are sanitized so that no one can mess with you.


## REQUIREMENTS:

To make this all work, you need to create some directories and some default files:

### DIRECTORIES:

          /home/students/YOURNAME/assets/cis127/layouts/
          /home/students/YOURNAME/assets/cis127/html5/

### FILES: 

          /home/students/YOURNAME/assets/cis127/layouts/default.html
          /home/students/YOURNAME/assets/cis127/html5/index.html
          /home/students/YOURNAME/assets/cis127/html5/error404.html

## EXAMPLE MINIMAL default.html LAYOUT:

You can make your layouts as elaborate as you wish, or as simple.

1. {title} will be filled in automatically
2. {content} will be the HTML page in the URL

        <!doctype html>
        <html lang=en>
        <head>
          <meta charset="utf-8">
          <title>{title}</title> 
        </head>
        {content}

       
## EXAMPLE MINIMAL HTML PAGE

This file would be placed in your HOME/assets/cis127/html5/ directory. 
The title in the comment will be inserted into the HEAD tag. The entire
HTML page will be inserted where the {content} is located.
    
        <!-- title="My Beautiful Web Page" -->
        <h1>Hello, world</h1>

## KNOWN ISSUES

<code>my.py</code> is written in Python3. If you want to print "{}"" characters,
as in an embedded stylesheet, you have to double up the braces, or
you will have fatal errors:

__BAD__

      p {background-color:blue}
        
__GOOD__ 

      p {{background-color:blue}}


## EVERY SOFTWARE PROJECT NEEDS A LICENSE

> LICENSE

> Copyright (C) 2012 Douglas Putnam

> This program is free software: you can redistribute it and/or modify
> it under the terms of the GNU General Public License as published by
> the Free Software Foundation, either version 3 of the License, or
> (at your option) any later version.
> 
> This program is distributed in the hope that it will be useful,
> but WITHOUT ANY WARRANTY; without even the implied warranty of
> MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
> GNU General Public License for more details.
> 
> You should have received a copy of the GNU General Public License
> along with this program.  If not, see <http://www.gnu.org/licenses/>.    

## CONTACT

putnamd@smccd.edu


Keep hacking...

Doug Putnam
