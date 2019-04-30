import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from bs4 import BeautifulSoup
sess = requests.Session()

http_proxy = "http://163.172.110.14:1457"

proxyDict = {
    "http":  http_proxy,
    "https": http_proxy
}




def step_one():
    headers = {
    "Host": "twitter.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "DNT": "1",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"


    }

    r = sess.get("https://twitter.com/account/begin_password_reset",headers=headers,proxies=proxyDict,verify=False)

    m = r.text
        
    soup = BeautifulSoup(m,"html.parser")

    token = soup.find(attrs={"name": "authenticity_token"})['value']
            
    print(token)
            
    authenticity_token = token

    result = step_two(authenticity_token)    

    return result    

def step_two(authenticity_token):
    email="mustafasarikaya1@hotmail.com"

    headers = {
    "Host": "twitter.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://twitter.com/account/begin_password_reset",
    "Content-Type": "application/x-www-form-urlencoded",
    "DNT": "1",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
    }

    data = {
        "authenticity_token": authenticity_token,
        "account_identifier": email

        }

    r = sess.post("https://twitter.com/account/begin_password_reset",headers=headers, data=data, proxies=proxyDict, verify=False)

    #print(r.text)
    result = ""
    if  "/account/begin_password_reset" in r.text or "We couldn't find your account with that information" in r.text: 
        result = "Available"
    elif "/account/send_password_reset" in r.text or "https://twitter.com/account/send_password_reset" in r.text: 
        result = "Not Available"
    print(result)

    return result

def startTask():
    result = step_one()
    print(result)
    

startTask()