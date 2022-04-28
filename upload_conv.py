from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import os
import zipfile
import datetime

# to find yesterday's date
date_info = datetime.date.today()
#folder_name = 'Data_' + str(date_info)
#folder_name = 'Data_2020-04-27'

#with zipfile.ZipFile(folder_name+'.zip','w') as zf:
#  zf.write('conversation_history.csv')


chrome_options = Options() 
chrome_options.add_argument('--headless')
#chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get('https://unimelbcloud-my.sharepoint.com/:f:/g/personal/jwwei2_student_unimelb_edu_au/EoL-ZWvrJwZFvMT1gXtI8lgBJbJuHAgCWbYy-m30qmMJoQ')
sleep(20)

elementUpload = browser.find_element_by_class_name('od-fileRequest-input')
elementUpload.send_keys('/home/ubuntu/question_bot/'+str(date_info)+'_conversation_history.csv')
sleep(30)

elementFirst = browser.find_element_by_id('TextField11')
elementFirst.send_keys("Rasa")
elementSecond = browser.find_element_by_id('TextField14')
elementSecond.send_keys("Conv")
upload = browser.find_element_by_class_name('od-fileRequest-button').click()
sleep(2*60)
browser.quit()
