from django.shortcuts import render
from django.http import HttpResponse

import requests
from bs4 import BeautifulSoup

# Create your views here.

def main(request):
  return render(request, 'main.html')

# Funcion cotizar, realiza el request y el scrapping
def cotizar(request):
  
  if request.method == 'GET':

    url = request.GET['link']

    # headers 
    my_headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3", 
        "Accept-Encoding": "gzip, deflate, br", 
        "Accept-Language": "en-US,en;q=0.9", 
        "Upgrade-Insecure-Requests": "1", 
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}

    response = requests.get(url, headers= my_headers)
    
    res = BeautifulSoup(response.text,"lxml");

    # Data of interest
    img = res.find("img", {"id":"landingImage"})
    title = res.find("span", {"id":"productTitle"})


    # Getting image from the string
    image_txt = img['data-a-dynamic-image']
    print(image_txt)
    q1 = image_txt.find('"')
    q2 = image_txt[(q1+1):].find('"')
    txt_image = image_txt[(q1+1):(q1+q2+1)]
    
    # Excepciones debido al id del precio, ya que puede variar de producto a producto
    try:
      price = res.find("span", {"id":"priceblock_ourprice"}).text
    except:
      try:
        price = res.find("span", {"id":"priceblock_saleprice"}).text
      except:
        try:
          price = res.find("span", {"id":"priceblock_dealprice"}).text
        except:
          price = 'No se encontro el precio'

    # Generamos el html que sera lo que devuelve
    res_html = '<img src={}> <br> <p>{}</p>'.format(txt_image, price)

  return HttpResponse(res_html)
