from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from helper_functions import (
    find_job_list,
    get_job_data,
    driver,
)
import json
from tqdm import tqdm


def scraper(driver):
    """main scraper function"""
    job_list_data = []
    job_count = 0
    try:
        while job_count == 0:
            job_list = find_job_list(driver)
            print("Total jobs found: ", len(job_list))
            for i in tqdm(range(len(job_list))):  
                # job_list = find_job_list(
                #     driver
                # )  # find the table again to avoid stale element error

                data = get_job_data(job_list, i, driver)
                job_list_data.append(data)
                job_count += 1
            if job_count == 0:
                continue
            else:
                job_list_data.append({"status": "completed"}) 
                return job_list_data
    except Exception as e:
        print("Error: ", e)
        job_list_data.append({"status": "failed"})
        return job_list_data
 


def main():

    webdriver = driver()

    data_list = scraper(webdriver)
    with open("data.json", "r") as file:
        old_data = json.load(file)

    if len(old_data) == 0: 
        with open("new.json", "w") as file:
            json.dump(data_list, file, indent=4)
    else:    
        new_list = []
        
        for i in range(len(data_list)):
            if i == len(data_list) - 1:
                new_list.append(data_list[i])
                break
            if data_list[i] in old_data:
                continue
            new_list.append(data_list[i])
            
        with open("new.json", "w") as file:
            json.dump(new_list, file, indent=4)
    with open("data.json", "w") as file:
            json.dump(data_list, file, indent=4)
    print("\n========== DOWNLOAD COMPLETED ===========\n")


main()
