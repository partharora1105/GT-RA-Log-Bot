from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import pandas as pd


excel_file_path = 'input_sheet.xlsx'
form_link = "https://gatech.co1.qualtrics.com/jfe/form/SV_1YofsnFLCeTX8X4"


basic_info = list(pd.read_excel(excel_file_path).iloc[1, 0:6])
submit_form = True
building_name = "North Ave North, West"
ra_name = basic_info[0]
ra_email = basic_info[1]
sub_building_name = "NA"+basic_info[3]
floor_num = str(basic_info[5])

## Form Fields ##
id_of_building_dropdown = "QR~QID36"
id_of_name_dropdown = "QR~QID45"
id_of_email_input = "QR~QID38"
id_of_resident_name = "QR~QID2"
id_of_sub_building_dropdown = "QR~QID39"
id_of_nan_floor_dropdown = "QR~QID94"
id_of_naw_floor_dropdown = "QR~QID51"
floor_room_id_map = {
    "NAN2" : "69",
    "NAN3" : "60",
    "NAN4" : "61",
    "NAN5" : "62",
    "NAN6" : "63",
    "NAN7" : "64",
    "NAN8" : "65",
    "NAN9" : "66",
    "NAN10" : "67",
    "NAW1" : "59",
    "NAW2" : "54",
    "NAW3" : "55",
    "NAW4" : "56",
    "NAW5" : "57",
}
id_of_bedroom_dropdown = "QR~QID91"
id_of_date = "QR~QID3"
id_of_optional_text = "QR~QID49"
base_id_of_method = "QID48"
base_id_of_topic = "QID41"

def choose_dropdown(browser, dropdown_id, choosen_text):
    dropdown = Select(browser.find_element("id",dropdown_id ))
    dropdown.select_by_visible_text(choosen_text)

def enter_text(browser, input_id, text):
    input_field = browser.find_element("id", input_id)
    input_field.send_keys(text)

def choose_room(browser, room_num):
    q_id_num = floor_room_id_map[f"{sub_building_name}{floor_num}"]
    for i in range(100):
        id = f"QID{q_id_num}-{i}-label"
        try:
            button = browser.find_element("id", id)
        except:
            continue
        if button.text == room_num:
            button.click()
            break
    time.sleep(1.5)

def click_button(browser, id):
    browser.find_element("id", id).click()

def click_next(browser):
    click_button(browser,"NextButton")
    time.sleep(1.5)

def fill_form(browser, resident_name, room_num, bedroom,
              date, method_choice, topic_choice,
              optional_text):
    # Page 1
    choose_dropdown(browser, id_of_building_dropdown, building_name)
    click_next(browser)

    # Page 2
    choose_dropdown(browser, id_of_name_dropdown, ra_name)
    enter_text(browser, id_of_email_input, ra_email)
    click_next(browser)

    # Page 3
    enter_text(browser, id_of_resident_name, resident_name)
    choose_dropdown(browser, id_of_sub_building_dropdown, sub_building_name)
    click_next(browser)

    # Page 4
    choose_dropdown(browser, id_of_nan_floor_dropdown if sub_building_name == "NAN" else id_of_naw_floor_dropdown, floor_num)
    click_next(browser)

    # Page 5
    choose_room(browser, room_num)
    choose_dropdown(browser, id_of_bedroom_dropdown, bedroom)
    enter_text(browser, id_of_date, date)
    click_button(browser, f"{base_id_of_method}-{method_choice}-label")
    click_button(browser, f"{base_id_of_topic}-{topic_choice}-label")
    click_next(browser)

    # Page 6
    enter_text(browser, id_of_optional_text, optional_text)
    if (submit_form):
        click_next(browser)
    time.sleep(3)


def get_data():
    df = pd.read_excel(excel_file_path, skiprows=4)
    selected_data = df.iloc[:, :7]
    data_matrix = selected_data.values
    data_matrix = data_matrix[~pd.isna(data_matrix).any(axis=1)]
    return data_matrix

def log_interactions():
    data = get_data()
    browser = webdriver.Chrome()
    browser.get(form_link)
    for i in range(len(data)):
        entry = data[i]
        resident_name = entry[0]
        room_num = str(int(entry[1]))
        bedroom = entry[2]
        date = entry[3].strftime("%m-%d-%Y")
        method_choice = str(int(entry[4]))
        topic_choice = str(int(entry[5]))
        optional_text = entry[6]
        fill_form(browser, resident_name, room_num, bedroom,
                  date, method_choice, topic_choice,
                  optional_text)
        print(f"Completed for {resident_name}")
    browser.quit()

if __name__ == "__main__":
    log_interactions()



