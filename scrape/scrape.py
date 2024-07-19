from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import json
from tqdm import tqdm


class Scrape: 
    
    def __init__(self, url, company):
        self.url = url
        self.company = company
        self.driver = self.driver()
        self.data_list = self.scraper(self.driver)
        
    def run(self):
        with open(f"{self.company}/data.json", "r") as file:
            old_data = json.load(file)

        if len(old_data) == 0: 
            with open(f"{self.company}/new.json", "w") as file:
                json.dump(self.data_list, file, indent=4)
        else:    
            new_list = []
        
            for i in range(len(self.data_list)):
                if i == len(self.data_list) - 2:
                    new_list.append(self.data_list[-2])
                    new_list.append(self.data_list[-1])
                    break
                if self.data_list[i] in old_data:
                    continue
                new_list.append(self.data_list[i])
                
            with open(f"{self.company}/new.json", "w") as file:
                json.dump(new_list, file, indent=4)
        with open(f"{self.company}/data.json", "w") as file:
                json.dump(self.data_list, file, indent=4)
        print("\n========== DOWNLOAD COMPLETED ===========\n")
        
        return new_list

    def driver(self):
        '''creates driver instance'''
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("window-size=1920,1080")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("start-maximized")
        driver = webdriver.Chrome(options=chrome_options) # use this line if you want to run the scraper in the background
        driver.maximize_window()
        # driver = webdriver.Chrome()
        # driver.get("https://jobs.careers.microsoft.com/global/en/search?lc=United%20States&d=Software%20Engineering&exp=Students%20and%20graduates&l=en_us&pg=1&pgSz=20&o=Relevance&flt=true")
        driver.get(self.url)
        
        return driver
  
    def scraper(self, driver):
        """main scraper function"""
        job_list_data = []
        job_count = 0
        retry = 0
        try:
            while retry < 20 and job_count == 0:
                job_list = self.find_job_list(driver)
                print("Total jobs found: ", len(job_list))
                for i in tqdm(range(len(job_list))):  
                    # job_list = find_job_list(
                    #     driver
                    # )  # find the table again to avoid stale element error

                    data = self.get_job_data(job_list, i, driver)
                    job_list_data.append(data)
                    job_count += 1
                if job_count != 0:
                    job_list_data.append({"status": "completed"}) 
                    job_list_data.append({"company": f"{self.company}"})
                    return job_list_data
            job_list_data.append({"status": "completed"}) 
            job_list_data.append({"company": f"{self.company}"})
            return job_list_data
        except Exception as e:
            print("Error: ", e)
            job_list_data.append({"status": "failed"})
            job_list_data.append({"company": f"{self.company}"})
            return job_list_data
    
    def find_job_list(self, driver):
        raise NotImplementedError
    def get_job_data(self, job_list, i, driver):
        raise NotImplementedError
        