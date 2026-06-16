'''
1) Using the requests module, create the function fetch_html that takes two arguments (URL and headers), sends a GET request to 
https://www.gutenberg.org/cache/epub/11/pg11-images.html, and returns a string containing the HTML of the webpage. Store in a variable 
called "html" and print the first 598 characters.'''
import requests

def fetch_html(url, header):
    response = requests.get(url, headers= header)
    html = response.text
    return html

url = f'https://www.gutenberg.org/cache/epub/11/pg11-images.html'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36'}
html = fetch_html(url, header)
#print(html[:599])


'''
2) Using the BeatufilSoup module, parse the html using the lxml parser to create a BeautifulSoup object. After creating your object, 
spend a few minutes exploring the structure of the page. Print characters 5078 through 10212 of a prettified version of the html, as 
well as the title of the page, and the first 1000 characters of all text on the page. Next, inspect the first 3 occurrences of the <p> 
tag and print them. Finally, print the first 10 text nodes that are not empty.'''
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "lxml")
pretty = soup.prettify()[5078:10213]
#print(pretty)
#print(soup.title)
#print(soup.text[:1001])
#print(soup.find_all('p')[4])


'''
3) Locate the <img> tag for the book's cover illustration and print the entire <img> tag along with its "id" attribute and its "src" 
attribute. If the value of "src" does NOT begin with "http", then it is a relative URL. Inspect the page URL to determine the directory 
that the HTML file lives in, and use that directory as your base URL. Assign this directory to a variable called base_url. Construct the 
full image URL by combining base_url with the src value, then download the image bytes.'''
cover = soup.find('img')
#print(cover)
id = cover.get('id')
#print(id)
src = cover.get('src')
base_url = f'https://www.gutenberg.org/cache/epub/11/'
img_url = base_url + src
#print(img_url)
img_data = requests.get(img_url).content


'''
4) Inspect the HTML to find which tags are used for chapter headings and which tag is used for paragraphs. Write a function that takes: 
the chapter heading tag name, the paragraph tag name, a chapter label, and a paragraph number, and returns the corresponding paragraph 
element from that chapter. Then call your function to print paragraph 4 of chapter 4. After extracting the paragraph, italicize every third 
word (wrap them in * *). Finally, print the cleaned/manipulated paragraph to the terminal.'''

def fetch_paragraph(ctag, ptag, cnum, pnum):
    chapter_heading = soup.find(lambda tag: tag.name == ctag and cnum in tag.get_text())
    if chapter_heading is None:
        raise ValueError(f'Could not find chapter heading with the text {cnum}')
    paragraphs = []
    for tag in chapter_heading.find_all_next():
        if tag.name == ctag: 
            break
        if tag.name == ptag:
            paragraphs.append(tag.get_text())
    return paragraphs[pnum-1]

ctag = 'h2'
ptag = 'p'
cnum = 'IV'
pnum = 4
pgraph = fetch_paragraph(ctag, ptag, cnum, pnum)
#print(pgraph)
words = pgraph.split()
#print(words)
iwords = []
for i,w in enumerate(words):
    if i % 3 == 0:
        iwords.append(f'*{w}*')
    else:
        iwords.append(w)
igraph = " ".join(iwords)
#print(igraph)


'''
5) Save a .jpeg of the book's cover photo and the extracted paragraph (using elements from Part 3 and 4) to a folder called "Case1_output". 
If the folder already exists, delete it and recreate it. Display the message, "cover-photo.jpg and paragraph.txt files created" on the 
terminal. Then create a DataFrame with the following columns: word, length, starts_with_vowel (True/False). Fill the DataFrame using the 
manipulated paragraph from Part 4 and print it to the terminal.'''
import os
import shutil

'''folder = f'Case1_output'
if os.path.exists(folder):
    shutil.rmtree(folder)
os.makedirs(folder)

with open(os.path.join(folder, 'cover-photo.jpg'), 'wb') as f:
    f.write(img_data)
with open(os.path.join(folder, 'paragraph.txt'), 'w', encoding='UTF-8') as f:
    f.write(igraph)
print(f'cover-photo.jpg and paragraph.txt files created)'''
import pandas as pd
df = pd.DataFrame({'word':words, 'length':[len(w) for w in words],'starts_with_vowel':[w[0].lower() in 'auiouy' for w in words]})
#print(df)
