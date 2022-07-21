import csv

# function to write csv file
def to_csv(header, info_list):
    
    with open('LinkedInUsersProfile.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(info_list)
    print('Done!')