from django.shortcuts import render
import django.http as http
import os
from urllib.parse import urlparse
import requests
import sys
from bs4 import BeautifulSoup
from  meta_info.helpers.getInfoObj import getInfoObj


def index(request):

  file_dir = os.path.dirname(__file__)
  file_path = os.path.join(file_dir, './homepage.html')

  with open(file_path, 'r') as f:
    data = "\n".join(line for line in f)

  return http.HttpResponse(data, content_type="text/html")



def getMetaInfo(request, url):
  try:
    n_url = url
    p_url = urlparse(n_url)
  except ValueError:
    return http.JsonResponse({
      "status": "failure",
      "status_from_url_server": None,
      "reason": "Invalid url"
    })
  else:
    if(p_url.scheme!='http' and p_url.scheme!='https'):
      url = 'http://' + url

  try:
    print(f'requesting url... : {url}')
    res = requests.get(url, headers = {
      'User-Agent': 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'
    })
    print(f'res.status_code: {res.status_code}')
  except Exception as e:
    return http.JsonResponse({
      "status": "failure",
      "status_from_url_server": None,
      "reason": str(e)
    })

  if(res.ok==False):
    response_obj = {
      "status": "failure",
      "status_from_url_server": res.status_code,
      "reason": res.reason
    }
    return http.JsonResponse(response_obj)
  
  try:
    soup = BeautifulSoup(res.text, "html5lib")
  except Exception as e:
    return http.JsonResponse({
      "status": "failure",
      "status_from_url_server": None,
      "reason": str(e)
    })

  finalInfo = getInfoObj(soup)
  finalInfo.update({"status": "success"})

  print(f'\nfinalInfo:\n{finalInfo}')

  return http.JsonResponse(finalInfo)