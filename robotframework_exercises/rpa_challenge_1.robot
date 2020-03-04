*** Settings ***
Metadata    Version        1.0
Documentation     RPA Challenge 1
Library           SeleniumLibrary
Library           ExcelLibrary
Library           Collections
Resource          ${INPUT}
Variables         config.yaml


*** Tasks ***
Challenge 1
    Open Challenge Website
    ${data} =   Get Data From Excel
    Click Element       css: button.uiColorButton
    FOR     ${row}     IN   @{data}
        Handle Row          ${row}
        Click Element       css: input.uiColorButton
    END
    Capture Page Screenshot

*** Keywords ***
Open Challenge Website
    Open Browser    ${URL}    ${BROWSER}
    Title Should Be     Rpa Challenge

Get Data From Excel
    Open Excel Document     filename=${INPUT}   doc_id=1
    @{data}=    Create List
    FOR     ${i}    IN RANGE    2   12
        ${row}=    Read Excel Row  row_num=${i}
        Append To List  ${data}     ${row}
    END
    [Return]    ${data}

Handle Row
    [Arguments]     ${row}
    FOR     ${index}    ${label}     IN ENUMERATE      @{LABELS}
        ${elem} =      GetWebElement    xpath://*[label="${label}"]/input
        Input Text  ${elem}  @{row}[${index}]
    END

