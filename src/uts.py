from seleniumwire import webdriver
from selenium.webdriver.common.by import By

import time
import json
import pandas as pd
import re
import random
import os

folder_dist_data = '../dist/data'
try:
    os.makedirs(folder_dist_data, exist_ok=True)
    print(f"'{folder_dist_data}' isimli klasör başarıyla oluşturuldu.")
except OSError as error:
    print(f"'{folder_dist_data}' isimli klasör oluşturulurken hata oluştu: {error}")


options = {"disable_encoding": True}
driver = webdriver.Chrome(seleniumwire_options=options)
collected_data = []

driver.get("https://utsuygulama.saglik.gov.tr/UTS/")
print("visit UTS")
time.sleep(3)

driver.get("https://utsuygulama.saglik.gov.tr/UTS/vatandas#/vatTibbiCihazListele")
print("visit vatTibbiCihazListele")
time.sleep(10)

driver.get("https://utsuygulama.saglik.gov.tr/UTS/vatandas#/vatandasTibbiCihazFirmaOzetiListele")
print("visit vatandasTibbiCihazFirmaOzetiListele")
time.sleep(3)

chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'H', 'I', 'İ', 'J', 'K', 'L', 'M', 'N', 'O', 'Ö', 'P', 'Q', 'R', 'S', 'Ş', 'T', 'U', 'Ü', 'V', 'W', 'X', 'Y', 'Z']
i = 0

for char in chars:

    input_element = driver.find_element(By.ID, "unvanIn")
    input_element.clear()
    input_element.send_keys(char)
    print("write ", char)
    time.sleep(2)

    if i == 0:
        open_filter = driver.find_element(By.ID, "gelismisLbl")
        open_filter.click()
        print("click ayrıntılar")
        time.sleep(2)

        listbox = driver.find_element(By.XPATH, "//span[@aria-owns='faaliyetAlaniDropDown_listbox']")
        listbox.click()
        print("click listbox")
        time.sleep(2)
            
        select_filter = driver.find_element(By.XPATH, "//li[contains(text(), 'Üretici/İthalatçı/Bayi/İhracatçı')]")
        select_filter.click()
        print("click bayi")
        time.sleep(2)
    
    i += 1

    button_element = driver.find_element(By.ID, "sorgulaBtn")
    button_element.click()
    print("click sorgula")
    time.sleep(2)

    driver.wait_for_request("https://utsuygulama.saglik.gov.tr/UTS/vat/rest/vatKurum/aktifTibbiCihazKurumListele", timeout=30)

    del driver.requests

    calculate_link = driver.find_element(By.XPATH, "//a[contains(text(), 'hesapla')]")
    calculate_link.click()
    print("click hesapla")
    time.sleep(2)


    data_count = driver.find_element(By.XPATH, "//span[@ng-if='totalCountKnown === true && showCalculateButton === true']")
    number_count = re.search(r'\d+', data_count.text)
    
    page_total = 0
    page = 2
    wait = 3
    page_wait = 1
    collected_data = []
    
    if number_count:
        number = number_count.group()
        page_total = -(-int(number) // 15)
    
    print("Şu anki sayfa:", char,":", "1", "/", page_total)
    
    # FOR TEST
    # for _ in range(3):
    for _ in range(page_total):
        for request in driver.requests:
            if request.url == "https://utsuygulama.saglik.gov.tr/UTS/vat/rest/vatKurum/aktifTibbiCihazKurumListele":
                json_data = json.loads(request.response.body.decode('utf-8'))
                
                for item in json_data['data']:
                    collected_data.append(item)

        del driver.requests
        
        print("Şu anki sayfa:", char,":", page, "/", page_total)
        page += 1
        
        next_link = driver.find_element(By.XPATH, "//a[@ng-click='goNextPage()']")
        next_link.click()
        # print("click next page")
        
        random_wait = random.randint(2, wait+page_wait)
        # print("wait:", wait)
        # print("random_wait:", random_wait)
        time.sleep(random_wait)
        
        if page % 10 == 0:
            page_wait += 1

    collected_data_dumps = json.dumps(collected_data, ensure_ascii=False, indent=4)
    json_fn = f'{folder_dist_data}/data_{char}.json'
    with open(json_fn, 'w', encoding='utf-8') as f:
        f.write(collected_data_dumps)
    print(char,": Veriler JSON dosyasına kaydedildi.")

    df = pd.DataFrame(collected_data)
    excel_fn = f'{folder_dist_data}/data_{char}.xlsx'
    df.to_excel(excel_fn, index=False)
    print(char,": Veriler EXCEL dosyasına kaydedildi.")


print("Driver Quit")
driver.quit()