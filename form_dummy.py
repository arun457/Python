from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from tqdm import tqdm
import time

browser = webdriver.Chrome(ChromeDriverManager().install())
url = "https://forms.microsoft.com/r/Rs4R4pR9KZ"
browser.get(url)

for i in tqdm(range(100)):
	time.sleep(2)
	never1_xpath = '//*[@id="question-list"]/div/div[2]/div/div/div[2]/div/label/span[1]/input'
	never1 = browser.find_element(By.XPATH, never1_xpath)
	never1.click()

	submit_xpath = '//*[@id="form-main-content1"]/div/div/div[2]/div[3]/div/button'
	submit = browser.find_element(By.XPATH, submit_xpath)
	submit.click()

	time.sleep(2)
	submit_another_xpath = '//*[@id="form-main-content1"]/div/div/div[2]/div[2]/div[2]/a'
	submit_another = browser.find_element(By.XPATH, submit_another_xpath)
	submit_another.click()