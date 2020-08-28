from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PATH = '/Users/vvila/Desktop/coursera/Drivers/chromedriver'
driver = webdriver.Chrome(PATH)

executor_url = driver.command_executor._url
session_id = driver.session_id

driver.get('https:/www.coursera.org/')
cookies = {'domain': '.coursera.org', 'expiry': 1598562787, 'httpOnly': False, 'name': '__400vt', 'path': '/', 'secure': False, 'value': '1598560987696'}, {'domain': '.coursera.org', 'expiry': 1630097345, 'httpOnly': False, 'name': 'stc113717', 'path': '/', 'secure': False, 'value': 'tsa:1598560958791.1084761263.993956.5305325782528458.9:20200827211305|env:1%7C20200927204238%7C20200827211305%7C2%7C1030880:20210827204305|uid:1598560958790.2098511142.310347.113717.1421830964.:20210827204305|srchist:1030880%3A1%3A20200927204238:20210827204305'}, {'domain': 'www.coursera.org', 'expiry': 1661632983, 'httpOnly': False, 'name': '_tq_id.TV-63455409-1.39ed', 'path': '/', 'secure': False, 'value': 'aec45645b0ad1803.1598560957.0.1598560983..'}, {'domain': '.coursera.org', 'expiry': 1602880979, 'httpOnly': True, 'name': 'CAUTH', 'path': '/', 'secure': True, 'value': 'XO8r_Am1eumODJDed-riV0kE74olTG8vnNu15Uv7iBbnxsuZoVoVu5nz3qTzqm7s8x0u0sLLkvbi4wCretfWLA.TAv_HF6vdaV_AtYYrWKySA.kT5L0RQnWeqFD5xB6_EhEV-yQ0dKsHp184SnsA6o7noGo74Fx8U37ttOXAcydzbvWRxiG9bV6YmHDen-E2hPNwbuJZnvKurgnL28_KmWPHSF-uiFlUHBDI_w5Ea75S2OpQaFIAZ9AE3QmppaXX0TD2ThrXpVnvtZFclUBesG6arUzD72daNSpiObSnANRUFN'}, {'domain': '.www.coursera.org', 'httpOnly': False, 'name': 'G_AUTHUSER_H', 'path': '/', 'secure': True, 'value': '0'}, {'domain': '.coursera.org', 'expiry': 1598561015, 'httpOnly': False, 'name': '_dc_gtm_UA-86370891-1', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.coursera.org', 'expiry': 1598647383, 'httpOnly': False, 'name': '_uetsid', 'path': '/', 'secure': False, 'value': '42c8da7cfb8b9fe7ca3918b06c36075b'}, {'domain': '.www.coursera.org', 'expiry': 253402257600, 'httpOnly': False, 'name': 'G_ENABLED_IDPS', 'path': '/', 'secure': False, 'value': 'google'}, {'domain': '.coursera.org', 'expiry': 1598647383, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1331459877.1598560956'}, {'domain': '.coursera.org', 'expiry': 1630096954, 'httpOnly': False, 'name': '__204u', 'path': '/', 'secure': False, 'value': '6934985959-1598560953972'}, {'domain': '.coursera.org', 'expiry': 1598561015, 'httpOnly': False, 'name': '_dc_gtm_UA-28377374-1', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.coursera.org', 'expiry': 1661632983, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1640890997.1598560956'}, {'domain': '.coursera.org', 'expiry': 1599964983, 'httpOnly': False, 'name': '_uetvid', 'path': '/', 'secure': False, 'value': 'b7b465ff21fc74a67b1afca76540e660'}, {'domain': '.coursera.org', 'expiry': 1606336983, 'httpOnly': False, 'name': '_gcl_au', 'path': '/', 'secure': False, 'value': '1.1.461055385.1598560956'}, {'domain': '.coursera.org', 'expiry': 1599424954, 'httpOnly': False, 'name': 'CSRF3-Token', 'path': '/', 'secure': False, 'value': '1599424953.APZqf5pLu4pesKU5'}, {'domain': '.coursera.org', 'expiry': 1598562754, 'httpOnly': False, 'name': '__400v', 'path': '/', 'secure': False, 'value': '4deb1cff-0cbf-4ddf-fdc7-a818fd353af6'}, {'domain': '.coursera.org', 'expiry': 1606336983, 'httpOnly': False, 'name': '_fbp', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'fb.1.1598560956782.381864032'}, {'domain': '.coursera.org', 'expiry': 1630096954, 'httpOnly': False, 'name': '__204r', 'path': '/', 'secure': False, 'value': ''}
for cookie in cookies:
    driver.add_cookie(cookie)
time.sleep(1)
x = 1
f = open("all_videos.txt", "w")
while x < 7:
    link = 'https://www.coursera.org/learn/os-power-user/home/week/{x}'.format(x=x)
    driver.get(link)
    #all_modules = driver.find_element(By.TAG_NAME, 'class')
    time.sleep(5)
    modules = driver.find_elements_by_class_name("od-lesson-collection-element")
    for module in modules:
        videos = module.find_elements_by_tag_name('li')
        for video in videos:
            res = {}
            a_tag = video.find_element_by_tag_name('a')
            link = (a_tag.get_attribute('href'))
            lista = link.split('/')
            title = lista[-1]
            title = title.replace('-', '_')
            res[title] = link
            f.write(str(res)+'\n')
    x += 1
f.close()