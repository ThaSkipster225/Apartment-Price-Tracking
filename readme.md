Prerequisites:
- Selenium

These scripts were written specifically to work with https://arizona.weidner.com/apartments/az/mesa/reflect-at-dobson-ranch to track the prices of apartments at this complex.

To run this, simply activate your virtual environment if applicable, and then run dobsonRanchPricing.py
- The script will loop through all of the floor plans on the site and find the starting prices for a given floor plan. It will also run a different query to get all available 2 bed apartments for a given floor plan with their unit number, monthly rent price, and date of availability. We only run this extra query for 2 bed apartments, because at the time this script was created we were looking to upgrade to a 2 bed apartment and were specifically looking for a top floor 2 bed.
- The data gathered will be appended into a text file called prices.txt, which will automatically be created if it does not already exist in the folder where this file exists.
