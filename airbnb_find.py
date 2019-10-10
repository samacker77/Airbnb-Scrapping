import sys
import requests
import pandas as pd
from bs4 import BeautifulSoup
def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)
location = input("Enter your location: ")
check_in = input("Enter Check-in date: ")
check_out = input("Enter Check-out date: ")
guests = input("Enter number of guests: ")
url = "https://www.airbnb.co.in/s/"+location+"/homes?adults=2&checkin="+check_in+"&checkout="+check_out+"&guests="+guests+"&place_id=ChIJwe1EZjDG5zsRaYxkjY_tpF0&allow_override%5B%5D=&s_tag=N9fRr9A1"
airbnb_r = requests.get(url)
airbnb_soup = BeautifulSoup(airbnb_r.text, 'html.parser')
for name in airbnb_soup.findAll('span',{'class':'text_5mbkop-o_O-size_small_1gg2mc-o_O-weight_bold_153t78d-o_O-inline_g86r3e'}):
	uprint(name.text)

 
