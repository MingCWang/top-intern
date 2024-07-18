# top-intern

## Purpose

_**This is a system that sends notifications exclusively on FAANG internship/new grad positions in the United States. (updates every hour).**_

Many existing github repositories provide lists of internships and new grad positions. However, I find these repositories are often out of date. For the up-to-date ones, there's no way for me to receive notifications only from the companies I care about, over time I stopped checking notifications. For someone who is aiming for the top of the top positions, applying early could be more valuable than getting a referral, so it is important to have the most up-to-date information, but also not have to waste time checking the company pages constantly (more time to leetcode of course).

## Understanding the Code
This code leverages OOP allowing easy addition of new companies.:

- `send.py` is the main file that initiates all scraping and sending notifications.
- `/scrape` directory contains the main class that other company child classes inherit from. 
- `/[company]` directory contains the classes that scrape the respective company's career page. 

To add a company, one would only need to complete two functions `find_job_list()` and `get_job_data()` in each child class. Look at [meta.py](./meta/meta.py) for example

## Disclaimer
This web scraper is designed to operate in full compliance with legal and ethical standards to ensure responsible and lawful data extraction. Below are the key practices and guidelines our scraper follows:

1. Respecting robots.txt Files
Our scraper strictly adheres to the rules specified in the robots.txt files of target websites. 

2. Polite Crawling with Rate Limits
To avoid overloading web servers and ensure respectful access, our scraper implements rate limiting. Requests are configured to introduce delays between successive requests. This polite crawling approach helps maintain the performance and availability of the target websites.

3. Zero Monetization
This web scraper is used strictly for educational, research, or personal purposes and is not intended for commercial gain. I do not monetize the data extracted by our scraper. 
