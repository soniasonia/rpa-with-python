> RPA (Robotic process automation) is used when standard automation is not applicable because it is too expensive or take too much time versus the benefit that can be made by much faster RPA implementation. 
> RPA does not require any change in the application used in the process. Where there is no API available, RPA script (often called robot) can interact with existing GUI. It mimics human actions, like clicking button or setting text to the form. These actions are combined with reading data from/saving to documents like Word, Excel or DB.

###  Folders
1. ***python-exercises***
- RPA cases  in Python + Javascript, Selenium, openpyxl

2. ***robotframework-exercises***
- Exercises to get familiar with robotframework - open source framework for test automation 
and robotic process automation with human-readable syntax
[https://robotframework.org/](https://robotframework.org/)

### Exercises
1. [Rpa Challenge - Input Forms](http://www.rpachallenge.com/) - The goal is to input data from an Excel spreadsheet 
into a form fields on the web for 10 cases                                                                                                              

The fastest solution in Python with Selenium + Javascript uses JS for web interaction and execution 
takes 170 - 400 miliseconds.

Solution in robotframework has human-readable syntax compose from keywords. 
It takes 5-9 seconds to complete the task.
``` 
Challenge 1
    Open Challenge Website
    ${data} =   Get Data From Excel
    Click Element       css: button.uiColorButton
    FOR     ${row}     IN   @{data}
        Handle Row          ${row}
        Click Element       css: input.uiColorButton
    END
    Capture Page Screenshot
```