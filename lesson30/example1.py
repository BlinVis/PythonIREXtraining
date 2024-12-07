from bs4 import BeautifulSoup

html_content="<html><body><p>Hello, Soup!</p></body></html>"

soup=BeautifulSoup(html_content, 'html.parser')

paragraph_text=soup.find("p").text

print(paragraph_text)
