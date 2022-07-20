from page_helper import  navigate, get_profile_link, get_profile_info
from to_csv import to_csv

# navigate to LinkedIn and login
driver, profiles = navigate()
# get links of profiles, LinkedIn only show connection info, 
# I use 20 profiles because of security purpose
link_list = get_profile_link(profiles, 20)
# get information
info_list = get_profile_info(link_list, driver)
header = ['First name', 'Last name', 'Label', 'Location', 'Gender']
# write to csv file
to_csv(header, info_list)

    

