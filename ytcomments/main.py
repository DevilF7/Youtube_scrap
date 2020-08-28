from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from datetime import datetime
import time
import csv

class bcolors:
    HEADER = '\033[102m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[31m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'

options = Options()
# options.headless = True
driver = webdriver.Firefox(options=options, executable_path=r"/home/rook/work/scrap/Vahan_Scrap/geckodriver")

base_url = "https://www.youtube.com/watch?v=ftMnmPC82qM"
url = base_url.replace("watch?v=","live_chat?v=")

def main():
    driver.get(url)
    driver.implicitly_wait(1)
    count_prev = 0
    count_change_prev = 1
    total = 0
    while True: #Only int allowed here !
        no_chat = len(driver.find_elements_by_css_selector('yt-live-chat-text-message-renderer'))

        count_change = no_chat - count_prev
        total = total + count_change
        if count_change == 0:
            count_change = count_change +1

        chat_rate  = count_change_prev - count_change
        if count_change > 0:
            print(bcolors.GREEN+ str(count_change) + "^" +bcolors.END+" More comments | Total Comments :  "+ str(total))
            sign = "+"
        elif count_change == 0:
            print(bcolors.RED+"No change"+bcolors.END+" | Total Comments : "+str(total))
            sign = "="
        else:  #Lol only happens once in a million years or say youtube got hacked
            print(bcolors.HEADER + str(count_change) + "V" + bcolors.END + " Less comments")

        time.sleep(1)
        count_change_prev = count_change
        count_prev = no_chat
        write_csv(count_change, total, sign)

def write_csv(count_change, total, sign):
    with open('log.csv', 'a+', newline='\n') as file:
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        writer = csv.writer(file)
        writer.writerow([current_time, base_url, count_change, total, sign])




if __name__ == '__main__':
    main()
