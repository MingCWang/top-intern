from scrape.scrape import Scrape 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Tiktok(Scrape): 
    
    def __init__(self):
        url = "https://careers.tiktok.com/position?keywords=&category=&location=CT_157%2CCT_1103355%2CCT_114%2CCT_94&project=7322364513776093449&type=2&job_hot_flag=&current=1&limit=10&functionCategory=&tag="
        company = 'tiktok'
        super().__init__(url, company)

    def find_job_list(self, driver):
        '''find the container that contains the job data'''
        try:
            job_container = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.rightBlock.rightBlock__2ZGFh')))
            job_list = job_container.find_elements(By.CSS_SELECTOR, 'div.listItems__1q9i5')
            return job_list
        except Exception as e:
            print('Error in find_job_list', e)
        
        
    def get_job_data(self, job_list, i, driver):
        '''get the job data from the container in json format'''
        try: 
            job_name = job_list[i].find_element(By.CSS_SELECTOR, 'a').get_attribute('href')    
            job_url = job_list[i].find_element(By.CSS_SELECTOR, 'span.positionItem-title-text > span.content__3ZUKJ.clamp-content').text 
            job_data = {
                'jobName': job_name,
                'jobURL': job_url
            }
            return job_data

        except Exception as e:
            print('Error in get_job_data', e)
        return 