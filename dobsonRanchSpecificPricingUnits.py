from datetime import datetime
from selenium import webdriver

def main(floorplan, file_name):
    # URL for prices of the apartments
    url = f"https://arizona.weidner.com/apartments/az/mesa/reflect-at-dobson-ranch/floorplans/{floorplan}"

    # Initialize driver
    driver = webdriver.Chrome()

    # Send a get request to the URL
    driver.get(url)

    # Set a variable for the returned html
    response_text = driver.page_source

    # Open file to write to
    # 'pricesUnit.txt'- prior file name
    file = open(file_name, 'a')
    file.write("Ran on " + str(datetime.now()) + "\n")
    file.write(floorplan + "\n")

    # Search the returned html for what we're looking for, prices, apartment numbers, and date available
    apartment_index = str.find(response_text, "Apartments Available")
    apartment_count = int(response_text[apartment_index-2 : apartment_index-1])

    # Loop through all available units and get the prices
    if(apartment_count > 0):
        for i in range(0, apartment_count):
            # Get apartment number
            apartment_number_index = str.find(response_text, "Apartment:")
            apartment_number = response_text[apartment_number_index+19 : apartment_number_index + 23]
            
            # Get date available
            date_available_index = str.find(response_text, "Date Available:")
            date_available = response_text[date_available_index+23 : date_available_index+34]
            # Get rid of the span tag if neeeded
            date_available = date_available.replace("</sp", '')
            date_available = date_available.replace("</s", '')
            date_available = date_available.replace("</", '')

            # Get cost
            cost_index = str.find(response_text, "Starting at:")
            cost = response_text[cost_index+20 : cost_index+26]
            
            # Save the name and value to the file
            file.write("Apartment: " + apartment_number + " - Monthly Rent: " + cost + " - " + "Date Available: " + date_available + "\n")

            # Remove the already found apartment from the response
            response_text = response_text[cost_index+26:]

    # Add space for next day
    file.write("\n")

    # Close the browser
    driver.close()

    # Close the file
    file.close()
    

def get_floorplan_details(floorplan, file_name):
    # URL for prices of the apartments
    url = f"https://arizona.weidner.com/apartments/az/mesa/reflect-at-dobson-ranch/floorplans/{floorplan}"

    # Intialize array of apartments
    apartment_details = []

    # Initialize driver
    driver = webdriver.Chrome()

    # Send a get request to the URL
    driver.get(url)

    # Set a variable for the returned html
    response_text = driver.page_source

    # Search the returned html for what we're looking for, prices, apartment numbers, and date available
    apartment_index = str.find(response_text, "Apartments Available")
    if(apartment_index != -1):
        apartment_count = int(response_text[apartment_index-2 : apartment_index-1])
    else:
        apartment_count = 0

    # Loop through all available units and get the prices
    if(apartment_count > 0):
        for i in range(0, apartment_count):
            # Get apartment number
            apartment_number_index = str.find(response_text, "Apartment:")
            apartment_number = response_text[apartment_number_index+19 : apartment_number_index + 23]
            
            # Get date available
            date_available_index = str.find(response_text, "Date Available:")
            date_available = response_text[date_available_index+23 : date_available_index+34]
            # Get rid of the span tag if neeeded
            date_available = date_available.replace("</sp", '')
            date_available = date_available.replace("</s", '')
            date_available = date_available.replace("</", '')

            # Get cost
            cost_index = str.find(response_text, "Starting at:")
            cost = response_text[cost_index+20 : cost_index+26]
            
            # Save the name and value to the file
            apartment_details.append("Apartment: " + apartment_number + " - Monthly Rent: " + cost + " - " + "Date Available: " + date_available + "\n")

            # Remove the already found apartment from the response
            response_text = response_text[cost_index+26:]

    # Close the browser
    driver.close()
    
    # Return the apartment details list
    return apartment_details

if __name__ == '__main__':
    main('artesa', 'pricesUnit.txt')