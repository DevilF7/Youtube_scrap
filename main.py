# from threading import Thread
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.firefox.options import Options
from pyvirtualdisplay import Display
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
import time
import csv

#display = Display(visible=0, size=[800, 600])
#display.start()


# Constants
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path=r'/usr/bin/chromedriver',options=options, service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])



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
        view_asianet = Asianet(Asianet_url)
        view_24 = News24(News24_url)
        view_manorama = Manorma(Manorma_url)
        view_media1 = MediaOne(MediaOne_url)
        view_aljazeera = AlJazeera(aljazeera_url)
        view_ndtv = NDTV(ndtv_url)
        writecsv(current_time, view_asianet, view_24, view_manorama, view_media1, view_aljazeera, view_ndtv)
        print(count)
        time.sleep(7200)
        count = count + 6


def writecsv(current_time, view_asianet, view_24, view_manorama, view_media1, view_aljazeera, view_ndtv):
    with open('View_log.csv', 'a+', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow([current_time, view_asianet, view_24, view_manorama, view_media1, view_aljazeera, view_ndtv])




def Asianet(Asianet_url):
    
    driver.get(Asianet_url)
    time.sleep(1)
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    span = soup.find("span", {"class":"view-count"})
    watch = span.text
    number = int(''.join(filter(str.isdigit, watch)))
    return number

def News24(News24_url):
    driver.get(News24_url)
    time.sleep(1)
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')

    span = soup.find("span", {"class":"view-count"})
    watch = span.text
    number = int(''.join(filter(str.isdigit, watch)))
    return number

def Manorma(Manorma_url):
    driver.get(Manorma_url)
    time.sleep(1)
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    span = soup.find("span", {"class":"view-count"})
    watch = span.text
    number = int(''.join(filter(str.isdigit, watch)))
    return number

def MediaOne(MediaOne_url):
    driver.get(MediaOne_url)
    time.sleep(1)
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    span = soup.find("span", {"class":"view-count"})
    watch = span.text
    number = int(''.join(filter(str.isdigit, watch)))
    return number
    
def AlJazeera(aljazeera_url):
    driver.get(aljazeera_url)
    time.sleep(1)
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    span = soup.find("span", {"class":"view-count"})
    watch = span.text
    number = int(''.join(filter(str.isdigit, watch)))
    return number
    
def NDTV(ndtv_url):
    driver.get(ndtv_url)
    time.sleep(1)
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    span = soup.find("span", {"class":"view-count"})
    watch = span.text
    number = int(''.join(filter(str.isdigit, watch)))
    return number

if __name__ == "__main__":
    main()


driver.quit()
