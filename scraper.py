from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
 
from helper_function import find_class_table, get_course_data, navigate_to_current_term, driver
import time
import json

def scraper(driver, start, end):
    '''main scraper function'''
    count = 0
    value = start - 1
    data_list = []
    course_count = 0
    try:
      while value < end:
            selected_text, value, count = navigate_to_current_term(driver, value, count)
            try: 
                while True: # loop through all the pages, until the next button is not found
                    class_list = find_class_table(driver)
                  
                    for i in range(1, len(class_list)): # skip the first row, then store the course data in a list in json format  
                        class_list = find_class_table(driver) # find the table again to avoid stale element error
                    
                        course, courseTitle, syllabus, instructor, requirements, prerequisites, description = get_course_data(class_list, i, driver)
                        driver.back() # go back to the previous page after scraping course description
                        data_list.append({
                            'course': course,
                            'courseTitle': courseTitle,
                            'syllabus': syllabus,
                            'instructor': instructor,
                            'term': selected_text,
                            'requirements': requirements,
                            'prerequisites': prerequisites,
                            'description': description
                        })
                        course_count += 1
                        print(f'{course_count} courses scraped - {course} - {courseTitle}')
                    WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Next →')]"))).click()
            except Exception as e:
                driver.get("https://registrar-prod.unet.brandeis.edu/registrar/schedule/search")
                print(e)
                continue
    except Exception as e:  # store the data in json format even when the program crashes
        with open('data1.json', 'w') as file:
            json.dump(data_list, file, indent=4)
        print("paused at ", value)
    return data_list, course_count

def main():
    start = 1201 
    # start = 1213
    # end = 1213
    end = 1233
    webdriver = driver()
    start_time = time.time()
     
    data_list, course_count = scraper(webdriver, start, end)

    end_time = time.time()
    duration = round(end_time - start_time, 1)
    with open('data1.json', 'w') as file:
            json.dump(data_list, file, indent=4)
    print("\n========== DOWNLOAD COMPLETED ===========\n")
    print(
        f"""Duration: {duration} seconds
Courses Downloaded: {course_count}
        """
    )
    print("==========================================\n")


main()