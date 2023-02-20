# Only for AWS Lambda deployment
# DO NOT run it locally

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

def main(event, context):
    options = Options()
    options.binary_location = '/opt/headless-chromium'
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome('/opt/chromedriver',chrome_options=options)
    print(event['body'], type(event['body']))
    body = json.loads(event['body'])
    print(body['url'])
    driver.get(body['url'])

    driver.maximize_window() # For maximizing window
    driver.implicitly_wait(20) # gives an implicit wait for 20 seconds

    wait = WebDriverWait(driver, 10)

    inp=wait.until(
        EC.presence_of_element_located((By.XPATH, '//input[@id="ag"]'))
    ) #input examination number
    inp.click()
    inp.send_keys(body['ag'])
    submit = driver.find_element(By.XPATH, '//button[text()="Semak"]')
    submit.click()
    elem = driver.find_element_by_tag_name("body")
    # Get data after submit at the website
    response = {
        "statusCode": 200,
        "body": elem.text
    }
    driver.close()
    driver.quit()

    return response