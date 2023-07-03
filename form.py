from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from tqdm import tqdm
import time

browser = webdriver.Chrome(ChromeDriverManager().install())
url = "https://forms.office.com/pages/responsepage.aspx?id=ANUvPxRQGUupdAkOtgz_1UVmOI_bu4xHgKujCpL_4EBUQ1RCVVVIVUhSRElaOE40VzlSNE4wVFhYVi4u&fbclid=IwAR1C67BWBhHEU5ai87fgy1EGaihaHQg6uwxYr9zJLxOK9YM-4F5S-6-tYx4"
browser.get(url)

for i in tqdm(range(1000)):
	time.sleep(2)
	never1_xpath = '//*[@id="question-list"]/div[1]/div[2]/div/div/div[4]/div/label/span[1]/input'
	never1 = browser.find_element(By.XPATH, never1_xpath)
	never1.click()

	never2_xpath = '//*[@id="question-list"]/div[2]/div[2]/div/div/div[4]/div/label/span[1]/input'
	never2 = browser.find_element(By.XPATH, never2_xpath)
	never2.click()

	never3_xpath = '//*[@id="question-list"]/div[3]/div[2]/div/div/div[2]/div/label/span[1]/input'
	never3 = browser.find_element(By.XPATH, never3_xpath)
	never3.click()

	never4_xpath = '//*[@id="question-list"]/div[4]/div[2]/div/div/div[4]/div/label/span[1]/input'
	never4 = browser.find_element(By.XPATH, never4_xpath)
	never4.click()

	never5_xpath = '//*[@id="question-list"]/div[5]/div[2]/div/div/div[5]/div/label/span[1]/input'
	never5 = browser.find_element(By.XPATH, never5_xpath)
	never5.click()

	text6_xpath = '//*[@id="question-list"]/div[6]/div[2]/div/span/textarea'
	text6_field = browser.find_element(By.XPATH, text6_xpath)
	text6_field.clear()
	text6_field.send_keys("Nothing.")

	never7_xpath = '//*[@id="question-list"]/div[7]/div[2]/div/div/div[4]/div/label/span[1]/input'
	never7 = browser.find_element(By.XPATH, never7_xpath)
	never7.click()

	text8_xpath = '//*[@id="question-list"]/div[8]/div[2]/div/span/textarea'
	text8_field = browser.find_element(By.XPATH, text8_xpath)
	text8_field.clear()
	text8_field.send_keys("Nothing.")


	time.sleep(0.1)
	nine_1_xpath = '//*[@id="question-list"]/div[9]/div[2]/div/table/tbody/tr[1]/td[2]/div/label/span/input'
	nine_1 = browser.find_element(By.XPATH, nine_1_xpath)
	nine_1.click()

	# time.sleep(0.1)
	nine_2_xpath = '//*[@id="question-list"]/div[9]/div[2]/div/table/tbody/tr[2]/td[2]/div/label/span/input'
	nine_2 = browser.find_element(By.XPATH, nine_2_xpath)
	nine_2.click()

	# time.sleep(0.1)
	nine_3_xpath = '//*[@id="question-list"]/div[9]/div[2]/div/table/tbody/tr[3]/td[2]/div/label/span/input'
	nine_3 = browser.find_element(By.XPATH, nine_3_xpath)
	nine_3.click()

	# time.sleep(0.1)
	nine_4_xpath = '//*[@id="question-list"]/div[9]/div[2]/div/table/tbody/tr[4]/td[2]/div/label/span/input'
	nine_4 = browser.find_element(By.XPATH, nine_4_xpath)
	nine_4.click()

	# time.sleep(0.1)
	nine_5_xpath = '//*[@id="question-list"]/div[9]/div[2]/div/table/tbody/tr[5]/td[2]/div/label/span/input'
	nine_5 = browser.find_element(By.XPATH, nine_5_xpath)
	nine_5.click()

	# time.sleep(0.1)
	nine_6_xpath = '//*[@id="question-list"]/div[9]/div[2]/div/table/tbody/tr[6]/td[2]/div/label/span/input'
	nine_6 = browser.find_element(By.XPATH, nine_6_xpath)
	nine_6.click()

	# time.sleep(0.1)
	nine_7_xpath = '//*[@id="question-list"]/div[9]/div[2]/div/table/tbody/tr[7]/td[2]/div/label/span/input'
	nine_7 = browser.find_element(By.XPATH, nine_7_xpath)
	nine_7.click()

	# time.sleep(0.1)
	text10_xpath = '//*[@id="question-list"]/div[10]/div[2]/div/span/textarea'
	text10_field = browser.find_element(By.XPATH, text10_xpath)
	text10_field.clear()
	text10_field.send_keys("Nothing.")

	submit_xpath = '//*[@id="form-main-content1"]/div/div/div[2]/div[3]/div/button'
	submit = browser.find_element(By.XPATH, submit_xpath)
	submit.click()

	time.sleep(2)
	submit_another_xpath = '//*[@id="form-main-content1"]/div/div/div[2]/div[2]/div[2]/a'
	submit_another = browser.find_element(By.XPATH, submit_another_xpath)
	submit_another.click()


input("Press any key to exit.")

browser.quit()