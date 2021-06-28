#! python 3
# WS_personal_project - a robot created from scratch to download all the book covers
# from the homepage of 'https://inventwithpython.com/'

import requests
import bs4
import os

os.mkdir(r'C:\Users\ticom\OneDrive\Documentos\Python_Scripts\Covers')
url = 'https://inventwithpython.com/'

#get the home page and check if it worked
res = requests.get(url)
res.raise_for_status()

#parsig the HTML
soup = bs4.BeautifulSoup(res.text, 'html.parser')
#getting the img elements inside a "<a> <\a>"
img_element = soup.select('a img')
#create a list to store each img url str in a element of the list
imgsrc = ['' for n in range(len(img_element))]
#getting the second half of the url of the covers
for n in range(len(img_element)):
    imgsrc[n] = img_element[n].get('src')

# downloading the covers
for n in range(len(imgsrc)):
    # specifying only covers by url
    if 'cover' in imgsrc[n]:
        #getting the source page for the image
        res = requests.get(url + imgsrc[n])
        res.raise_for_status()

        # saving the image
        imageFile = open(os.path.join(r'C:\Users\ticom\OneDrive\Documentos\Python_Scripts\Covers',
                                      os.path.basename(imgsrc[n])), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
        print(f'{imgsrc[n]} downloaded')
    else:
        print( f"{imgsrc[n]} is not a cover, im not downloading it")
pause