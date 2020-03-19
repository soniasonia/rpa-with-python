# rpa-with-python
Repository with scripts for RPA 

> RPA (Robotic process automation) is used when standard automation is not applicable because it is too expensive or take too much time versus the benefit that can be made by much faster RPA implementation. 
> RPA does not require any change in the application used in the process. Where there is no API available, RPA script (often called robot) can interact with existing GUI. It mimics human actions, like clicking button or setting text to the form. These actions are combined with reading data from/saving to documents like Word, Excel or DB.

## robotframework-exercises
Exercise to get familiar with robotframework - open source framework for test automation and robotic process automation with human-readable syntax
[https://robotframework.org/](https://robotframework.org/)

### RPA Challenge
Solution for [Rpa Challenge - Input Forms](http://www.rpachallenge.com/) - The goal is to input data from am Excel spreadsheet into a form fields on the web. 

Syntax is human-readable keywords:
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
