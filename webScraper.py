import os
import cv2
import selenium
from selenium import webdriver
import time
import datetime


def submit_assignment(targetWebsite = 'https://www.bartvsports.com.au/football/220827-nnsw-nplw-round-20-warners-bay-fc-w-v-maitland-fc-w/'):
	# Using Chrome to access web
	driver = webdriver.Chrome()

	time.sleep(5)

	# Open the website
	driver.get(targetWebsite)

	# Find and click on list of courses
	video_1 = driver.find_element_by_id('video929314')
	video_1.click()


	# Wait for the page to load
	time.sleep(2)

	return

if __name__ == "__main__":

	submit_assignment()