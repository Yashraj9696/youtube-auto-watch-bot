from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from time import sleep
import random

# get the proxies from proxy.txt and store it into proxy_list array
proxy_list = []

with open('proxy.txt') as fil:
    proxy_list = [i.strip() for i in fil]

# get input from user
URL = input("https://youtu.be/TGZgULpdgn4?si=H79oOLvD_jxTBGQX")
timeToReopenBrowser = input("2")
videoLength = input("20:00:00")

# convert input to int
timeToReopenBrowser = int(2)
videoLength = int(20 min)

# get a rendom proxy every time the while loop runs
# open chrome and go to the URL link
# wait for n secounds to close the browser and open it again
i = 0
while i < timeToReopenBrowser:
    proxies = random.choice(proxy_list)
    proxy_ip_port = proxies

    print("The proxy used is:", proxy_ip_port)

    # set proxy

    proxy = Proxy()
    proxy.proxy_type = ProxyType.MANUAL
    proxy.http_proxy = proxy_ip_port
    proxy.ssl_proxy = proxy_ip_port

    capabilities = webdriver.DesiredCapabilities.CHROME
    proxy.add_to_capabilities(capabilities)

    # let's call the browser

    driver = webdriver.Chrome(desired_capabilities=capabilities)
    driver.get(URL)

    sleep(videoLength)

    # close browser

    driver.quit()

    i += 1

# https://openproxy.space/api replace static proxies
