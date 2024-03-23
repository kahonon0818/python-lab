# take URL and check things on that URL
"""import requests
# example1: hard coding not formal way for a reusable code
try:
    resp = requests.get("http://cnn.com")
    print(dir(resp))
    status = resp.status_code
    print(status)

    if status == 200:
        print("site is up")
    else:
        print ("site is down")  
except:
    print("please double check your url")"""

# example2 : hard coding not formal way for a reusable code
"""try:
    resp = requests.get("http://cnn.com")   
except:
    print("please double check your url")
else:
    status = resp.status_code
    if status == 200:
        print("site is up")
    else:
        print ("site is down")  
"""
# same code written as function 

import requests

def urlCheck(url):
    isUp = True
    try:
        resp = requests.get(url)   
    except:
        print("please double check your url")
    else:
        status = resp.status_code
        if status == 200:
            isUp = True
        else:
            isUp = False  
    return isUp
a = urlCheck("http://google.com")
print(a)