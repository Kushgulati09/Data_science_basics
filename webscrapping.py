#step 0: import the pips for environment
import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"

#step 1: get the html
r= requests.get(url) #gets the content of the website
htmlContent= r.content #converts the content to html content
#print(htmlContent)

#step 2: parse the html
soup = BeautifulSoup(htmlContent, 'html.parser')
#print(soup.prettify())
#prettify takes account of the alignment of the html doc and "()" after the word prettify is imp. 

#step 3: html tree traversal or manipulation 
#commonly used types of objects:
#1) tag
#2) NavigableString
#3) Beautifulsoup
#4) Comment
title = soup.title
#print(type(soup)) #finds and shows what type of soup we used, here, beautifulsoup
#print(type(title)) #shows type of title, i.e. tag
#print(type(title.string)) #shows the type f title string used in the scrapped code

#get the title of the html page
title = soup.title

#get all the paragraphs from the page
paras = soup.find_all('p') #if we used find instead of find_all, it would just print the first par
#print(paras)

#get all anchors tags from the page
#just replace p with a 

#get the text from the tags/soup
#print(soup.find('p').get_text()) #first para text
#print(soup.get_text()) #text from whole soup

#get all the links on the website 
#anchors = soup.find_all('a') #gets all anchor tags and we use this as anchor tag contains links in its href attribute 
#for link in anchors:
    #print(link.get('href')) 
    #now this will only give us the texts of links, and we can't go to the links by clicking on them 
#so, we will modify the code and create an  empty set (set as it would not repeat the repaeting links )
#anchors = soup.find_all('a')
#all_links = set()
#for link in anchors:
    #link_text = "https://codewithharry.com" +link.get('href')
    #print(link_text)
#this will give us clickable links to the website

#4. comment
#markup = "<p><!-- this is a comment--></p>"
#soup2 = BeautifulSoup(markup) #converting the markup into a soup
#print(soup2.p)
#this will show you the comments the coder added in the file we scrapped

#------------------------------------------------------------------------------------------------------------#

#now we can find all the children code under a specific id used in the code, eg. we saw in the inspect option of the website, there's a div
#tag with id imgpreview2 and we want to find all the code under that id tag,

imgpreview2 = soup.find(id = "imgpreview2")
#print(imgpreview2.prettify())

#now if we want to find all the strings in this specific code 

#for item in imgpreview2.strings:
    #print(item)
#we can use similar way to find other specific things
#we want to find the parent of the id code, i.e. what was above it in the code tree

#print(imgpreview2.parent) #we can use parents instead of parent for further up the html tree

#now we want just the name of the parent tags in the order

#for y in imgpreview2.parents:
    #print(y.name) #this will give the order od the tags above it in the document

#now we want to parse the CSS file contents, 
#we want to find the content under the id = loginModal in the css file

#elem = soup.select('#loginModal')                                               #( # inside '' specifies id and . specifies class) 
#print(elem)
