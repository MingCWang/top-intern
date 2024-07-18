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
        with open("backup.json", "w") as file:
                json.dump(job_list, file, indent=4)
 


def main():

    webdriver = driver()

    data_list = scraper(webdriver)
    with open("data.json", "r") as file:
        old_data = json.load(file)

    if len(old_data) == 0: 
        with open("data.json", "w") as file:
            json.dump(data_list, file, indent=4)
    else:    
        new_list = [job for job in data_list if job not in old_data]
        with open("data.json", "w") as file:
                    json.dump(data_list, file, indent=4)
        with open("new.json", "w") as file:
            json.dump(new_list, file, indent=4)
    print("\n========== DOWNLOAD COMPLETED ===========\n")


main()
