from scrape.scrape import Scrape 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Meta(Scrape): 
    
    def __init__(self):
        url = "https://www.metacareers.com/jobs?teams[0]=University%20Grad%20-%20Engineering%2C%20Tech%20%26%20Design&teams[1]=Internship%20-%20Engineering%2C%20Tech%20%26%20Design"
        company = 'meta'
        super().__init__(url, company)

    def find_job_list(self, driver):
        '''find the container that contains the job data'''
        try:
            job_container = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div._6g3g.x1vxotmq.x1jkpaj2.x1x3ocdb')))
            job_list = job_container.find_elements(By.CSS_SELECTOR, 'div.x1ypdohk[role="link"]')
            return job_list
        except Exception as e:
            print('Error in find_job_list', e)
        
        
    def get_job_data(self, job_list, i, driver):
        '''get the job data from the container in json format'''
        try: 
            job_name = job_list[i].find_element(By.CSS_SELECTOR, 'div._6g3g.x8y0a91.xriwhlb.xngnso2.xeqmlgx.xeqr9p9.x1e096f4').text
            card = job_list[i].find_element(By.CSS_SELECTOR, 'div.x2izyaf.x1lcm9me.x1yr5g0i.xrt01vj.x10y3i5r')
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", card)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.x2izyaf.x1lcm9me.x1yr5g0i.xrt01vj.x10y3i5r'))).click()
            handle = driver.window_handles
            if len(handle) > 1:
                driver.switch_to.window(handle[-1])
                job_url = driver.current_url
                driver.close()
                driver.switch_to.window(handle[0])
                job_data = {
                    'jobName': job_name,
                    'jobURL': job_url
                }
                return job_data
            else:
                print('new tab not opened')
        
        except Exception as e:
            print('Error in get_job_data', e)
        return 