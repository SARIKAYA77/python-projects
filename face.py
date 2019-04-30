import requests
import brotli
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from bs4 import BeautifulSoup

sess = requests.Session()
http_proxy = "http://163.172.110.14:1457"

proxyDict = {
    "http":  http_proxy,
    "https": http_proxy
}

def brotli_decompress_utf8(html):
        
    r = brotli.decompress(html)
    decoded = r.decode('utf-8', 'ignore')
    return str(decoded)


def step_one():
    headers = {
    "Host": "mbasic.facebook.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "DNT": "1",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"


    }

    r = sess.get("https://mbasic.facebook.com/login/identify/",headers=headers,proxies=proxyDict,verify=False)

    m= r.content
        
    m = brotli_decompress_utf8(m)


    soup = BeautifulSoup(m,"html.parser")

    face = soup.find(attrs={"name": "lsd"})['value']
            
    print(face)
            
    lsd = face

    result = step_two(lsd)    

    return result    


def step_two(lsd):
    email="mustafasarikaya1@hotmail.com"

    headers = {
    "Host": "mbasic.facebook.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://mbasic.facebook.com/login/identify/",
    "Content-Type": "application/x-www-form-urlencoded",
    "DNT": "1",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"

    }

    params = {
        "ctx": "recover",
        "search_attempts": "1"

        }
    data = {
        "lsd":lsd,
        "email":email,
        "did_submit": "Search"
    }    

    r = sess.post("https://mbasic.facebook.com/login/identify/",headers=headers,params=params,data=data,proxies=proxyDict,verify=False)
    m= r.content
        
    m = brotli_decompress_utf8(m)

    #print(r.text)
    result = ""
    if  "login_identify_search_error_msg" in m: 
        result = "Available"
    elif 'pic.php'in m or 'reset_action' in m: 
        result = "Not Available"
    print(m)

    return result

def start():
    result = step_one()
    print(result)
    

start()