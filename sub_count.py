# from threading import Thread
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
import time
import csv

#driver = webdriver.Chrome("/usr/bin/chromedriver")
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options, executable_path=r'/usr/bin/geckodriver')
#driver.get("http://google.com/")
#options = webdriver.ChromeOptions()
#options.headless = True
options.add_argument('--disable-gpu')

def main():
    count = 6
    Asianet_url = "https://www.youtube.com/watch?v=iL53Y28Rp84"
    News24_url = "https://www.youtube.com/watch?v=zcrUCvBD16k"
    Manorma_url = "https://www.youtube.com/watch?v=jjH6v95z3Nw"
    MediaOne_url = "https://www.youtube.com/watch?v=d1iwUB9YFnA"
    aljazeera_url = "https://www.youtube.com/watch?v=_dsWF2prkR8"
    ndtv_url = "https://www.youtube.com/watch?v=l9ViEIip9q4"
    
    while True:
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        sub_asianet = Asianet(Asianet_url)
        sub_24 = News24(News24_url)
        sub_manorama = Manorma(Manorma_url)
        sub_media1 = MediaOne(MediaOne_url)
        sub_aljazeera = AlJazeera(aljazeera_url)
        sub_ndtv = NDTV(ndtv_url)
        writecsv(current_time, sub_asianet, sub_24, sub_manorama, sub_media1, sub_aljazeera, sub_ndtv)
        print(count)
        time.sleep(36000)
        count = count + 6
    

def writecsv(current_time, sub_asianet, sub_24, sub_manorama, sub_media1, sub_aljazeera, sub_ndtv):
    with open('Sub_log.csv', 'a+', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow([current_time, sub_asianet, sub_24, sub_manorama, sub_media1, sub_aljazeera, sub_ndtv])
        
        
def Asianet(Asianet_url):
    
    driver.get(Asianet_url)
    time.sleep(1)
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    span = soup.find("yt-formatted-string", {"id": "owner-sub-count"})
    span = span.text
    sub_count = span.replace(' subscribers','')
    return sub_count

def News24(News24_url):
    driver.get(News24_url)
    time.sleep(1)
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    span = soup.find("yt-formatted-string", {"id": "owner-sub-count"})
    span = span.text
    sub_count = span.replace(' subscribers','')
    return sub_count
    
def Manorma(Manorma_url):
    driver.get(Manorma_url)
    time.sleep(1)
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    span = soup.find("yt-formatted-string", {"id": "owner-sub-count"})
    span = span.text
    sub_count = span.replace(' subscribers','')
    return sub_count

def MediaOne(MediaOne_url):
    driver.get(MediaOne_url)
    time.sleep(1)
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    span = soup.find("yt-formatted-string", {"id": "owner-sub-count"})
    span = span.text
    sub_count = span.replace(' subscribers','')
    return sub_count
    
def AlJazeera(aljazeera_url):
    driver.get(aljazeera_url)
    time.sleep(1)
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    span = soup.find("yt-formatted-string", {"id": "owner-sub-count"})
    span = span.text
    sub_count = span.replace(' subscribers','')
    return sub_count
    
def NDTV(ndtv_url):
    driver.get(ndtv_url)
    time.sleep(1)
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    span = soup.find("yt-formatted-string", {"id": "owner-sub-count"})
    span = span.text
    sub_count = span.replace(' subscribers','')
    return sub_count

if __name__ == "__main__":
    main()    
  

