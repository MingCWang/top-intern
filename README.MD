# top-intern

## Purpose
There are many existing github repositories that provide lists of internships and new grad positions. However, these repositories are often outdated and do not provide the most up-to-date information, and for someone that is aiming for the top of the top positions it is important to have the most up-to-date information.

_**The project is to create a system that sends notification exclusivley on FAANG internship/new grad positions in the United States. (updates every hour).**_

## Features
- Users can recieve notifications on new FAANG internship/new grad positions in the United States through sms or email.
- Users can view the most up-to-date FAANG internship/new grad positions in the United States.

## Understanding the Code
This code leverages OOP allowing easy addition of new companies.:

- `send.py` is the main file that initiates all scraping and sending notifications.
- `/scrape` directory contains the main class that other company child classes inherit from.
- `/[company]` directory contains the classes that scrape the respective company's career page.

## Disclaimer
This web scraper is designed to operate in full compliance with legal and ethical standards to ensure responsible and lawful data extraction. Below are the key practices and guidelines our scraper follows:

1. Respecting robots.txt Files
Our scraper strictly adheres to the rules specified in the robots.txt files of target websites. 

2. Polite Crawling with Rate Limits
To avoid overloading web servers and ensure respectful access, our scraper implements rate limiting. Requests are configured to introduce delays between successive requests. This polite crawling approach helps maintain the performance and availability of the target websites.

3. Zero Monetization
This web scraper is used strictly for educational, research, or personal purposes and is not intended for commercial gain. I do not monetize the data extracted by our scraper. 