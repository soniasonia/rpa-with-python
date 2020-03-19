import openpyxl
from selenium import webdriver

INPUT = r"challenge.xlsx"
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

    javascript = '''var start = $("button.uiColorButton")[0]; 
                    var submit = $("input.uiColorButton")[0];
                    var data = ALL_MY_DATA;
                    start.click();    
                    for (case_ of data) {              
                        var fields = document.getElementsByTagName("rpa1-field");
                        for (field of fields) {
                          label_ = field.getAttribute("ng-reflect-dictionary-value");
                          field.getElementsByTagName("input")[0].value = case_[label_];                  
                        }
                        submit.click();
                    }
                    return dict'''.replace("ALL_MY_DATA", str(data))
    driver.execute_script(javascript)


data = get_data()
set_data(data)