# This uses BeautifulSoup to scrape from a html file in a local directory

from bs4 import BeautifulSoup  # Import the modile

with open("website.html", encoding="utf-8") as file:  # Open and Read the file
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")  # Create soup object using the html code and parser as attributes, can use lxml parser for xml files.

# print(soup.title)   #prints the title tag in its entirety
# print(soup.title.name)  #Gives the name of the tag
# print(soup.title.string)    #Returns the string inside the tag

# print(soup.prettify())  #Gives proper indentation

# print(soup.a)   #Gives the first anchor tag
# print(soup.li)   #Gives the first li tag
# print(soup.p)   #Gives the first p tag

all_anchor_tags = soup.find_all(name="a")  # Gives a list of all anchor tags
for a in all_anchor_tags:
    # print(a.getText())  #Gives the text in all anchor tags
    # print(a.get("href"))    #Returns a specific attribute of a tag
    pass

heading = soup.find_all(name="h1", id="name")
# print(heading)

section_heads = soup.find_all(
    name="h3", class_="heading"
)  # class_ is used so as to not clash with the class keyword
# print(section_heads)

company_url = soup.select_one(selector="p a")  # Use CSS selectors to narrow down
print(company_url)
