from datetime import datetime
import dobsonRanchSpecificPricingUnits
import pdb
from selenium import webdriver

def main(file_name):
    # URL for prices of the apartments
    url = "https://arizona.weidner.com/apartments/az/mesa/reflect-at-dobson-ranch/floorplans"
     # Initialize driver
    driver = webdriver.Chrome()

    # Send a get request to the URL
    driver.get(url)

    # Open file to write to
    file = open(file_name, 'a')
    file.write("Ran on " + str(datetime.now()) + "\n")

    # Search the returned html for what we're looking for, prices for 2 bed apartments
    responseText = driver.page_source

    responseText = responseText.replace('\u2212','')
    responseText = responseText.replace('\u200e','')

    # Loop through all apartment floorplans and get the prices
    for i in range(0, 10):
        # Narrow the search to smaller subsection of the returned HTML
        index = str.find(responseText, "Starting at")
        searchText = responseText[index:index+1500]
        # Find the dollar value in the search text
        index_of_dollar = str.find(searchText, "$")
        value = searchText[index_of_dollar:index_of_dollar+6]
        # Find the name in the search text
        index_of_name = str.find(searchText, "/floorplans/")
        index_of_double_quote = str.find(searchText[index_of_name:], '"')
        name = searchText[index_of_name+len("/floorplans/"):index_of_name+index_of_double_quote]

        # If the length of the name is greater than 20, it couldn't be found, so move to next
        if(len(name) > 20):
            responseText = responseText[index+1500:]
        else:
            # Save the name and value to the file
            file.write(name + ": " + value + "\n")
        
        if(name == 'luna' or name == 'castello' or name == 'artesa'):
            # Call the other file to get the unit number and specific prices
            details = dobsonRanchSpecificPricingUnits.get_floorplan_details(name)
            
            for i in range (0, len(details)):
                file.write(details[i])

        # Remove the already found value from the text
        responseText = responseText[index+index_of_name + index_of_double_quote:]

    # Close the browser
    driver.close()

    # Add space for next day
    file.write("\n")

    # Close the file
    file.close()
    
if __name__ == '__main__':
    main('prices.txt')