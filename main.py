from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
import os
from dotenv import load_dotenv

load_dotenv()


PROMISE_DOWN=100
PROMISE_UP=40
TWITTER_EMAIL=os.environ.get('TWITTER_EMAIL')
TWITTER_PASSWORD=os.environ.get('TWITTER_PASSWORD')
TWITTER_NAME=os.environ.get('TWITTER_NAME')
# got_d=0
# got_s=0


chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

CHROME_DRIVER=webdriver.Chrome(options=chrome_option)

class InternetSpeedTwitterBot:
    def __init__(self,driver):
        self.driver1=driver
        # self.driver2=driver------------------------------------------------------------------------------
        self.up=0
        self.down=0

    def get_internet_speed(self):
        self.driver1.get("https://www.speedtest.net/")
        time.sleep(10)
        continue_=self.driver1.find_element(By.ID,value="onetrust-accept-btn-handler")
        continue_.click()
        time.sleep(2)
        go=self.driver1.find_element(By.XPATH,value="//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a")
        go.click()
        time.sleep(60)
        d_sp=self.driver1.find_element(By.XPATH,value="//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span")
        print(f"DOWN SPEED {d_sp.text}")
        self.down=float(d_sp.text)
        s_sp=self.driver1.find_element(By.XPATH,value="//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span")
        self.up=float(s_sp.text)
        print(f"UPLOAD SPEED {s_sp.text}")
        #self.driver1.quit()

    def tweet_at_provider(self):
        self.driver1.get("https://x.com/i/flow/login")
        time.sleep(20)
        email=self.driver1.find_element(By.XPATH,value="//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input")
        email.send_keys(TWITTER_EMAIL,Keys.ENTER)
        time.sleep(20)
        pasword=self.driver1.find_element(By.XPATH,value="//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        pasword.send_keys(TWITTER_PASSWORD,Keys.ENTER)
        time.sleep(10)
        post=self.driver1.find_element(By.XPATH,value="//*[@id='react-root']/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div")
        post.click()
        time.sleep(5)
        msg=self.driver1.find_element(By.XPATH,value="//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div")
        msg.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISE_DOWN}down/{PROMISE_UP}up??")
        post_but=self.driver1.find_element(By.XPATH,value="//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/button[2]")
        post_but.click()
        time.sleep(5)
        self.driver1.quit()
        print("Post Potachi!!!!")

        
        





bot = InternetSpeedTwitterBot(CHROME_DRIVER)
bot.get_internet_speed()
time.sleep(10)
bot.tweet_at_provider()