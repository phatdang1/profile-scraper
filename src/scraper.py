from page_helper import  navigate, get_profile_link, get_profile_info
from to_csv import to_csv

# navigate to LinkedIn and login
username = 'youremail@gmail.com'
password = 'yourpassword'
driver, profiles = navigate(username, password)
# get links of profiles, LinkedIn only show connection info, 
# I use 20 profiles because of security purpose
link_list = get_profile_link(profiles, 50)
# get information
info_list = get_profile_info(link_list, driver)
header = ['First name', 'Last name', 'Label', 'Location', 'Gender']
# write to csv file
to_csv(header, info_list)

    

