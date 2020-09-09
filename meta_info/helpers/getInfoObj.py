# from bs4 import BeautifulSoup

# str = '''
# <title>This is the Title</title>
# <meta name="description" content="This is Description Content"/>
# <meta name="description" content="More Description"/>
# <meta name="keywords" content="This is Keywords"/>
# <meta name="keywords" content="More, Keywords"/>
# '''
# soup = BeautifulSoup(str,"html5lib")

# getInfoObj(soup)

def getInfoObj(soup):

  title = ''
  if soup.title and soup.title.contents:
    if len(soup.title.contents) > 0:
      title = f'{soup.title.contents[0]}'

  title = title.strip()
  print(f'title: {title}')

  Description = ''
  description_objs = soup.find_all("meta", attrs={"name": "description"})
  print(f'description_objs: {description_objs}')

  for descp in description_objs: 
    if descp.has_attr("content"):
      filler = '' if Description=='' else ' '
      if not Description.endswith('.') and Description!='':
        Description+='.'
      Description+=f'{filler}{descp["content"]}'

  Description = Description.strip()

  Keywords = [] 
  Keywords_string = ''
  keyword_objs = soup.find_all("meta", attrs={"name": "keywords"})

  print(f'keyword_objs: {keyword_objs}')
  for keyword in keyword_objs:
    if keyword.has_attr("content"):
      filler = '' if Keywords_string=='' else ','
      Keywords_string+=f'{filler}{keyword["content"]}'

  if(Keywords_string!=''):
    Keywords = Keywords_string.split(',')

  for i in range(len(Keywords)):
    Keywords[i] = Keywords[i].strip()

  return {
    'Title': title,
    'Description': Description,
    'Keywords': Keywords
  }