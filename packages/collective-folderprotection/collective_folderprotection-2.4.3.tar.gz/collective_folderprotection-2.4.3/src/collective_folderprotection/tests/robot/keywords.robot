*** Settings ***

Resource  plone/app/robotframework/keywords.robot

*** Variables ***

${ZOPE_URL} =  http://${ZOPE_HOST}:${ZOPE_PORT}
${PLONE_URL} =  ${ZOPE_URL}/plone
${BROWSER} =  Firefox

${protected_folder_url} =  ${PLONE_URL}/protected
${internal_protected} =  ${protected_folder_url}/a-page
${not_protected_folder_url} =  ${PLONE_URL}/not-protected
${internal_not_protected} =  ${not_protected_folder_url}/a-page

${MANAGER_USER_NAME} =  manager
${MANAGER_PASSWORD} =  manager
${CONTRIBUTOR_USER_NAME} =  contributor
${CONTRIBUTOR_PASSWORD} =  contributor

*** Keywords ***

Start browser
    Open browser  ${PLONE_URL}  browser=${BROWSER}

Custom Log out
    Go to  ${PLONE_URL}/logout
    Page should contain  logged out

Log In As Manager User
    Log in  ${MANAGER_USER_NAME}  ${MANAGER_PASSWORD}

Log In As Contributor User
    Log in  ${CONTRIBUTOR_USER_NAME}  ${CONTRIBUTOR_PASSWORD}

Click Add Folderish Protected
    Open Add New Menu
    Click Link  link=Folderish-Protected
    Page Should Contain  Add Folderish-Protected

Click Add Folderish Not Protected
    Open Add New Menu
    Click Link  link=Folderish-Not-Protected
    Page Should Contain  Folderish-Not-Protected

Click Add Page
    Open Add New Menu
    Click Link  link=Page
    Page Should Contain  Page

Custom Remove Content
    Click Delete Action
    Wait Until Page Contains Element  css=input#form-buttons-Delete
    Wait until keyword succeeds  2  2  Click Element  css=div.plone-modal-footer input#form-buttons-Delete
    Wait until keyword succeeds  40  1  Page should not contain element  css=div.plone-modal-dialog

Failed Remove Content
    Click Delete Action
    Wait Until Page Contains Element  css=input#form-buttons-Delete
    Click Element  css=div.plone-modal-footer input#form-buttons-Delete
    Page Should Contain  You do not have sufficient privileges to view this page

Rename Content
    [arguments]  ${old_id}  ${new_id}  ${new_title}

    Click Rename Action
    Wait Until Page Contains Element  css=input#form-widgets-new_id
    Input Text  css=input#form-widgets-new_id  ${new_id}
    Input Text  css=input#form-widgets-new_title  ${new_title}
    Click Element  css=div.plone-modal-footer input#form-buttons-Rename

Failed Rename Content
    [arguments]  ${old_id}  ${new_id}  ${new_title}

    Click Rename Action
    Wait Until Page Contains Element  css=input#form-widgets-new_id
    Input Text  css=input#form-widgets-new_id  ${new_id}
    Input Text  css=input#form-widgets-new_title  ${new_title}
    Click Element  css=div.plone-modal-footer input#form-buttons-Rename
    Page Should Contain  You do not have sufficient privileges to view this page

Create Password Protected Folder
    [arguments]  ${title}  ${password}
    Click Add Folderish Protected
    Input Text  css=input#form-widgets-IDublinCore-title  ${title}
    Input Text  css=input#form-widgets-IPasswordProtected-passw_hash  ${password}
    Click Button  Save
    Page Should Contain  Item created

Create Delete Protected Folder
    [arguments]  ${title}
    Click Add Folderish Protected
    Input Text  css=input#form-widgets-IDublinCore-title  ${title}
    Select Checkbox  css=input#form-widgets-IDeleteProtected-delete_protection-0
    Click Button  Save
    Page Should Contain  Item created

Create Rename Protected Folder
    [arguments]  ${title}
    Click Add Folderish Protected
    Input Text  css=input#form-widgets-IDublinCore-title  ${title}
    Select Checkbox  css=input#form-widgets-IRenameProtected-rename_protection-0
    Click Button  Save
    Page Should Contain  Item created

Create Protected Folder Disabled
    [arguments]  ${title}
    Click Add Folderish Protected
    Input Text  css=input#form-widgets-IDublinCore-title  ${title}
    Click Button  Save
    Page Should Contain  Item created

Create Not Protected Folder
    [arguments]  ${title}
    Click Add Folderish Not Protected
    Input Text  css=input#form-widgets-IDublinCore-title  ${title}
    Click Button  Save
    Page Should Contain  Item created

Create Page
    [arguments]  ${title}  ${summary}

    Click Add Page
    Input Text  css=input#form-widgets-IDublinCore-title  ${title}
    Input Text  css=textarea#form-widgets-IDublinCore-description  ${summary}
    Click Button  Save
    Page Should Contain  Item created
