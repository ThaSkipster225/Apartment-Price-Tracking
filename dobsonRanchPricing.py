from datetime import datetime
import dobsonRanchSpecificPricingUnits
import pdb
from selenium import webdriver

def main(file_name):
    # URL for prices of the apartments
    url = "https://arizona.weidner.com/apartments/az/mesa/reflect-at-dobson-ranch/floorplans?Beds=2"
     # Initialize driver
    driver = webdriver.Chrome()

    # Send a get request to the URL
    driver.get(url)

    # Open file to write to
    file = open(file_name, 'a')
    file.write("Ran on " + str(datetime.now()) + "\n")

    # Search the returned html for what we're looking for, prices for 2 bed apartments
    responseText = driver.page_source

    # Loop through all apartment floorplans and get the prices
    for i in range(0, 10):
        # Narrow the search to smaller subsection of the returned HTML
        index = str.find(responseText, "Starting at")
        searchText = responseText[index:index+700]
        # Find the dollar value in the search text
        index_of_dollar = str.find(searchText, "$")
        value = searchText[index_of_dollar:index_of_dollar+6]
        # Find the name in the search text
        index_of_name = str.find(searchText, "/floorplans/")
        #pdb.set_trace()
        index_of_questionmark = str.find(searchText[index_of_name:], '?')
        name = searchText[index_of_name+len("/floorplans/"):index_of_name+index_of_questionmark]

        # Save the name and value to the file
        file.write(name + ": " + value + "\n")
        
        if(name == 'luna' or name == 'castello' or name == 'artesa'):
            # Call the other file to get the unit number and specific prices
            details = dobsonRanchSpecificPricingUnits.get_floorplan_details(name, file_name=file_name)
            
            for i in range (0, len(details)):
                file.write(details[i])

        # Remove the already found value from the text
        responseText = responseText[index+index_of_name + index_of_questionmark:]

    # Add space for next day
    file.write("\n")

    file.close()

    # Close the browser
    driver.close()
    
if __name__ == '__main__':
    main('prices.txt')