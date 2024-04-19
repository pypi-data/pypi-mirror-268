from browser import Browser 
from definition import Spreadsheet


import time 
bot = Browser()
bot.open_browser('https://booking.com/')

def click_dissmiss_sign_in():
    try:
        bot.click_by_aria_label("Dismiss sign-in info.")
    except Exception as e:
        print(e)

click_dissmiss_sign_in() 
bot.fill_by_id(':re:', 'Teresina')
bot.click_element_by_data_test_id("searchbox-dates-container")
bot.click_general_element("data-date", "2024-04-25")
bot.click_button_by_type("submit")

click_dissmiss_sign_in()
popular_filters = bot.get_webelements_by_id("filter_group_popular_:rj:")

bot.click_by_text(popular_filters, "Breakfast Included")
elements = bot.get_elements_by_data_test_id("property-card-container")

list_to_df = []
for i in elements:
    fields = i.text.split('\n')
    
    data_dict = {
        'name': fields[0],
        'location_info': fields[1],
        'distance_from_beach': fields[2],
        'rating': fields[3],
        'reviews': fields[4],
        'room_type': fields[5],
        'beds': fields[6],
        'cancellation_policy': fields[7],
        'availability_info': fields[8],
        'price_per_night': fields[9],
        'includes_taxes_and_fees': fields[10],
        'see_availability_link': fields[11]
    }
    list_to_df.append(data_dict)

spreadsheet = Spreadsheet()
spreadsheet.convert_list_to_excel(list_to_df, 'data.xlsx')

time.sleep(10)