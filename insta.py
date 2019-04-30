import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from bs4 import BeautifulSoup
sess = requests.Session()


http_proxy = "http://163.172.110.14:1460"

proxyDict = {
    "http":  http_proxy,
    "https": http_proxy
}

def step_one():
    headers = {
    "Host": "www.instagram.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "DNT": "1",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"

    }

    r = sess.get("https://www.instagram.com/accounts/password/reset/",headers=headers,proxies=proxyDict,verify=False,timeout=10)

    part1 = r.text.split('"csrf_token":"')[1]
    part2 = part1.split('"')
    csrf_token = part2[0]
    ajax = r.text.split('"rollout_hash":"')[1].split('"')[0]
   
    step_two(csrf_token,ajax)

 


def step_two(csrf_token,ajax):
    email="mustafasarikaya1@hotmail.com"

    headers = {
    "Host": "www.instagram.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://www.instagram.com/accounts/password/reset/",
    "X-CSRFToken": csrf_token,
    "X-Instagram-AJAX":ajax,
    "Content-Type": "application/x-www-form-urlencoded",
    "X-Requested-With": "XMLHttpRequest",
    "DNT": "1",
    "Connection": "keep-alive"
    }

    data = {
    "email_or_username": email,
    "recaptcha_challenge_field":""
    }

    r = sess.post("https://www.instagram.com/accounts/account_recovery_send_ajax/",headers=headers, data=data, proxies=proxyDict, verify=False,timeout=10).json()
    
  
    if r['status']=="ok":
        print("avaliable")
    elif r['status']=="fail":
        print("not avaliable")



def startTask():
    step_one()
    
    

startTask()
    