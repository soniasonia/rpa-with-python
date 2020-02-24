import openpyxl
from selenium import webdriver

INPUT = "challenge.xlsx"
URL = "http://www.rpachallenge.com/"


def get_data():
    wb = openpyxl.open(INPUT)
    ws = wb.active
    header = [ws.cell(1,col).value.strip() for col in range(1,8)]
    data = []
    for row in range(2, 12):
        case = {k: None for k in header}
        for col in range(1,8):
            case[header[col - 1]] = ws.cell(row,col).value
        data.append(case)
    return data


def set_data(data):
    driver = webdriver.Firefox()
    driver.get(URL)
    javascript = 'var start = $("button.uiColorButton")[0]; start.click();'
    driver.execute_script(javascript)
    for case in data:
        fill_form(driver, case)


def fill_form(driver, case):
    javascript = '''const x = document.getElementsByTagName("rpa1-field");
                    var dict = {};
                    for (e of x) {
                      label = e.getAttribute("ng-reflect-dictionary-value");
                      id = e.getElementsByTagName("input")[0].id;
                      dict[label] = id;
                    }
                    return dict'''
    web = driver.execute_script(javascript)
    for label in web.keys():
        id_ = web[label]
        value_ = case[label]
        javascript = f'document.getElementById("{id_}").value="{value_}"'
        driver.execute_script(javascript)
    javascript = 'submit = $("input.uiColorButton")[0]; submit.click();'
    driver.execute_script(javascript)


data = get_data()
set_data(data)