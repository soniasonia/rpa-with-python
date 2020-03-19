import openpyxl
from selenium import webdriver

INPUT = "challenge.xlsx"
URL = "http://www.rpachallenge.com/movieSearch"


def get_data():
    driver = webdriver.Firefox()
    driver.get(URL)
    buttons = driver.find_elements_by_tag_name("button")
    js = '''
        var btns = document.getElementsByTagName("button");
        for (e of btns){    
            if (e.innerText == "GET POPULAR MOVIES"){
                e.click();
            }
        }

        var review_list = [];
            var icons = document.getElementsByClassName("instructionsDiv")[0].getElementsByTagName("i");
            for (icon of icons){
                if (icon.textContent == "comment"){
                  icon.click();  
                  var reviews = document.getElementsByClassName("modal-content")[0].getElementsByClassName("card");
                  for (review of reviews) {        
                    review_list.append(review.getElementsByTagName("p")[0].innerText);
                  }
                };
            }
    '''
    return driver.execute_script(js)

seba = get_data()
print(seba)