import requests, random, chromedriver_binary
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from gender_predictor import predict

def scrollpage(driver, scroll):
    SCROLL_PAUSE_TIME = 3

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    s = 0
    while s < scroll:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        s+=1

def save_img(link,name):
    response = requests.get(link) 
    image_path = 'images' + '/' + str(name) + '.jpg'
    with open(image_path, 'wb') as file:
        file.write(response.content)
    return image_path

def navigate():
    username = 'dangminhphat1@gmail.com'
    password = 'Tiennguyen381@l'
    url1 = 'https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'
    url2 = 'https://www.linkedin.com/company/hubspot/people/'
    driver = webdriver.Chrome(executable_path="driver/chromedriver")
    driver.get(url1)
    sleep(3)
    driver.maximize_window()
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    sleep(3)
    #driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button').click()
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    sleep(3)
    driver.get(url2)
    sleep(2)
    # scroll 7 times to get 200 profiles
    scrollpage(driver, 20)
    source = driver.page_source
    soup = BeautifulSoup(source, 'html.parser')
    profiles =  soup.find('div', class_="artdeco-card pv5 pl5 pr1 mt4").find_all('li', class_ = "grid grid__col--lg-8 pt5 pr4 m0")
    return driver, profiles

def get_profile_link(profiles, n_profiles):
    link_list = []
    item = 'https://www.linkedin.com/search/results/people/headless?currentCompany=%5B68529%5D&origin=FACETED_SEARCH'
    # use to get different link
    i = 0
    while len(link_list) < n_profiles:
        link = profiles[i].find('a', class_="app-aware-link link-without-visited-state").get('href')
        if(link != item):
            link_list.append(link)
        i+=1
    return link_list

def get_profile_info(link_list, driver):
    id = 0
    no_profile_pic = "data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"
    info_list = []
    for link in link_list:
        print(link)
        driver.get(link)
        p_source = driver.page_source
        p_soup = BeautifulSoup(p_source, 'html.parser')
        p_container = p_soup.find('div', class_="pv-text-details__left-panel")
        
        if p_container == None:
            p_container = p_soup.find('section', class_="top-card-layout container-lined overflow-hidden babybear:rounded-[0px]")
            name = p_container.find('h1', class_= "top-card-layout__title font-sans text-lg papabear:text-xl font-bold leading-open text-color-text mb-0").text.split(" ")
            label = p_container.find('h2', class_="top-card-layout__headline break-words font-sans text-md leading-open text-color-text").text
            location = p_container.find('span', class_="top-card__subline-item").text
            
        else:
            name = p_container.find('h1').text.split(" ")
            label = p_container.find('div', class_="text-body-medium break-words").get_text().strip()
            location = p_container.find('span', class_="text-body-small inline t-black--light break-words").get_text().strip()
        img_link = p_soup.find('div', class_="pv-top-card__non-self-photo-wrapper ml0").find('img').get('src')
        first_name = name[0]
        last_name = name[1]
        
        print(first_name)
        print(last_name)
        print(label)
        print(location)
        gender = ''
        if(img_link != no_profile_pic):
            path = save_img(img_link, id)
            gender = predict(path)
        else:
            gender = None
        id+=1
        info_list.append([first_name, last_name, label, location, gender])
        sleep(2)
    return info_list
    
