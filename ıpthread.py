from bs4 import BeautifulSoup
import threading
import time
import requests


def check_url(url):
 
    url="http://spys.one/en/"        
    r = requests.get("url")   
    m = r.text
    soup = BeautifulSoup(m,"html.parser")
    result = soup.find_all("font",{"class":"spy14"})
    
   
    lock.acquire()
    array.append(result)
    lock.release()   


    threads = []
    for row in result:
      
        t = threading.Thread(target=check_url)
        threads.append(t)
        t.start()

  

    for t in threads:
        t.join()
    
