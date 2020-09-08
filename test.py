#!/usr/bin/python3
from bs4 import BeautifulSoup

str = '''
<title>This is the Title</title>
<meta name="description" content="This is Description Content"/>
<meta name="description" content="More Description"/>
<meta name="keywords" content="This is Keywords"/>
<meta name="keywords" content="More, Keywords"/>
'''
soup = BeautifulSoup(str,"html5lib")


def getInfoObj(soup):

  title = ''
  if soup.title and soup.title.contents:
    if len(soup.title.contents) > 0:
      title = soup.title.contents[0]


  print(f'title: {title}')

  Description = ''
  description_objs = soup.find_all("meta", attrs={"name": "description"})

  for descp in description_objs: 
    if descp.has_attr("content"):
      filler = '' if Description=='' else ' '
      if not Description.endswith('.') and Description!='':
        Description+='.'
      Description+=f'{filler}{descp["content"]}'
      if not Description.endswith('.') and Description!='':
        Description+='.'



  print(f'Description: {Description}')

  Keywords = [] 
  Keywords_string = ''
  keyword_objs = soup.find_all("meta", attrs={"name": "keywords"})

  for keyword in keyword_objs:
    if keyword.has_attr("content"):
      filler = ','
      Keywords_string+=f'{filler}{keyword["content"]}'

  Keywords_string = Keywords_string.replace(",", " ")

  Keywords = Keywords_string.split()


  print(f'Keywords: {Keywords}')

  return {
    'title': title,
    'Description': Description,
    'Keywords': Keywords
  }

getInfoObj(soup)